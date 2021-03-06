import json
import plotly  as go
import plotly.express as px
import pandas as pd


import requests
import datetime

date = datetime.datetime.now().strftime("%m/%d/%Y")
fet = "features"
att = "attributes"

state_daily_cnty_inf = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Colorado_COVID19_Positive_Cases/FeatureServer/0/query?where=LABEL%20%3D%20%27ADAMS%27%20OR%20LABEL%20%3D%20%27DENVER%27%20OR%20LABEL%20%3D%20%27ARAPAHOE%27&outFields=*&outSR=4326&f=json"
state_daily_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_daily_state_statistics_cumulative/FeatureServer/0/query?where=Date%20%3D%20'11%2F12%2F2020'&outFields=*&outSR=4326&f=json"
state_exp_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/CDPHE_COVID19_StateLevel_Expanded_Case_Data_Summary/FeatureServer/0/query?where=date%20%3D%20%2711%2F11%2F2020%27&outFields=section,category,description,date,metric,value&outSR=4326&f=json"

url = [state_daily_cnty_inf, state_daily_url, state_exp_url]


for i in url:
    urll = i
    data = requests.get(urll)
    data = data.json()
    i = data
    for w in data[fet]:
        blah = w[att]
#        print(json.dumps(blah, indent=2))


#df = px.data()
#fig = px.treemap(
#        state_exp_url,
#        path = [fet, att, 'Label'],
#        values = 'rate')

#fig.show()

print(len(fet), len(att), len())
