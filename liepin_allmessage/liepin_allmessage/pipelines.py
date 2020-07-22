# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ulist=list()
import pandas as pd
class LiepinAllmessagePipeline:
    def process_item(self, item, spider):
        #c=[a for a in item.values() ]
        c=[item]
        df=pd.DataFrame(c)
        self.addition(df)
        #df=pd.DataFrame(columns={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"})
        #mdd=pd.DataFrame(pd.pivot_table(c))
        #df = df.append(columns=c, ignore_index=True)
        #df.to_excel("liepin.xlsx")
        #df=pd.DataFrame(item["zhiwei"])
#         df=pd.DataFrame((item["company_jieshao"].strip()))
#         df["xinshui"]=item["xinshui"].strip()
        #return df
#         self.addition(df)
        
    def addition(self,df):
        #print(df,"不知道是不是为空喔")
        ulist.append(df)
#         #print(ulist) 
        df_合并=pd.concat(ulist)
#         #print(df_合并)
        df_合并.to_excel("猎聘教育相关岗位详情页.xlsx")
