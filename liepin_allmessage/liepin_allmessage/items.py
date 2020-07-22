# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinAllmessageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    职位=scrapy.Field()
    公司名字=scrapy.Field()
    公司链接=scrapy.Field()
    薪水=scrapy.Field()
    工作城市=scrapy.Field()
    学历要求=scrapy.Field()
    经验要求=scrapy.Field()
    语言要求=scrapy.Field()
    年龄要求=scrapy.Field()
    职位描述=scrapy.Field()
    公司介绍=scrapy.Field()
    公司规模=scrapy.Field()
    工作地点=scrapy.Field()
    注册资本=scrapy.Field()
    注册时间=scrapy.Field()
    经营范围=scrapy.Field()