#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JvItem(Item):
    """
    text, url, retweetnum, commentnum, pdate, favonum
    """
    title = Field() #
    slug = Field() # JKSR-138
    category = Field() # 类别
    preview = Field() # url
    downloadurl = Field() # magnet:?xt=urn:btih:F661CCFFE
    actor = Field()
