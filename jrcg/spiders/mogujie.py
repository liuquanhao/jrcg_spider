# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem
from scrapy_selenium import SeleniumRequest

class MogujieSpider(scrapy.Spider):
    name = 'mogujie'
    allowed_domains = ['www.mogu.com']
    #start_urls = ['https://www.mogu.com/']

    def start_requests(self):
        return [SeleniumRequest(url = "https://www.mogu.com/", callback = self.parse)]

    def parse(self, response):
        li_list = response.xpath('//div[@class="category-item header-category-topic"]/div[@class="header-category-container"]/ul/li')
        for index, li in enumerate(li_list):
            jrcg = JrcgItem()
            jrcg['rank'] = index + 1
            jrcg['title'] = li.xpath('.//a/text()').extract_first()
            jrcg['link'] = li.xpath('.//a/@href').extract_first()
            jrcg['name'] = 'mogujie'
            yield jrcg
