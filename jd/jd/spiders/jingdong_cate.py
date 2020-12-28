# -*- coding: utf-8 -*-
import scrapy
import json

from jd.items import JdItem

class JingdongSpider(scrapy.Spider):
    name = 'jingdong_cate'
    allowed_domains = ['jd.com']
    start_urls = ['https://dc.3.cn/category/get']   # 分类的url

    def parse(self, response):
        # 解码方式是GBK，默认utf8会显示乱码
        result = json.loads(response.body.decode('GBK'))
        item = JdItem()
        if result['data']:
            # 分类都在datas里面
            datas = result["data"]
            # 首先是大分类
            for data in datas:
                b_cates = data['s'][0]
                b_cate = b_cates["n"]
                # print("大分类：{}".format(b_cate))
                # 专门写个函数来获得分类的url和名称，把分类传给该函数
                item["b_cate_url"], item["b_cate_name"] = self.get_info_cate(b_cate)
                # 中分类在大分类下面一级，和n同一级
                m_catess = b_cates['s']
                # 中分类下有很多分类，先遍历中分类
                for m_cates in m_catess:
                    m_cate = m_cates["n"]
                    # print("中分类：{}".format(m_cate))
                    # 调用分类函数
                    item["m_cate_url"], item["m_cate_name"] = self.get_info_cate(m_cate)
                    # 小分类在中分类下和n同一级
                    s_catess = m_cates['s']
                    # 遍历小分类
                    for s_cates in s_catess:
                        s_cate = s_cates["n"]
                        # print("小分类：{}".format(s_cate))
                        item["s_cate_url"], item["s_cate_name"] = self.get_info_cate(s_cate)
                        # print(item)
                        yield item


    def get_info_cate(self, category_info):
        # 分类有3中，首先用|分开，来获得url和名称
        category = category_info.split('|')
        category_url = category[0]
        category_name = category[1]
        # 如果分开后的url中含有1个jd.com，直接补全url
        if category_url.count("jd.com") == 1:
            category_url = "https://" + category_url
        # 如果分开后的url中只含有一个-, 那取找中分类的url，然后补全
        elif category_url.count("-") == 1:
            category_url = "https://channel.jd.com/{}.html".format(category_url)
        else:
            # 上面两个都不是的话，就用，替换掉 - ，然后补全url
            category_url = category_url.replace("-", ",")
            category_url = "https://list.jd.com/list.html?cat={}".format(category_url)
        #
        return category_url, category_name

