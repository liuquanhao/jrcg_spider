# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class Weixin24hrewenbangSpider(scrapy.Spider):
    name = 'weixin_24hrewenbang'
    allowed_domains = ['gsdata.cn']
    start_urls = ['http://www.gsdata.cn/rank/wxarc']

    def parse(self, response):
       tr_list = response.xpath('.//table[@id="rank_data"]/tbody/tr') 
       for index, tr in enumerate(tr_list):
           jrcg = JrcgItem()
           jrcg['rank'] = index + 1
           jrcg['title'] = tr.xpath('.//td[1]/span/a/text()').extract_first()
           jrcg['link'] = tr.xpath('.//td[1]/span/a/@href').extract_first()
           jrcg['name'] = self.name 
           yield jrcg
