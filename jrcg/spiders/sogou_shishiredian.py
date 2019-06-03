# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class SogouSpider(scrapy.Spider):
    name = 'sogou_shishiredian'
    allowed_domains = ['top.sogou.com']
    start_urls = ['http://top.sogou.com/hot/shishi_1.html', 'http://top.sogou.com/hot/shishi_2.html', 'http://top.sogou.com/hot/shishi_3.html']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='pub-list']/li")
        for index, li in enumerate(li_list):
            jrcg = JrcgItem()
            if index in (0, 1, 2):
                jrcg['rank'] = li.xpath(".//span[@class='s1']/a/i/text()").extract_first()
            else:
                jrcg['rank'] = li.xpath(".//span[@class='s1']/i/text()").extract_first()
            jrcg['title'] = li.xpath(".//span[@class='s2']/p/a/text()").extract_first()
            jrcg['link'] = li.xpath(".//span[@class='s2']/p/a/@href").extract_first()
            jrcg['count'] = li.xpath(".//span[@class='s3']/text()").extract_first()
            jrcg['name'] = 'sogou_shishiredian'
            yield jrcg
