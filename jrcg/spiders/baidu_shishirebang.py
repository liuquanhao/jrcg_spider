# -*- coding: utf-8 -*-

import scrapy
from jrcg.items import JrcgItem


class BaiduShishirebangSpider(scrapy.Spider):
    name = 'baidu_shishirebang'
    allowed_domains = ['top.baidu.com']
    start_urls = ['http://top.baidu.com/buzz?b=1&fr=topbuzz_b341_c513']

    def parse(self, response):
        trlist = response.xpath('//table[@class="list-table"]//tr')
        for index, tr in enumerate(trlist):
            if index in (0, 2, 4, 6):
                continue
            jrcg = JrcgItem()
            jrcg['rank'] = tr.xpath('.//td[@class="first"]/span/text()').extract_first()
            jrcg['title'] = tr.xpath('.//td[@class="keyword"]/a/text()').extract_first()
            jrcg['link'] = tr.xpath('.//td[@class="keyword"]/a/@href').extract_first()
            jrcg['count'] = tr.xpath('.//td[@class="last"]/span/text()').extract_first()
            jrcg['name'] = 'baidushishirebang'
            yield jrcg
