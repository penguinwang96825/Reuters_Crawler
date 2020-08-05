# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ReutersCrawlerPipeline(object):
	def open_spider(self, spider):
		self.con = sqlite3.connect("reuters.db")
		self.cur = self.con.cursor()

    def process_item(self, item, spider):
    	insert_query = \
    		"""
    		INSERT INTO reuters (title, text, date)
    		VALUES('{}', '{}', '{}')
    		""".format(item['title'], item['text'], item['date'])
    	self.cur.execute(insert_query)
        return item

    def spider_close(self, spider):
    	self.con.close()