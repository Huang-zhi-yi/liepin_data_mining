# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
ulist=list()
class LiepinPipeline:
    def process_item(self, item, spider):
        df=pd.DataFrame(item["liepin_xueli"]).rename(columns={0:"学历"})
        df["经验"]=item["liepin_jingyan"]
        df["薪水"]=item["job_xinshui"]
        df["职称"]=item["job_zhicheng"]
        df["公司名称"]=item["job_company_name"]
        df["链接"]=item["job_url"]
        df["公司链接"]=item["job_company_url"]
        self.addition(df)
        #df.to_excel("liepin_job.xlsx")
#         df1=list()
#         df1.append(item["liepin_job"],ignore_index=True)
#         print(df1) 
        #print(type(item["liepin_job"]))
#         df_all=pd.concat(item["liepin_job"])
#        print(df_all)
#         for x in item["liepin_job"]:
            
#             df=pd.DataFrame(item["liepin_job"]
        
        #return df
    def addition(self,df):
        #print(df,"不知道是不是为空喔")
        ulist.append(df)
        #print(ulist) 
        df_合并=pd.concat(ulist)
        #print(df_合并)
        df_合并.to_excel("猎聘网数据分析相关岗位信息.xlsx")
#         return df_合并
        #ulist=list()
