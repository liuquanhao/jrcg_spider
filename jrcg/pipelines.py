# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
# import time
import redis
import json
# from jrcg.items import JrcgItem

class MysqlPipeline(object):
    # def __init__(self):
    #     self.conn = MySQLdb.connect(host = "127.0.0.1", port = 33060, user = "homestead", password = "secret", database = "jrcg", charset="utf8", use_unicode=True)
    #     self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # if not isinstance(item, WeiboItem):
        #     return item
        # # item.setdefault('rank', 0)
        # # item.setdefault('title', '-')
        # # item.setdefault('link', '-')
        # # item.setdefault('count', 0)
        # # item.setdefault('state', '-')
        # try:
        #     self.cursor.execute("INSERT INTO weibo_items (rank, title, link, count, state, insert_time) VALUES (%s, %s, %s, %s, %s, %s  )", (item['rank'], item['title'], item['link'], item['count'], item['state'], int(time.time())))
        #     self.conn.commit()
        # except Exception as e:
        #     print("Error: " + str(e))
        return item

class RedisPipeline(object):
    def __init__(self, host, port):
        pool = redis.ConnectionPool(host=host, port=port)
        self.rds = redis.Redis(connection_pool=pool)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('REDIS_HOST'), port=crawler.settings.get('REDIS_PORT'))

    def process_item(self, item, spider):
        arow = json.dumps(dict(item), ensure_ascii=False)
        self.rds.zremrangebyrank(item['name'], item['rank'], item['rank'])
        self.rds.zadd(item['name'], {arow: item['rank']})
        return item
