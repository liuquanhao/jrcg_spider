# -*- coding: utf-8 -*-

import scrapy
import re
import json
from jrcg.items import JrcgItem

class MogujieSpider(scrapy.Spider):
    name = 'mogujie'
    allowed_domains = ['www.mogu.com']
    start_urls = ['https://mce.mogucdn.com/jsonp/multiget/3?pids=132244%2C132263%2C137170&callback=httpCb156385075444744&_=1563850754447']

    def parse(self, response):
        res = re.search('{.*}', response.text).group()
        objs = json.loads(res)
        li_list = objs['data']['137170']['list']
        for index, li in enumerate(li_list):
            if index == 0:
                continue
            jrcg = JrcgItem()
            jrcg['rank'] = index
            jrcg['title'] = li['title'].strip('#')
            jrcg['link'] = li['link']
            jrcg['name'] = 'mogujie'
            yield jrcg
