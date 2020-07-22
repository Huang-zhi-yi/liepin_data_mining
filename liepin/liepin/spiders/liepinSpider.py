# -*- coding: utf-8 -*-
import scrapy
from liepin.items import LiepinItem
from urllib.parse import urlparse, parse_qs
import pandas as pd 
from requests_html import HTMLSession
import requests
url="https://www.liepin.com/zhaopin/?industries=&subIndustry=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&searchType=1&isAnalysis=&sortFlag=15&d_headId=467ad319171ce6c969b1f414e1664e45&d_ckId=467ad319171ce6c969b1f414e1664e45&d_sfrom=search_fp_nvbar&d_curPage=0&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EfA9rXquZc5IkJpXC-Ycixw&key=%E6%95%99%E8%82%B2"
from urllib.parse import urlparse, parse_qs,urlencode
import pandas as pd
def parse_url_qs_for_curPage (url):
    six_parts = urlparse(url) #把url拆成6部分
    out = parse_qs(six_parts.query)#取出query值并输出为字典out
    return (out)
参数模板=parse_url_qs_for_curPage(url)
参数模板
#下面这个函数要改，上面的url要改
def 参数修改(key,curPage):
    参数=参数模板.copy()
    参数["key"]=key
    参数["curPage"]=curPage
    return 参数
#关键词换
参数修改后列表=[参数修改(curPage=[i],key=["教育"]) for i in range(10)]
参数修改后列表
starts_url=list()
for a in 参数修改后列表:
    querys = urlencode(a, doseq = True) # doseq = True
    #print(querys)
    #six_new = six._replace(query=q)
    url="https://www.liepin.com/zhaopin/?"+querys
    starts_url.append(url)
starts_url

class LiepinspiderSpider(scrapy.Spider):
    name = 'liepinSpider'
    allowed_domains = ['www.liepin.com']
    start_urls =starts_url
    def parse(self, response): 
        r=response.xpath('//ul[@class="sojob-list"]/li')
        for a in r:
            job_xueli =a.xpath('//div[contains(@class,"job-info")]/p/span[@class="edu"]/text()').extract()
            job_jingyan=a.xpath('//div[contains(@class,"job-info")]/p/span[@class="edu"]/following-sibling::span/text()').extract()
            job_xinshui=a.xpath('//div[contains(@class,"job-info")]/p/span[@class="text-warning"]/text()').extract()
            job_shijian=a.xpath('//div[contains(@class,"job-info")]/p/time/@title/text()').extract()
            job_zhicheng=[x.strip()for x in (a.xpath('//div[contains(@class,"job-info")]/h3/a/text()')).extract() ]
            job_company_name=a.xpath('//div[contains(@class,"sojob-item-main")]//p[@class="company-name"]/a/text()').extract()
            job_url=a.xpath('//div[contains(@class,"job-info")]/h3/a/@href').extract()
            job_company_url=a.xpath('//div[contains(@class,"sojob-item-main")]//p[@class="company-name"]/a/@href').extract()   
        
        
        item=LiepinItem()
        item["liepin_jingyan"]=job_jingyan
        item["liepin_xueli"]=job_xueli
        item["job_xinshui"]=job_xinshui
        item["job_zhicheng"]=job_zhicheng
        item["job_company_name"]=job_company_name
        item["job_url"]=job_url
        item["job_company_url"]=job_company_url
        yield item
#         for v in item["job_url"]:
#             yield scrapy.Request(url=v,callback=self.parse_detail)
        
#     def parse_detail(self,response):
#         #接收前两层数据
#         #item = response.meta['item_2']
#         res = requests.get(response.url) 
#         print(res)
        #print(item)
        #return item
        #             job_zhicheng=["".join([x.strip() if type(x) is str else x.text.strip() for x in #a.xpath('//div[contains(@class,"job-info")]/h3/a/text()').extract()
#                  ])
#               ]
        
        #a=pd.DataFrame([x for x in (response.xpath('//div[contains(@class,"job-info")]/p/span[@class="edu"]/text()').extract())])
        #print(item["liepin_job"])
        #item["liepin_job"]=job_xueli
        
        
        #print(a)#list_df.append(c)
#         for x in a["0"]:
#             print(x)
#         ulist=list()
#         ulist.append(a)
#         print(ulist)
        
#         for a in c:
#             list_df.append(a)
        
        #print(list_df)
        
#         df_all = pd.concat(list_df).reset_index()
#         df_all.index.name = '序'
        #r=response.xpath('//ul[@class="sojob-list"]/li')
        #print(response)
        #session=HTMLSession()
        #list_url=list()
        #list_url.append(response)
        #for a in response.xpath('//ul[@class="sojob-list"]/li'):
             #print(a)
            #xpath不能被遍历
             #c=a.xpath('//div[contains(@class,"job-info")]/p/span[@class="edu"]/text()').extract()
             #print(c)   #print(e)
        
            #暂存结果 = [e.xpath(_xpath_)[0].lxml.text_content() for e in a]
            #print(暂存结果)
#             ulist=(requests_liepin(a))
#             display(ulist)
#             r = session.get(a)
#             # 先取特定元素, 精准打击其子后辈
#             主要元素 = r.html.xpath('//ul[@class="sojob-list"]/li')
#             return 主要元素
    #          ulist=list(requests_liepin(response))
#          display(ulist)
#         #list_df.append(df)
#         df_all = pd.concat(ulist).reset_index()
#         df_all.index.name = '序'
        
         #print(response)
#         list_df=list()
#         session=HTMLSession()
#         data=requests_liepin_scrapy(url)
#         data
#         list_df.append(data)

#         df_all = pd.concat(list_df).reset_index()
#         df_all.index.name = '序号'
#         df_all
