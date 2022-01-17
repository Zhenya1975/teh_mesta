import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_templates import load_figure_template

import functions
import select_filters_tab
import settings_tab
from dash import dash_table
import base64
import io
import json
# import plotly.graph_objects as go
import result_df_prep


# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
# template_theme1 = "sketchy"
template_theme1 = "flatly"
template_theme2 = "darkly"
# url_theme1 = dbc.themes.SKETCHY
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

teh_mesta_full_list = pd.read_csv('data/origin_codes_df.csv', dtype=str)
teh_mesta_full_list.fillna('no_data', inplace=True)
loading_style = {
    # 'position': 'absolute',
                 # 'align-self': 'center'
                 }

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[url_theme1, dbc_css])

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H4("ТЕХНИЧЕСКИЕ МЕСТА"),
                    ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2], ),

                    html.Div([
                        dcc.Tabs(
                            id="tabs-all",
                            style={
                                # 'width': '50%',
                                # 'font-size': '200%',
                                # 'height':'5vh'
                            },
                            value='tab_select_parameters',
                            # parent_className='custom-tabs',
                            # className='custom-tabs-container',
                            children=[
                                select_filters_tab.select_filters_tab(),
                                settings_tab.settings_tab()

                                # tab2(),
                                # tab3(),
                            ]
                        ),
                    ]),

                ]
            )
        ]
    ),
    className="m-4 dbc",
    fluid=True,
)


@app.callback([
    Output("checklist_level_1", "value"),
    Output("checklist_level_1", "options"),
    Output("checklist_level_2", "value"),
    Output("checklist_level_2", "options"),
    Output("checklist_level_3", "value"),
    Output("checklist_level_3", "options"),
    Output("checklist_level_4", "value"),
    Output("checklist_level_4", "options"),
    Output("checklist_level_5", "value"),
    Output("checklist_level_5", "options"),
    Output("checklist_level_upper", "value"),
    Output("checklist_level_upper", "options"),
    Output('code_table', 'children'),
    Output('number_of_rows_text', 'children'),
    Output('loading', 'parent_style')

],

    [
        Input('checklist_level_1', 'value'),
        Input('checklist_level_2', 'value'),
        Input('checklist_level_3', 'value'),
        Input('checklist_level_4', 'value'),
        Input('checklist_level_5', 'value'),
        Input('checklist_level_upper', 'value'),
    ],
)
def meeting_plan_fact(
        checklist_level_1,
        checklist_level_2,
        checklist_level_3,
        checklist_level_4,
        checklist_level_5,
        checklist_level_upper,
):
    # changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    

    # читаем файл с дефолтными фильтрами
    # Opening JSON file
    with open('saved_filters.json', 'r') as openfile:
      # Reading from json file
      saved_filters_dict = json.load(openfile)

    ################## level_1 VALUES ###################################
    if checklist_level_1 == None:
      filter_level_1 = saved_filters_dict['level_1']
    else:
      filter_level_1 = checklist_level_1
      saved_filters_dict['level_1'] = checklist_level_1
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_1_values = filter_level_1
    ################## level_2 VALUES ###################################
    if checklist_level_2 == None:
      filter_level_2 = saved_filters_dict['level_2']
    else:
      filter_level_2 = checklist_level_2
      saved_filters_dict['level_2'] = checklist_level_2
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_2_values = filter_level_2

    ################## level_3 VALUES ###################################
    if checklist_level_3 == None:
      filter_level_3 = saved_filters_dict['level_3']
    else:
      filter_level_3 = checklist_level_3
      saved_filters_dict['level_3'] = checklist_level_3
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_3_values = filter_level_3

    ################## level_4 VALUES ###################################
    if checklist_level_4 == None:
      filter_level_4 = saved_filters_dict['level_4']
    else:
      filter_level_4 = checklist_level_4
      saved_filters_dict['level_4'] = checklist_level_4
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_4_values = filter_level_4

    ################## level_5 VALUES ###################################
    if checklist_level_5 == None:
      filter_level_5 = saved_filters_dict['level_5']
    else:
      filter_level_5 = checklist_level_5
      saved_filters_dict['level_5'] = checklist_level_5
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_5_values = filter_level_5
    
    
    ################## level_upper VALUES ###################################
    if checklist_level_upper == None:
      filter_level_upper = saved_filters_dict['level_upper']
    else:
      filter_level_upper = checklist_level_upper
      saved_filters_dict['level_upper'] = checklist_level_upper
      # print('saved_filters_dict', saved_filters_dict)
      # записываем в json
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)
    checklist_level_upper_values = filter_level_upper

    
    print('filter_level_1: ', filter_level_1, 'filter_level_2: ', filter_level_2, 'filter_level_3: ', filter_level_3, 'filter_level_4: ', filter_level_4, 'filter_level_5: ', filter_level_5, 'filter_level_upper: ', filter_level_upper)
    result_df = result_df_prep.initial_result_df_prep(filter_level_1, filter_level_2, filter_level_3, filter_level_4, filter_level_5, filter_level_upper)
    print('initial_result_df_len = ', len(result_df))
   
    



    # фильтра должны быть пустыми. Принцип такой. Пустой фильтр - это не примененный фильтр. То есть
    # отдаются все данные, которые есть без фильтрации.
    selected_items_df = pd.read_csv('data/selected_items.csv', dtype=str)
    selected_items_df = selected_items_df.astype({"level_no": int})


    level_1_df = selected_items_df.loc[selected_items_df['level_no'] == 1]
    checklist_level_1_options = []
    if len(level_1_df)>0:
        checklist_level_1_options = functions.level_checklist_data(level_1_df)[0]

    # Список чек-боксов Level_2
    level_2_df = selected_items_df.loc[selected_items_df['level_no'] == 2]
    checklist_level_2_options = []
    if len(level_2_df) > 0:
        checklist_level_2_options = functions.level_checklist_data(level_2_df)[0]
    


    # Список чек-боксов Level_3
    level_3_df = selected_items_df.loc[selected_items_df['level_no'] == 3]
    checklist_level_3_options = []
    if len(level_3_df) > 0:
        checklist_level_3_options = functions.level_checklist_data(level_3_df)[0]



    # Список чек-боксов Level_4
    level_4_df = selected_items_df.loc[selected_items_df['level_no'] == 4]
    checklist_level_4_options = []
    if len(level_4_df) > 0:
        checklist_level_4_options = functions.level_checklist_data(level_4_df)[0]


    # Список чек-боксов Level_5
    level_5_df = selected_items_df.loc[selected_items_df['level_no'] == 5]
    checklist_level_5_options = []
    if len(level_5_df) > 0:
        checklist_level_5_options = functions.level_checklist_data(level_5_df)[0]


    # Список чек-боксов Level_upper
    level_upper_df = selected_items_df.loc[selected_items_df['level_no'] == 0]
    checklist_level_upper_options = []
    if len(level_upper_df) > 0:
        checklist_level_upper_options = functions.level_checklist_data(level_upper_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_upper_values = []


     

    result_df.to_csv('data/result_df.csv')


    table_list = []

    for index,row in result_df.iterrows():
        temp_dict = {}
        teh_mesto_code = row['Техническое место']

        temp_dict['Код технического места'] = teh_mesto_code
        temp_dict['Наименование технического места'] = row['Название технического места']
        temp_dict['level_upper'] = row['level_upper']

        table_list.append(temp_dict)
    table_df = pd.DataFrame(table_list)
    number_of_rows = len(table_df)
    number_of_rows_text = 'Количество записей: {}'.format(number_of_rows)
    # print(table_df)

    code_table = dash_table.DataTable(
        # id='table',
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict('records'),
        filter_action='native',
        style_header={
            # 'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
        },
        style_cell={'textAlign': 'left'},
    )
    new_loading_style = loading_style
    return checklist_level_1_values, checklist_level_1_options,checklist_level_2_values, checklist_level_2_options, checklist_level_3_values, checklist_level_3_options, checklist_level_4_values, checklist_level_4_options, checklist_level_5_values, checklist_level_5_options, checklist_level_upper_values, checklist_level_upper_options, code_table, number_of_rows_text, new_loading_style

@app.callback(
    Output("download-excel", "data"),
    Input("btn-download", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if n_clicks:
        df = pd.read_csv('data/result_df.csv', dtype=str)
        df = df.loc[:, ['Техническое место', 'Название технического места',	'Вышестоящее ТехМесто']]
        return dcc.send_data_frame(df.to_excel, "тех_места.xlsx", index=False, sheet_name="тех_места")


########## Настройки################
@app.callback(
    Output("download_template", "data"),
    Input("btn_download_template", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    if n_clicks:
        df = pd.read_csv('data/selected_items.csv', dtype=str)
        df = df.astype({'level_no': int})
        return dcc.send_data_frame(df.to_excel, "шаблон фильтров.xlsx", index=False, sheet_name="шаблон фильтров")


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv('data/selected_items.csv', dtype=str)
    df = df.astype({'level_no': int})
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xlsx' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            df.to_csv('data/selected_items.csv')
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),


        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            filter_action='native',
            style_header={
                # 'backgroundColor': 'white',
                'fontWeight': 'bold'
            },
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            style_cell={'textAlign': 'left'},

        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              )
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        
        return children

if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', debug=False)
