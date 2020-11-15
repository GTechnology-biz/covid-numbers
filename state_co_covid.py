import json
import requests
import datetime

date = datetime.datetime.now().strftime("%m/%d/%Y")


state_daily_cnty_inf = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Colorado_COVID19_Positive_Cases/FeatureServer/0/query?where=LABEL%20%3D%20%27ADAMS%27%20OR%20LABEL%20%3D%20%27DENVER%27%20OR%20LABEL%20%3D%20%27ARAPAHOE%27&outFields=*&outSR=4326&f=json"
state_daily_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_daily_state_statistics_cumulative/FeatureServer/0/query?where=Date%20%3D%20'11%2F12%2F2020'&outFields=*&outSR=4326&f=json"
state_exp_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/CDPHE_COVID19_StateLevel_Expanded_Case_Data_Summary/FeatureServer/0/query?where=date%20%3D%20%2711%2F11%2F2020%27&outFields=section,category,description,date,metric,value&outSR=4326&f=json"

url = "{state_daily_cnty_inf, state_daily_url, state_exp_url}"


for item in url():
    data = requests.get(item)
    data = data.json()

    print(json.dumps(data, indent=2))
