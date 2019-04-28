# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    count = scrapy.Field()
    state = scrapy.Field()
    insert_time = scrapy.Field()
