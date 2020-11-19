import dash_table as dt
import dash_table_experiments 
import dash
import dash_html_components as html
import pandas as pd
import json
import requests
import datetime


app = dash.Dash(__name__)
date_now = datetime.datetime.now()
date = datetime.datetime.now().strftime("%m/%d/%Y")
date_1 = (date_now - datetime.timedelta(days=2)).strftime("%m/%d/%Y")
fet = "features"
att = "attributes"
new_index = pd.DataFrame( columns=['FULL_', 'GEOID', 'LABEL', 'STAETFP', 'COUNTY', 'COUNTYFP', 'County_Pos_Cases', 'County_Population', 'County_Rate_Per_100_000', 'County_Pos_Cases_Yesterday', 'County_Pos_Cases_Change', 'County_Deaths', 'County_Deaths_Yesterday', 'County_Deaths_Change', 'State_Pos_Cases', 'State_Population', 'State_Rate_Per_100000', 'State_Deaths', 'State_CDC_Deaths', 'State_Number_Hospitalizations', 'State_Number_Tested', 'State_Test_Encounters', 'State_Number_of_Counties_Pos', 'State_Number_of_Outbreaks', 'Data_Source', 'Date_Data_Last_Updated', 'Shape__Area', 'Shape__Length'], index=['16','32','62'])

state_daily_cnty_inf = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Colorado_COVID19_Positive_Cases/FeatureServer/0/query?where=LABEL%20%3D%20%27ADAMS%27%20OR%20LABEL%20%3D%20%27DENVER%27%20OR%20LABEL%20%3D%20%27ARAPAHOE%27&outFields=*&outSR=4326&f=json"
state_daily_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/colorado_covid19_daily_state_statistics_cumulative/FeatureServer/0/query?where=Date%20%3D%20'" + date_1 + "'&outFields=*&outSR=4326&f=json"
state_exp_url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/CDPHE_COVID19_StateLevel_Expanded_Case_Data_Summary/FeatureServer/0/query?where=date%20%3D%20%27" + date_1 + "%27&outFields=section,category,description,date,metric,value&outSR=4326&f=json"
u_1 = state_daily_cnty_inf
u_2 = state_daily_url
u_3 = state_exp_url

app = dash.Dash(__name__)

#url = state_daily_cnty_inf
url = [state_daily_cnty_inf, state_daily_url, state_exp_url]
table1 = {} 
table2 = {}
table3 = {}


def tbl_1 (data):
    data = data.set_index('OBJECTID').transpose().reset_index()
    
    return(data)

def tbl_2 (data):
    data = data.transpose().reset_index()   
    return(data)

def tbl_3 (data):
    #data = data.set_index('OBJECTID').transpose().reset_index()
    return(data)


def url2json(urll):

    r = requests.get(urll)
    data = r.json()

    if 'objectIdFieldName' in data:
        del data['objectIdFieldName']
    elif 'uniqueIdField' in data:
        del data['uniqueIdField']
    elif 'globalIdFieldName' in data:
        del data['globalIdFieldName']
    elif 'geometryProperties' in data:
        del data['geometryProperties']
    elif 'geometryType' in data:
        del data['geometryType']
    elif 'geometry' in data:
        del data['geometry']
    elif 'fields' in data:
        del data['fields']
    elif 'spatialReference' in data:
        del data['spatialReference']

    url_json = data
    
    return url_json

def data_prep(urll):
    nope = url2json(urll)
    df = pd.json_normalize(nope, fet , att , max_level=1 , errors = 'ignore')
    df.columns = df.columns.str.lstrip(att + ".")
    df = df.drop(columns=[
        'GEOID',
        'FULL_',
        'Desc_',
        'GEOID',
        'geometry',
        'geometry.rings',
        'STAETFP',
        'Shape__Length', 
        'Shape__Area', 
        'rings',
        'LABEL',
        'COUNTYFP',
        'Data_Source'
        ], errors = 'ignore')
    if urll == state_daily_cnty_inf:
        data = tbl_1(df)
    elif urll ==  state_daily_url:
        data = tbl_2(df)
    elif urll ==  state_exp_url:
        data = tbl_3(df)
    
    
#    data = df.T.rename_axis('Stat').reset_index()
    return data



def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe) , max_rows))
        ])
    ])

#table1 = data_prep(state_daily_cnty_inf)



for tbl in 1, 2, 3:
    if tbl == 1:
        table1 = data_prep(u_1)
    elif tbl == 2:
        table2 = data_prep(u_2)
    elif tbl == 3:
        table3 = data_prep(u_3)


    

#app.layout = html.Div(children=[
  
tt_1 = html.Div([
    html.Div(
        html.H1("Table 1")
    ),
    dt.DataTable(
        columns=[
        {"name": str(i), "id": str(i)} for i in table2.columns
        ],
        data=table2.to_dict('records') ,
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
            ],
        fixed_columns={'headers': True, 'data': 1},
        style_table={'maxWidth': '30%'},
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'width': 'auto'},
        id='table2'
        ),
    html.Div(
        html.Br()
    )
    ])


tt_2 = html.Div([    
    dt.DataTable(
        columns=[
        {"name": str(i), "id": str(i)} for i in table1.columns
        ],
        data=table1.to_dict('records') ,
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
            ],
        fixed_columns={'headers': True, 'data': 1},
        style_table={'maxWidth': '55%'},
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'width': 'auto'},
        id='table1'
        )
    ])

tt_3 = html.Div([
    dt.DataTable(
        columns=[
        {"name": str(i), "id": str(i)} for i in table3.columns
        ],
        data=table3.to_dict('records') ,
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
            ],
        fixed_columns={'headers': True, 'data': 1},
        style_table={'maxWidth': '80%'},
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'width': 'auto'},
        id='table3'
        )
    ])



#for i in url:
#    df = data_prep(i)
#
app.layout = html.Div(children=[tt_1, tt_2, tt_3])
    
    
    
#    id='table1',
#    columns=[
#        {"name": str(i), "id": str(i)} for i in table1.columns
#        ],
#    data=table1.to_dict('records') ,
#    style_cell={'textAlign': 'left'},
#    style_data_conditional=[
#        {
#            'if': {'row_index': 'odd'},
#            'backgroundColor': 'rgb(248, 248, 248)'}
#        ],
#    fixed_columns={'headers': True, 'data': 1},
#    style_table={'minWidth': '100%'},
#    style_data={
#       'whiteSpace': 'normal',
#       'height': 'auto'},

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
