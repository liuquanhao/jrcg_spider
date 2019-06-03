# -*- coding: utf-8 -*-
import scrapy
from jrcg.items import JrcgItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot/']

    def parse(self, response):
        tr_list = response.xpath("//*[@id='pl_top_realtimehot']/table/tbody/tr")
        for index, tr in enumerate(tr_list):
            jrcg = JrcgItem()
            if index == 0:
                jrcg['rank'] = 0
            else:
                jrcg['rank'] = int(tr.xpath(".//td[position()=1]/text()").extract_first(default = 0))
            jrcg['title'] = tr.xpath(".//td[position()=2]/a/text()").extract_first(default = '-')
            jrcg['link'] = "https://s.weibo.com" + tr.xpath(".//td[position()=2]/a/@href").extract_first(default = '-')
            jrcg['count'] = int(tr.xpath(".//td[position()=2]/span/text()").extract_first(default = 0))
            jrcg['state'] = tr.xpath(".//td[position()=3]/i/text()").extract_first(default = '')
            jrcg['name'] = 'weibo'
            yield jrcg
