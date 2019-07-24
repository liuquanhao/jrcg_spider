# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from jrcg.items import JrcgItem
from scrapy.selector import Selector

class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/top']

    def parse(self, response):
        li_list_str = response.xpath('.//div[@id="list-hotposts"]/ol/script/text()').extract_first().strip()
        li_list_str = re.search(r'\'(.*)\'', li_list_str).group(1)
        li_list_str = urllib.parse.unquote(li_list_str)
        li_list = Selector(text=li_list_str).xpath('.//li')
        for index, li in enumerate(li_list):
            jrcg = JrcgItem()
            jrcg['rank'] = index + 1
            jrcg['title'] = li.xpath('./a/text()').extract_first()
            jrcg['link'] = li.xpath('./a/@href').extract_first()
            jrcg['name'] = self.name
            yield jrcg
