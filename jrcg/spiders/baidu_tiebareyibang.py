# -*- coding: utf-8 -*-
import scrapy
import json
from jrcg.items import JrcgItem

class BaiduTiebareyibangSpider(scrapy.Spider):
    name = 'baidu_tiebareyibang'
    allowed_domains = ['tieba.baidu.com']

    def start_requests(self):
        request = scrapy.Request(url="http://tieba.baidu.com/hottopic/browse/topicList")
        request.meta['proxy'] = "http://127.0.0.1:8081"
        yield request

    def parse(self, response):
        res = json.loads(response.text)
        item_list = res['data']['bang_topic']['topic_list']
        for index, item in enumerate(item_list):
            jrcg = JrcgItem()
            jrcg['rank'] = index + 1
            jrcg['title'] = item['topic_name']
            jrcg['link'] = item['topic_url']
            jrcg['count'] = item['discuss_num']
            jrcg['name'] = 'baidu_tiebareyibang'
            yield jrcg

