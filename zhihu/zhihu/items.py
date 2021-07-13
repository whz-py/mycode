# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    avatar_url_template = scrapy.Field()
    url = scrapy.Field()
    headline = scrapy.Field()
    is_vip = scrapy.Field()
    follower_count = scrapy.Field()

# class ZhihuItem(scrapy.Item):
#     follower_count = scrapy.Field()
#     user_name = scrapy.Field()

