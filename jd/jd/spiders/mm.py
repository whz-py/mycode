# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class MmSpider(RedisSpider):
    name = 'mm'
    allowed_domains = ['ivsky.com']
    redis_key = "mm:start_url"
    # start_urls = ['https://www.ivsky.com/tupian/chuangyisucai_t19624/']

    def parse(self, response):
        li_list = response.css(".pli li")
        item = {}
        for li in li_list:
            item["url"] = "https:" + li.css("div a img::attr(src)").extract_first()
            item["title"] = li.css("div a img::attr(alt)").extract_first()
            yield item
        next_url = "https://www.ivsky.com" + response.css(".page-next::attr(href)").extract_first()
        print(next_url)
        if next_url is not None:
            yield scrapy.Request(next_url, self.parse)