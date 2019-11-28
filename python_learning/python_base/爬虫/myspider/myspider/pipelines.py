# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient


# json
class JsonWritespiderPipeline(object):  
    def process_item(self, item, spider):
        with open('temp.txt','a+')as f:
            json.dump(item,f,ensure_ascii=False,indent=2)  # item:爬虫返回的dict数据，然后保存到文本temp.txt
        return item  # item获取完了之后要释放，否则权重比较靠后的管道就获取不了item


# mongoDB
class DyMongospiderPipeline(object):  
    def open_spider(self,spider):
        client = MongoClient(spider.settings.get("HOST"),spider.settings.get("PORT"))
        self.db = client['dytv']['dy_hpjy']  # 相当于[数据库名][表名]

    def process_item(self, item, spider):
        self.db.insert_one(dict(item))
        return item


# mysql
class DyMysqlspiderPipeline(object):
    def process_item(self, item, spider):
        pass