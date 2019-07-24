# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['36kr.com']
    start_urls = ['https://36kr.com/']

    def start_requests(self):
        request = scrapy.Request(url='https://36kr.com/')
        request.meta['proxy'] = 'http://127.0.0.1:8888'
        yield request

    def parse(self, response):
        div_list = response.xpath('.//div[@class="hotlist-main"]/div')
        for index, div in enumerate(div_list):
            index += 1
            jrcg = JrcgItem()
            jrcg['rank'] = index
            if index in (1, 2):
                jrcg['title'] = div.xpath('./a[2]/p/text()').extract_first()
                jrcg['link'] = response.url[0:-1] + div.xpath('./a[2]/@href').extract_first()
            else:
                jrcg['title'] = div.xpath('./div[2]/a/text()').extract_first()
                jrcg['link'] = div.xpath('./div[2]/a/@href').extract_first()
            jrcg['name'] = self.name
            yield jrcg
