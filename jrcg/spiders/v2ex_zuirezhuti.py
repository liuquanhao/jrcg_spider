# -*- coding: utf-8 -*-
import scrapy
import json
from jrcg.items import JrcgItem

class V2exZuirezhutiSpider(scrapy.Spider):
    name = 'v2ex_zuirezhuti'
    allowed_domains = ['www.v2ex.com']
    start_urls = ['https://www.v2ex.com/api/topics/hot.json']

    def parse(self, response):
        res = json.loads(response.text)
        for index, item in enumerate(res):
            jrcg = JrcgItem()
            jrcg['rank'] = index + 1
            jrcg['title'] = item['title']
            jrcg['link'] = item['url']
            jrcg['count'] = item['replies']
            jrcg['name'] = 'v2ex_zuirezhuti'
            yield jrcg
