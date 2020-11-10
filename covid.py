#!/usr/bin/python

import requests
import json
import datetime

date_now = datetime.datetime.now()
date_now_day = date_now.strftime("%d")
date_now_mth = date_now.strftime("%m")
date_now_yer = date_now.strftime("%Y")
date_1 = date_now - datetime.timedelta(days=1)
date_1_day = date_1.strftime("%d")
date_1_mth = date_1.strftime("%m")
date_1_yer = date_1.strftime("%Y")
date_14 = date_now - datetime.timedelta(days=14)
date_14_day = date_14.strftime("%d")
date_14_mth = date_14.strftime("%m")
date_14_yer = date_14.strftime("%Y")

key = "features"
att = "attributes"

county = ""
metric = ""
value = ""
rate = ""
date = ""


url_now = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_now_mth + "%2F" + date_now_day + "%2F" + date_now_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&outSR=4326&f=json"
url_1 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_1_mth + "%2F" + date_1_day + "%2F" + date_1_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&outSR=4326&f=json"
url_14 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_14_mth + "%2F" + date_14_day + "%2F" + date_14_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&outSR=4326&f=json"

data_now = requests.get(url_now)
jsn_now = data_now.json()
lst_now = jsn_now[key]

data_1 = requests.get(url_1)
jsn_1 = data_1.json()
lst_1 = jsn_1[key]

data_14 = requests.get(url_14)
jsn_14 = data_14.json()
lst_14 = jsn_14[key]


county = lst_now[0][att].get('COUNTY')
date = lst_now[0][att].get('Date')
print(County, date) 

now_value_cases = 
now_rate_cases_100k =
now_value_death =
now_rate_death_100k =
now_value_tests =

1_value_cases =
1_rate_cases_100k =
1_value_death =
1_rate_death_100k =
1_value_tests =

14_value_cases =
14_rate_cases_100k =
14_value_death =
14_rate_death_100k =
14_value_tests =

#def get_value(lst,indx,value):
#    blah = lst[indx][att]
#    reslt = blah.get(value)
    
if indx == 0:
    blah = lst[0][att]
    county = blah.get('COUNTY')
    date = blah.get('Date')
    now_value_cases = blah.get('Value')


for i in range(8):
    blah = lst[i][att]
    desc = blah.get('Desc_')
    print(i, desc)
    metric = blah.get('Metric')
    print(i, metric)
    county = blah.get('COUNTY')
    print(i, county)
    value = blah.get('Value')
    print(i, value)
    rate = blah.get('Rate')
    print(i,  rate)
    date = blah.get('Date')   
    print(i , date)





