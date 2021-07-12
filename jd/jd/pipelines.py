# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from jd.spiders.jingdong_cate import JingdongSpider
from jd.spiders.jd_product import JdProductSpider

class CategoryPipeline(object):

    def open_spider(self, spider):
        if isinstance(spider, JingdongSpider):
            # 连接 mongodb数据库
            self.client = pymongo.MongoClient(host="localhost", port=27017)
            self.collection = self.client['jd']['categorys']

    def process_item(self, item, spider):
        if isinstance(spider, JingdongSpider):
            self.collection.insert_one(dict(item))
            print("成功插入一条数据")
        return item

    def close_spider(self, spider):
        if isinstance(spider, JingdongSpider):
            self.client.close()

class ProductPipeline(object):

    def open_spider(self, spider):
        if isinstance(spider, JdProductSpider):
            # 连接 mongodb数据库
            self.client = pymongo.MongoClient(host="localhost", port=27017)
            self.collection = self.client['jd']['products']

    def process_item(self, item, spider):
        if isinstance(spider, JdProductSpider):
            self.collection.insert_one(dict(item))
            # print("成功插入一条数据")
        return item


    def close_spider(self, spider):
        if isinstance(spider, JdProductSpider):
            self.client.close()


class MmeiPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'mm':
            self.client = pymongo.MongoClient(host='localhost', port=27017)
            self.db = self.client['meinv']['mm']


    def process_item(self, item, spider):
        if spider.name == 'mm':
            self.db.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        if spider.name == 'mm':
            self.client.close()