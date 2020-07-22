# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from liepin_allmessage.items import LiepinAllmessageItem
df=pd.read_excel('C:\\Users\\1\\代码\\data_mining\\Spring20_Web_Mining\\20春_Web_Mining_week14\\20春_Web_Mining_week14\\20春_Web_Mining_week14\\scaryproject\\liepin\\猎聘网教育相关岗位信息.xlsx')

#with open("猎聘数据挖掘职位信息.xlsx" ,"rb") as f:
df_职位链接=df["链接"].to_list()
class LiepinAllmessagespiderSpider(scrapy.Spider):
    name = 'liepin_allmessageSpider'
    allowed_domains = ['www.liepin.com']
    start_urls =df_职位链接
    def parse(self, response):
        item=LiepinAllmessageItem()
        zhiwei= response.xpath('//div[@class="title-info"]/h1/@title')[0].extract()
        company_name=response.xpath('//div[@class="title-info"]/h3/a/@title')[0].extract()
        company_url=response.xpath('//div[@class="title-info"]/h3/a/@href')[0].extract()
        xinshui=response.xpath('//p[@class="job-item-title"]//text()')[0].extract().strip()
        gongzuodidian=response.xpath('//p[@class="basic-infor"]/span/a/text()')[0].extract()
        job_qualifications_xueli=response.xpath('//div[@class="job-qualifications"]/span[1]/text()')[0].extract()
        job_qualifications_jingyan=response.xpath('//div[@class="job-qualifications"]/span[2]/text()')[0].extract()
        job_qualifications_yuyan=response.xpath('//div[@class="job-qualifications"]/span[3]/text()')[0].extract()
        job_qualifications_nianling=response.xpath('//div[@class="job-qualifications"]/span[4]/text()')[0].extract()
        zhiwei_miaoshu=''.join(response.xpath('//div[contains(@class,"job-description")]/div//text()').extract())
        #print(zhiwei_miaoshu)
        company_jieshao=response.xpath('//div[@class="info-word"]//text()')[0].extract().strip()
        #侧边栏
        #industry=response.xpath('//ul[@class="new-compintro"]/li[1]/a/@title')[0].extract()
        guimo=response.xpath('//ul[@class="new-compintro"]/li[2]/text()').extract()[0].split("：")[1]#.split(":")#[1]
        location=response.xpath('//ul[@class="new-compintro"]/li[3]/text()').extract()[0].split("：")[1]
        zhuceshijian =response.xpath('//ul[@class="new-compdetail"]/li[1]/text()')[0].extract().split("：")[1]
        zhuceziben=response.xpath('//ul[@class="new-compdetail"]/li[2]/text()')[0].extract().split("：")[1]
        jingyingfanwei=response.xpath('//ul[@class="new-compdetail"]/li[4]/text()')[0].extract()
        item["职位"]=zhiwei
        item["公司名字"]=company_name
        item["公司链接"]=company_url
        item["薪水"]=xinshui
        item["工作城市"]=gongzuodidian
        item["学历要求"]=job_qualifications_xueli
        item["经验要求"]=job_qualifications_jingyan
        item["语言要求"]=job_qualifications_yuyan
        item["年龄要求"]=job_qualifications_nianling
        item["职位描述"]=zhiwei_miaoshu
        item["公司介绍"]=company_jieshao
        item["公司规模"]=guimo
        item["工作地点"]=location
        item["注册资本"]=zhuceziben
        item["注册时间"]=zhuceshijian
        item["经营范围"]=jingyingfanwei
        yield item
      #       print(location)
#         print("是否有报错",xinshui,fankuishijian,gongzuodidian,job_qualifications_xueli,job_qualifications_jingyan,job_qualifications_yuyan,
#              job_qualifications_nianling,zhiwei_miaoshu,company_jieshao,guimo,location,zhuceziben,zhuceshijian,jingyingqixian,jingyingfanwei)