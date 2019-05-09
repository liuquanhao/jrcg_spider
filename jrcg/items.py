# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JrcgItem(scrapy.Item):
    # 排名
    rank = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 连接地址
    link = scrapy.Field()
    # 观注人数
    count = scrapy.Field()
    # 状态 
    state = scrapy.Field()
    # 插入时间
    insert_time = scrapy.Field()
    # 来自哪个网站
    name = scrapy.Field()
