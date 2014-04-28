#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from pymongo import Connection
import urllib
from scrapy.exceptions import DropItem

connection = Connection('localhost', 27017) # the default is 27017
db_jv = connection.jv

class TiebaPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        """
            For each item, insert into mongodb as dict
        """
        # TODO: add more check here
        # collection names as spider.name
        db_jv[spider.name].insert(dict(item))
        return item
