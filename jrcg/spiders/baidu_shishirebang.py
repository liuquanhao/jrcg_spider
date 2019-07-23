# -*- coding: utf-8 -*-

import scrapy
from jrcg.items import JrcgItem

class BaiduShishirebangSpider(scrapy.Spider):
    name = 'baidu_shishirebang'
    allowed_domains = ['top.baidu.com']

    def start_requests(self):
        request = scrapy.Request(url="http://top.baidu.com/buzz?b=1&fr=topbuzz_b341_c513")
        request.meta['proxy'] = "http://127.0.0.1:8081"
        yield request

    def parse(self, response):
        response = response.replace(encoding='gb18030')
        trlist = response.xpath('//table[@class="list-table"]//tr')
        for index, tr in enumerate(trlist):
            if index in (0, 2, 4, 6):
                continue
            jrcg = JrcgItem()
            jrcg['rank'] = tr.xpath('.//td[@class="first"]/span/text()').extract_first()
            jrcg['title'] = tr.xpath('.//td[@class="keyword"]/a/text()').extract_first()
            jrcg['link'] = tr.xpath('.//td[@class="keyword"]/a/@href').extract_first()
            jrcg['count'] = tr.xpath('.//td[@class="last"]/span/text()').extract_first()
            jrcg['name'] = 'baidu_shishirebang'
            yield jrcg
