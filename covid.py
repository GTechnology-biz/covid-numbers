#!/usr/bin/python

import requests
import json
import datetime

date_now = datetime.datetime.now()
date = str(date_now)
date_1 = date_now - datetime.timedelta(days=1)
date_14 = date_now - datetime.timedelta(days=14)

src_date = date_now.strftime("%m/%d/%Y")
src_date_1 = (date_now - datetime.timedelta(days=1)).strftime("%m/%d/%Y")
src_date_14 = (date_now - datetime.timedelta(days=14)).strftime("%m/%d/%Y")
#src_date = "11/11/2020"
#src_date_1 = "11/10/2020"
#src_date_14 = "10/27/2020"


key = "features"
att = "attributes"

county_A = "ADAMS"
county ="COUNTY"
metric = "Metric"
value = "Value"
rate = "Rate"
date_k = "Date"
desc = "Desc_"

ca_100 = "Case Rates Per 100,000 People in Colorado by County>Rate Per 100,000"
ca  = "Cases of COVID-19 in Colorado by County>Cases"
de_100 = "Deaths Among COVID-19 Cases Rates Per 100,000 People in Colorado by County>Rate Per 100,000"
de = "Deaths Among COVID-19 Cases in Colorado by County>Deaths"
tst_100 = "Total COVID-19 Testing Rate per 100,000 People in Colorado by County>Rate Per 100,000"
tst_pcr = "Total COVID-19 Tests Performed in Colorado by County>Percent of tests by PCR"
tst_ser = "Total COVID-19 Tests Performed in Colorado by County>Percent of tests by Serology"
tst = "Total COVID-19 Tests Performed in Colorado by County>Total Tests Performed"

url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_county_statistics_cumulative/FeatureServer/0/query?where=Date%20%3D'" + src_date + "'%20OR%20Date%20%3D%20'" + src_date_1 +"'%20OR%20Date%20%3D%20'" + src_date_14 + "'&outFields=*&outSR=4326&f=json"

src = requests.get(url)
data = src.json()

dic = dict()
dic_1 = dict()
dic_14 = dict()
dicl = dict()

for at in data[key]:
    countyl = at[att][county]
    datel = at[att][date_k]

    if countyl == 'ADAMS':
        if datel == src_date:
            dicl = dic
        elif datel == src_date_1:
            dicl = dic_1
        elif datel == src_date_14:
            dicl = dic_14

        descl = at[att][desc]
        valuel = at[att][value]
        ratel = at[att][rate]
        metricl = at[att][metric]
        full = descl + ">" + metricl

        if valuel == None:
            dicl[full] = ratel
        else:
            dicl[full] = valuel

dic = json.dumps(dic, sort_keys=True)
dic = json.loads(dic)
dic_1 =json.dumps(dic_1, sort_keys=True)
dic_1 = json.loads(dic_1)
dic_14 = json.dumps(dic_14, sort_keys=True)
dic_14 = json.loads(dic_14)

new_c_1 = dic[ca] - dic_1[ca]
new_c_14 = dic[ca] - dic_14[ca]

new_100_1 = dic[ca_100] - dic_1[ca_100]
new_100_14 = dic[ca_100] - dic_14[ca_100]

new_d_1 = dic[de] - dic_1[de]
new_d_14 = dic[de] - dic_14[de]
ntst = dic[tst] - dic_1[tst]
ntst_14 = dic[tst] - dic_14[tst]
pos = (new_c_1 / ntst) * 100
pos_14 = (new_c_14 / ntst_14) * 100

print(f"Description | Stat ")
print(f"-----|-----")
print(f"Today Pos test percent | {round(pos,2)}%   ")
print(f"14 day Pos test percent | {round(pos_14,2)}%   ")
print(f"--------|--------")
print(f"New Cases Since yesterday | {new_c_1} ")
print(f"New Cases Since 14 days ago | {new_c_14} ")
print(f"--------|--------")
print(f"Cases per 100k today | {round(dic[ca_100])} ")
print(f"Diff in cases per 100k since yesterday | {round(new_100_1)} ")
print(f"Diff since 14 days ago | {round(new_100_14)} ")
print(f"--------|--------")
print(f"New Death since yesterday | {new_d_1} ")
print(f"New Death since 14 days ago | {new_d_14} ")
print(f"\n---\n---\n---")

for i in dic, dic_1, dic_14:
    if i == dic:
        time_h = src_date
    elif i == dic_1:
        time_h = src_date_1
    elif i == dic_14:
        time_h = src_date_14
    print(f"# **Covids stats: {time_h}**\n")
    print(f"**Stat** | **Value** ")
    print(f"-----|------ ")
    for x,y in i.items():
        print(f"{x} | {y} ")
    print(f"\n-----------------------------\n")


