# -*- coding: utf-8 -*-
import scrapy
import json
import pickle
import urllib.parse
import requests

from selenium import webdriver
from jsonpath import jsonpath
from jd.items import Product
from scrapy_redis.spiders import RedisSpider


class JdProductSpider(RedisSpider):
    name = 'jd_product'
    allowed_domains = ['jd.com', 'p.3.cn']
    # allowed_domains = ['httpbin.org']
    # start_urls = ['http://jd.com/']
    redis_key = "jd_product:category"

    # def start_requests(self):
    #     for i in range(1, 2):
    #         url = "http://httpbin.org/get"
    #         yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    #
    # def parse(self, response):
    #     print(json.loads(response.text)['ip'])
    #     print(json.loads(response.text)['port'])



    # def start_requests(self):
    #     categorys = {"b_cate_url": "https://jiadian.jd.com",
    #                  "b_cate_name": "家用电器",
    #                  "m_cate_url": "https://phat.jd.com/10-108.html",
    #                  "m_cate_name": "厨卫大电",
    #                  "s_cate_url": "https://list.jd.com/list.html?cat=737,13297,18577",
    #                  "s_cate_name": "空气能热水器"
    #                  }
    #     yield scrapy.Request(categorys["s_cate_url"], callback=self.parse, meta={"categorys": categorys})

    def make_request_from_data(self, data):
        '''
        从redis中自动读取的二进制数据，构建请求
        :param data: 分类信息的二进制数据
        :return: 返回根据小分类构建的请求
        '''

        # 把二进制数据loads成字典
        categorys = pickle.loads(data)
        # 注意此处只能用return， 可以ctrl + B 查看源码
        return scrapy.Request(categorys["s_cate_url"], callback=self.parse, meta={"categorys": categorys})

    def parse(self, response):
        categorys = response.meta["categorys"]
        sku_ids = response.xpath("//div[@id='J_goodsList']/ul/li/@data-sku").extract()
        for sku_id in sku_ids:
            item = Product()
            item["product_sku_id"] = sku_id
            item["product_category"] = categorys
            # 这个商品的url一直没找到，这里找到其他人之前的url，发现可用。
            product_base_url = "https://cdnware.m.jd.com/c1/skuDetail/android/6.2.3/{}.json".format(sku_id)
            yield scrapy.Request(
                product_base_url,
                callback=self.parse_product_detail,
                meta={"item": item}
            )

    # 获取商品信息
    def parse_product_detail(self, response):
        item = response.meta["item"]
        result = json.loads(response.text)
        try:
            item["product_name"] = result["wareInfo"]["basicInfo"]["name"]
            item["product_img_url"] = result["wareInfo"]["basicInfo"]["wareImage"][0]["small"]
            item["product_book_info"] = result["wareInfo"]["basicInfo"]["bookInfo"]
            color_size = jsonpath(result, "$..colorSize")
            if color_size:
                color_size = color_size[0]
                product_option = {}
                for info in color_size:
                    title = info["title"]
                    value = jsonpath(info, "$..text")
                    product_option[title] = value
                    item["product_option"] = product_option
            shop = jsonpath(result, "$..shop")
            if shop:
                shop = shop[0]
                if shop:
                    item["product_shop"] = {
                        "shop_id": shop["shopId"],
                        "shop_name": shop["name"],
                        "shop_score": shop["score"]
                    }
                else:
                    item["product_shop"] = {
                        "shop_name": "JD自营"
                    }
            item["product_category_id"] = result["wareInfo"]["basicInfo"]["category"]
            item["product_category_id"] = item["product_category_id"].replace(";", ",")
        except Exception as e:
            print(e)

        # 促销广告
        ad_url = "https://cd.jd.com/promotion/v2?skuId={}&area=22_1930_49324_0&cat={}".format(item["product_sku_id"], item["product_category_id"])
        yield scrapy.Request(ad_url, callback=self.parse_product_ad, meta={"item": item})

    def parse_product_ad(self, response):
        item = response.meta["item"]
        try:
            results = json.loads(response.text)
            item["product_ad"] = jsonpath(results, "$..ad")[0]
        except Exception as e:
            print(e)

        comment_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}".format(item["product_sku_id"])
        yield scrapy.Request(comment_url, callback=self.parse_comments, meta={"item": item})


    def parse_comments(self, response):
        item = response.meta["item"]
        try:
            results = json.loads(response.text)
            item["product_comments"] = results["CommentsCount"][0]["CommentCount"]
            item["product_good_comments"] = results["CommentsCount"][0]["GoodCount"]
            item["product_poor_comments"] = results["CommentsCount"][0]["PoorCount"]
        except Exception as e:
            print(e)

        price_url = "https://p.3.cn/prices/mgets?skuIds={}".format(item["product_sku_id"])
        yield scrapy.Request(price_url, callback=self.parse_product_price, meta={"item": item})

    def parse_product_price(self, response):
        item = response.meta["item"]
        result = json.loads(response.text)
        item["product_price"] = result[0]["p"]
        print(item)
        yield item









