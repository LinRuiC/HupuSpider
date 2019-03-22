# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HupuspiderItem(scrapy.Item):
    # 球队名称
    teamname = scrapy.Field()
    # 球队url
    teamurl = scrapy.Field()
    # 新闻标题
    newstitle=scrapy.Field()
    # 新闻链接
    newsurl=scrapy.Field()
    # 新闻内容
    content=scrapy.Field()
    # 新闻配图url
    imageurl=scrapy.Field()
