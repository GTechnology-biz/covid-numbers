#!/usr/bin/python

import requests
import json
import datetime

date_now = datetime.datetime.now()
date = str(date_now)
#date_now = date - datetime.timedelta(days=0)
date_now_day = date_now.strftime("%d")
date_now_mth = date_now.strftime("%m")
date_now_yer = date_now.strftime("%Y")
date_1 = date_now - datetime.timedelta(days=1)
#date_1 = date_now - datetime.timedelta(days=2)
date_1_day = date_1.strftime("%d")
date_1_mth = date_1.strftime("%m")
date_1_yer = date_1.strftime("%Y")
date_14 = date_now - datetime.timedelta(days=14)
#date_14 = date_now - datetime.timedelta(days=15)
date_14_day = date_14.strftime("%d")
date_14_mth = date_14.strftime("%m")
date_14_yer = date_14.strftime("%Y")

src_date = date_now.strftime("'%m/%d/%Y'") 
print(src_date)
key = "features"
att = "attributes"

county = ""
metric = "Metric"
value = "Value"
rate = "Rate"
date = "Date"
desc = "Desc_"

#url_now = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY='ADAMS'%20AND%20Date='" + date_now_mth + "%2F" + date_now_day + "%2F" + date_now_yer + "'&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"
#url_1 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_1_mth + "%2F" + date_1_day + "%2F" + date_1_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"
#url_14 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_14_mth + "%2F" + date_14_day + "%2F" + date_14_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"

url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20'ADAMS'%20AND%20Date%20%3D%20" + src_date + "&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"
#utl_now = url
print(url)  
src = requests.get(url)
data = src.json()
print(data)
dic = dict()

for at in data[key]:
    desc = at[att][desc]
    value = at[att][value]
    rate = at[att][rate]
    metric = at[att][metric]
    desc = desc + ":" + metric
    if value == None:
        dic[desc] = rate
    else:
        dic[desc] = value


for x in dic:
    print(x,"::", dic[x])

