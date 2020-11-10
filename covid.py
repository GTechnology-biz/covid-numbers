#!/usr/bin/python

import requests
import json
import datetime

date = datetime.datetime.now()
#date_now = date
date_now = date - datetime.timedelta(days=1)
date_now_day = date_now.strftime("%d")
date_now_mth = date_now.strftime("%m")
date_now_yer = date_now.strftime("%Y")
#date_1 = date_now - datetime.timedelta(days=1)
date_1 = date_now - datetime.timedelta(days=2)
date_1_day = date_1.strftime("%d")
date_1_mth = date_1.strftime("%m")
date_1_yer = date_1.strftime("%Y")
#date_1 = date_now - datetime.timedelta(days=14)
date_14 = date_now - datetime.timedelta(days=15)
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


url_now = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_now_mth + "%2F" + date_now_day + "%2F" + date_now_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"
url_1 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_1_mth + "%2F" + date_1_day + "%2F" + date_1_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"
url_14 = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=COUNTY%20%3D%20%27ADAMS%27%20AND%20Date%20%3D%20%27" + date_14_mth + "%2F" + date_14_day + "%2F" + date_14_yer + "%27&outFields=COUNTY,Desc_,Metric,Value,Rate,Date&f=json"


data_now = requests.get(url_now)
jsn_now = data_now.json()
lst_now = jsn_now[key]
#print(jsn_now)
data_1 = requests.get(url_1)
jsn_1 = data_1.json()
lst_1 = jsn_1[key]

data_14 = requests.get(url_14)
jsn_14 = data_14.json()
lst_14 = jsn_14[key]


blah = lst_now[0][att]
blah1 = lst_now[1][att]
blah2 = lst_now[2][att]
blah3 = lst_now[3][att]
blah4 = lst_now[4][att]

county = blah.get('COUNTY')
date = blah.get('Date')

now_value_cases = blah.get('Value')
now_rate_cases_100k = blah1.get('Rate')
now_value_death = blah2.get('Value')
now_rate_death_100k = blah3.get('Rate')
now_value_tests =  blah4.get('Value')

blah = lst_1[0][att]
blah1 = lst_1[1][att]
blah2 = lst_1[2][att]
blah3 = lst_1[3][att]
blah4 = lst_1[4][att]

b1_value_cases = blah.get('Value')
b1_rate_cases_100k = blah1.get('Rate')
b1_value_death = blah2.get('Value')
b1_rate_death_100k = blah3.get('Rate')
b1_value_tests = blah4.get('Value')

blah = lst_14[0][att]
blah1 = lst_14[1][att]
blah2 = lst_14[2][att]
blah3 = lst_14[3][att]
blah4 = lst_14[4][att]

b14_value_cases = blah.get('Value')
b14_rate_cases_100k = blah1.get('Rate')
b14_value_death = blah2.get('Value')
b14_rate_death_100k = blah3.get('Rate')
b14_value_tests = blah4.get('Value')

new_case_1 = round(now_value_cases - b1_value_cases,2)
new_case_14 = round(now_value_cases - b14_value_cases,2)

case_100k_14 = round(now_rate_cases_100k - b14_rate_cases_100k,2)

new_death_1 = round(now_value_death - b1_value_death,2)
new_death_14 = round(now_value_death - b14_value_death,2)

death_100k_14 = round(now_rate_death_100k - b14_rate_death_100k,2)

new_test_1 = round(now_value_tests - b1_value_tests,2)
new_test_14 = round(now_value_tests - b14_value_tests,2)

test_pos = round(new_case_1 / new_test_1 * 100,2)
test_pos_14 = round(new_case_14 / new_test_14 * 100,2)

sp = " "

print(f"\t\t# Adams County Covid Stats {date_now.strftime('%d-%m')}")
print(f"\tStat | Current Total | vs. Previous Day | vs. 14 Days Previous")
print(f"\tPositive Cases | {now_value_cases} | +{new_case_1}:{b1_value_cases} | +{new_case_14}:{b14_value_cases}")
print(f"\tTests Perfomed | {now_value_tests} | +{new_test_1}:{b1_value_tests} | +{new_test_14}:{b14_value_tests}")
print(f"\t% Pos. vs. Tests | %{test_pos} | | %{test_pos_14}")
print(f"\tPos. Cases per 100k | {now_rate_cases_100k} | | +{case_100k_14}:{b14_rate_cases_100k}")
print(f"\tDeaths Among Cases | {now_value_death} | +{new_death_1}:{b1_value_death} | +{new_death_14}:{b14_value_death}")
print(f"\tDeaths Among Cases per 100k | {now_rate_death_100k} | | +{death_100k_14}:{b14_rate_death_100k}")


#print('Cases for ' , date_now.strftime("%d-%m") , now_value_cases, '\n addtional from previous > Day: ', now_value_cases - b1_value_cases, ' > 14 days:',   now_value_cases - b14_value_cases)
#print("Day Before  " , date_1 , "/n " , b1_value_cases)
#print("2 weeks ago  " , date_14 , "/n "  , b14_value_cases)
#def get_value(lst,indx,value):
#    blah = lst[indx][att]
#    reslt = blah.get(value)
    
#if indx == 0:
#    blah = lst[0][att]
#    county = blah.get('COUNTY')
#    date = blah.get('Date')
#    now_value_cases = blah.get('Value')


#for i in range(8):
 #   blah = lst[i][att]
   # desc = blah.get('Desc_')
#    print(i, desc)
    #metric = blah.get('Metric')
  #  print(i, metric)
   # county = blah.get('COUNTY')
    #print(i, county)
 #   value = blah.get('Value')
   # print(i, value)
  #  rate = blah.get('Rate')
  # a print(i,  rate)
 #   date = blah.get('Date')   
   # print(i , date)





