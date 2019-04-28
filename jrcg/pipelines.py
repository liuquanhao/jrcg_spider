# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import time
from jrcg.items import WeiboItem

class WeiboPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host = "127.0.0.1", port = 33060, user = "homestead", password = "secret", database = "jrcg", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if not isinstance(item, WeiboItem):
            return item
        # item.setdefault('rank', 0)
        # item.setdefault('title', '-')
        # item.setdefault('link', '-')
        # item.setdefault('count', 0)
        # item.setdefault('state', '-')
        try:
            self.cursor.execute("INSERT INTO weibo_items (rank, title, link, count, state, insert_time) VALUES (%s, %s, %s, %s, %s, %s  )", (item['rank'], item['title'], item['link'], item['count'], item['state'], int(time.time())))
            self.conn.commit()
        except Exception as e:
            print("Error: " + str(e))
        return item
