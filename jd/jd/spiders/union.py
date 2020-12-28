# -*- coding: utf-8 -*-
import scrapy
import json

class UnionSpider(scrapy.Spider):
    name = 'union'
    allowed_domains = ['union.jd.com']
    start_urls = ['https://union.jd.com/api/goods/search']

    def start_requests(self):
        data = {
            "pageNo": "1",
            "pageSize": "60",
            "searchUUID": "998216089cb9496689ae407d640a0b9c",
            "data": {
                "bonusIds": None,
                "cat2Id": None,
                "cat3Id": None,
                "categoryId": None,
                "deliveryType": "0",
                "fromCommissionRatio": None,
                "fromPrice": None,
                "hasCoupon": "0",
                "isCare": "0",
                "isHot": None,
                "isPinGou": "0",
                "isZY": "0",
                "key": None,
                "keywordType": "kt0",
                "lock": "0",
                "orientationFlag": "0",
                "searchType": "st3",
                "sort": None,
                "sortName": None,
                "toCommissionRatio": None,
                "toPrice": None
            }
        }
        yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse)

    def parse(self, response):
        res = json.loads(response.text)
        print(res)
