# -*- coding: utf-8 -*-
import scrapy
import json

from zhihu.items import UserItem

class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['zhihu.com']
    # start_urls = ['http://zhihu.com/']

    user_name = "Germey"

    user_url = "https://www.zhihu.com/api/v4/members/{user}?include={include}"
    user_query = "allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"

    following_url = "https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}"
    following_query =  "data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics"

    followed_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"
    followed_query = "data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"

    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.user_name, include=self.user_query), callback=self.parse_user_info)
        yield scrapy.Request(self.following_url.format(user=self.user_name, include=self.following_query, offset=0, limit=20),  callback=self.parse_following)
        yield scrapy.Request(self.followed_url.format(user=self.user_name, include=self.followed_query, offset=0, limit=20),  callback=self.parse_followed)

    def parse_user_info(self, response):
        res = json.loads(response.text)
        item = UserItem()
        print(res)
        for info in res:
            item['user_name'] = info.get('name')
            item['user_personal_url'] = info.get('url')
            item['headline'] = info.get('headline')
            print(item)
        # for field in item.fields():
        #     print(field)
        #     if field in res.keys():
        #         item[field] = res.get(field)
        # yield item

    def parse_following(self, response):
        res = json.loads(response.text)
        if "data" in res.keys():
            for result in res.get("data"):
                url_token = result.get("url_token")
                yield scrapy.Request(self.user_url.format(user=url_token, include=self.user_query), callback=self.parse_user_info)

        if "paging" in res.keys() and res.get("paging").get("is_end") == False:
            yield scrapy.Request(res.get("paging").get("next"), callback=self.parse_following)

    def parse_followed(self, response):
        res = json.loads(response.text)
        if "data" in res.keys():
            for result in res.get("data"):
                url_token = result.get("url_token")
                yield scrapy.Request(self.user_url.format(user=url_token, include=self.user_query),
                                     callback=self.parse_user_info)

        if "paging" in res.keys() and res.get("paging").get("is_end") == False:
            yield scrapy.Request(res.get("paging").get("next"), callback=self.parse_followed)

