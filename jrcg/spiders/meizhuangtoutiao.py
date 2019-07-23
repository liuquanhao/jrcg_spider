# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class MeizhuangtoutiaoSpider(scrapy.Spider):
    name = 'meizhuangtoutiao'
    allowed_domains = ['www.mztoutiao.com']
    start_urls = ['http://www.mztoutiao.com/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="index_content_left_box2"]/ul[@class="list"]/li')
        for index, li_list in enumerate(li_list):
            jrcg = JrcgItem()
            jrcg['rank'] = index + 1
            jrcg['title'] = li.xpath('.//div[@class="index_content_left_box2_List_tit"]/a/text()').extract_first()
            jrcg['link'] = response.url[0:-1] + li.xpath('.//div[@class="index_content_left_box2_List_tit"]/a/@href').extract_first()
            jrcg['name'] = 'meizhuangtoutiao'
            yield jrcg
