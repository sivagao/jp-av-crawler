#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re

# add parent directory to path
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from items import JvItem

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

# define crawlerh
# scrapy crawl tb -a target=android -s LOG_FILE=scrapy_tb_android.log
# scrapy crawl tb_thread -a target=android -o data/android_threads.json -f json
class JvItemSpider(CrawlSpider):

    name = 'jv_genre_ne'
    allowed_domain = ['www.javlibrary.com']
    rules = (Rule(SgmlLinkExtractor(allow=(r'/\?v=jav.*',)), callback='parse_thread', follow=True),)
    magnet_regexp = re.compile('magnet[^<\s]*')

    def __init__(self, target=None, *args, **kwargs):
        super(JvItemSpider, self).__init__(*args, **kwargs)
        self.alias = target
        self.start_urls = ['http://www.javlibrary.com/cn/vl_genre.php?g=ne&page=%s' % pn for pn in range(1,101)]
        self.rules = (Rule(SgmlLinkExtractor(allow=(r'/\?v=jav.*',)), callback='parse_thread', follow=True),)

    def parse_thread(self, response):
        hxs = HtmlXPathSelector(response)
        items = []

        if self.magnet_regexp.findall(response.body):
            # item['downloadurl'] = self.magnet_regexp.findall(response.body)
            # print self.magnet_regexp.findall(response.body)[0]
            item = JvItem()
            item['preview'] = hxs.select("//*[@id='video_jacket_img']/@src").extract()[0]
            item['title'] = hxs.select("//h3/a/text()").extract()[0]
            item['downloadurl'] = self.magnet_regexp.findall(response.body)[0]
            item['slug'] = hxs.select('//*[@id="video_id"]/table/tr/td[2]/text()').extract()[0]
            item['category'] = hxs.select('//*[@class="genre"]/a/text()').extract()
            item['actor'] = hxs.select('//*[@class="star"]/a/text()').extract()
            print item
            items.append(item)
            return item
        return items
