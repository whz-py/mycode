# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from jd.spiders.jingdong_cate import JingdongSpider


class CategoryPipeline(object):

    def open_spider(self, spider):
        if isinstance(spider, JingdongSpider):
            # 连接 mongodb数据库
            self.client = pymongo.MongoClient(host="localhost", port=27017)
            self.collection = self.client['jd']['categorys']

    def process_item(self, item, spider):
        if isinstance(spider, JingdongSpider):
            self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        if isinstance(spider, JingdongSpider):
            self.client.close()
