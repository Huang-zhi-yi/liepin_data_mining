# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import json

class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    liepin_xueli=scrapy.Field()
    liepin_jingyan=scrapy.Field()
    job_xinshui=scrapy.Field()
    job_shijian=scrapy.Field()
    job_zhicheng=scrapy.Field()
    job_company_name=scrapy.Field()
    job_url=scrapy.Field()
    job_company_url=scrapy.Field()
   