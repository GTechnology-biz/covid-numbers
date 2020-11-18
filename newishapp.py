import dash_table
import dash
import dash_html_components as html
import pandas as pd
import json
import requests
import datetime
import jq

date = datetime.datetime.now().strftime("%m/%d/%Y")
fet = "features"
att = "attributes"

state_daily_cnty_inf = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Colorado_COVID19_Positive_Cases/FeatureServer/0/query?where=LABEL%20%3D%20%27ADAMS%27%20OR%20LABEL%20%3D%20%27DENVER%27%20OR%20LABEL%20%3D%20%27ARAPAHOE%27&outFields=*&outSR=4326&f=json"
state_daily_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_daily_state_statistics_cumulative/FeatureServer/0/query?where=Date%20%3D%20'" + date + "'&outFields=*&outSR=4326&f=json"
state_exp_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/CDPHE_COVID19_StateLevel_Expanded_Case_Data_Summary/FeatureServer/0/query?where=date%20%3D%20%27" + date + "%27&outFields=section,category,description,date,metric,value&outSR=4326&f=json"


app = dash.Dash(__name__)

url = state_daily_cnty_inf
#url = (state_daily_cnty_inf, state_daily_url, state_exp_url)
nope = ""

def url2json(urll):

    r = requests.get(urll)
    data = r.json()
    url_json = data
    return url_json

def data_prep(urll):

    nope = url2json(urll)
    df = pd.json_normalize(nope, 'features')
    df =df.drop(columns=[
        'attributes.GEOID', 
        'attributes.Shape__Length', 
        'attributes.Shape__Area', 
        'geometry.rings',
        'attributes.Data_Source'
        ], errors = 'ignore')
    df = df.T.rename_axis('Stat').reset_index()
    return df



def generate_table(dataframe, max_rows=100):
#    for i in url:
#        data_prep(url)
        
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

state_daily_cnty_inf = data_prep(state_daily_cnty_inf)




app.layout = html.Div(children=[
    html.H4(children=state_daily_cnty_inf),
    generate_table(state_daily_cnty_inf)
    ])

#for i in url:
#    df = data_prep(i)
#
#    app.layout = dash_table.DataTable(
#         id='table',
#         columns=[
#             {"name": str(i), "id": str(i)} for i in df.columns
#             ],
#         data=df.to_dict('records') ,
#         style_cell={'textAlign': 'left'},
#         style_data_conditional=[
#             {
#                 'if': {'row_index': 'odd'},
#                 'backgroundColor': 'rgb(248, 248, 248)'}
#             ],
#         fixed_columns={'headers': True, 'data': 1},
#         style_table={'minWidth': '100%'},
#    
#         style_data={
#            'whiteSpace': 'normal',
#            'height': 'auto'},
#    
#    
#         )
#
#
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
