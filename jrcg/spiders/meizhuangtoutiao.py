# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class MeizhuangtoutiaoSpider(scrapy.Spider):
    name = 'meizhuangtoutiao'
    allowed_domains = ['www.mztoutiao.com']
    start_urls = ['http://www.mztoutiao.com/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="index_content_right_league_content"]/ul/li')
        for index, li in enumerate(li_list):
            jrcg = JrcgItem()
            jrcg['rank'] = int(li.xpath('.//span/text()').extract_first())
            jrcg['title'] = li.xpath('.//a/text()').extract_first().strip()
            jrcg['link'] = response.url[0:-1] + li.xpath('.//a/@href').extract_first()
            jrcg['name'] = 'meizhuangtoutiao'
            yield jrcg
