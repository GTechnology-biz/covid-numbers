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

#print("day +0")
dic = json.dumps(dic, sort_keys=True)
dic = json.loads(dic)
#print("day -1")
dic_1 =json.dumps(dic_1, sort_keys=True)
dic_1 = json.loads(dic_1)
#print("day -14")
dic_14 = json.dumps(dic_14, indent=4, sort_keys=True)
dic_14 = json.loads(dic_14)





print(f"# Covids stats: {src_date}\n")
print(f"Stat | Value \n")
print(f"-----|------ \n")
for x,y in dic.items():
    print(f"{x} | {y} \n")
print(f"\n-----------------------------\n")


print(f"# Covids stats: {src_date_1}\n")
print(f"Stat | Value \n")
print(f"-----|------ \n")
for x,y in dic_1.items():
    print(f"{x} | {y} \n")
print(f"\n-----------------------------\n")


print(f"# Covids stats: {src_date_14}\n")
print(f"Stat | Value \n")
print(f"-----|------ \n")
for x,y in dic_14.items():
    print(f"{x} | {y} \n")
#print(dic[ca])
print(f"\n-----------------------------\n")
