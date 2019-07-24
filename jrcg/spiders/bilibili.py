# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking/all/0/0/1']

    def parse(self, response):
        li_list = response.xpath('.//ul[@class="rank-list"]/li')
        for li in li_list:
            jrcg = JrcgItem()
            jrcg['rank'] = li.xpath('./div[@class="num"]/text()').extract_first()
            jrcg['title'] = li.xpath('./div[@class="content"]/div[@class="info"]/a/text()').extract_first()
            jrcg['link'] = 'https:' + li.xpath('./div[@class="content"]/div[@class="info"]/a/@href').extract_first()
            jrcg['count'] = li.xpath('./div[@class="content"]/div[@class="info"]/div[@class="detail"]/span/text()').extract_first()
            jrcg['name'] = self.name
            yield jrcg
