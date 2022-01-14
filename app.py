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
        Input('select_all_level_1', 'n_clicks'),
        Input('release_all_level_1', 'n_clicks'),
        Input('checklist_level_2', 'value'),
        Input('select_all_level_2', 'n_clicks'),
        Input('release_all_level_2', 'n_clicks'),
        Input('checklist_level_3', 'value'),
        Input('select_all_level_3', 'n_clicks'),
        Input('release_all_level_3', 'n_clicks'),
        Input('checklist_level_4', 'value'),
        Input('select_all_level_4', 'n_clicks'),
        Input('release_all_level_4', 'n_clicks'),
        Input('checklist_level_5', 'value'),
        Input('select_all_level_5', 'n_clicks'),
        Input('release_all_level_5', 'n_clicks'),
        Input('checklist_level_upper', 'value'),
        Input('select_all_level_upper', 'n_clicks'),
        Input('release_all_level_upper', 'n_clicks'),
    ],
)
def meeting_plan_fact(
        checklist_level_1,
        select_all_level_1,
        release_all_level_1,
        checklist_level_2,
        select_all_level_2,
        release_all_level_2,
        checklist_level_3,
        select_all_level_3,
        release_all_level_3,
        checklist_level_4,
        select_all_level_4,
        release_all_level_4,
        checklist_level_5,
        select_all_level_5,
        release_all_level_5,
        checklist_level_upper,
        select_all_level_upper,
        release_all_level_upper
):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]


    # читаем файл с дефолтными фильтрами
    # Opening JSON file
    with open('saved_filters.json', 'r') as openfile:
      # Reading from json file
      saved_filters_dict = json.load(openfile)


    

    if len(saved_filters_dict['level_2'])>0:
      checklist_level_2_values = saved_filters_dict['level_2']
    else:
      checklist_level_2_values =[]

    # по умолчанию result_df - это полный список всех техмест
    result_df = teh_mesta_full_list
    

    if len(saved_filters_dict['level_1'])>0: # сначала смотрим в json. Если там что-то есть, то применяем
        checklist_level_1_values = saved_filters_dict['level_1']
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1_values)]
    else: # Если там ничего нет, то  изменения в result_df не вносим
      checklist_level_1_values =[] # если в json нет пусто, то изменения в result_df не вносим
    

    if checklist_level_1 and len(checklist_level_1)>0: # если селект с фильтром существует и там что-то есть,, то применяем
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1)]
        checklist_level_1_values = checklist_level_1
        # Сохраняем новые значения в json
        saved_filters_dict['level_1'] = checklist_level_1
        with open("saved_filters.json", "w") as jsonFile:
          json.dump(saved_filters_dict, jsonFile)    
    else: # если селект не существует или его длина равна нулю
      # если в json есть данные по этому уровню, то применяем. Есди их там нет, тоо с result_df ничего не произойдет
      if len(saved_filters_dict['level_1'])>0: 
        checklist_level_1_values = saved_filters_dict['level_1']
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1_values)]

    
    if checklist_level_1 == None: # если в селекте ничего не выбрали, то берем значение из json
      if len(saved_filters_dict['level_1'])>0: 
        checklist_level_1_values = saved_filters_dict['level_1']
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1_values)]
      else:
        checklist_level_1_values =[] # если в json нет пусто, то изменения в result_df не вносим
    # если в чек-боксах что-то есть, то берем значение из чек-бокса и перезаписываем файл json значениями из чек-боксов
    elif len(checklist_level_1)>0:
      checklist_level_1_values = checklist_level_1
      result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1_values)]
    elif len(checklist_level_1)==0: # если селект жив, но равен нулю, то есть все убрали. Нужно вернуть данные по этому фильтру как будто выбрано все


      # Data to be written
      saved_filters_dict['level_1'] = checklist_level_1
      with open("saved_filters.json", "w") as jsonFile:
        json.dump(saved_filters_dict, jsonFile)    


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
    # на начальном экране фильтра пустые
    checklist_level_3_values = []


    # Список чек-боксов Level_4
    level_4_df = selected_items_df.loc[selected_items_df['level_no'] == 4]
    checklist_level_4_options = []
    if len(level_4_df) > 0:
        checklist_level_4_options = functions.level_checklist_data(level_4_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_4_values = []


    # Список чек-боксов Level_5
    level_5_df = selected_items_df.loc[selected_items_df['level_no'] == 5]
    checklist_level_5_options = []
    if len(level_5_df) > 0:
        checklist_level_5_options = functions.level_checklist_data(level_5_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_5_values = []

    # Список чек-боксов Level_upper
    level_upper_df = selected_items_df.loc[selected_items_df['level_no'] == 0]
    checklist_level_upper_options = []
    if len(level_upper_df) > 0:
        checklist_level_upper_options = functions.level_checklist_data(level_upper_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_upper_values = []


    #  теперь надо проверять. Если список чек-боксов не None и его длина не равна нулю, то
    # то надо включать фильтр по выбранному чек-боксу. В таблицу
  
    if checklist_level_1 and len(checklist_level_1)>0:
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1)]
        checklist_level_1_values = checklist_level_1
        

    if checklist_level_2 and len(checklist_level_2)>0:
        result_df = result_df.loc[result_df['level_2'].isin(checklist_level_2)]
        checklist_level_2_values = checklist_level_2

    if checklist_level_3 and len(checklist_level_3)>0:
        result_df = result_df.loc[result_df['level_3'].isin(checklist_level_3)]
        checklist_level_3_values = checklist_level_3

    if checklist_level_4 and len(checklist_level_4)>0:
        result_df = result_df.loc[result_df['level_4'].isin(checklist_level_4)]
        checklist_level_4_values = checklist_level_4

    if checklist_level_5 and len(checklist_level_5)>0:
        result_df = result_df.loc[result_df['level_5'].isin(checklist_level_5)]
        checklist_level_5_values = checklist_level_5

    if checklist_level_upper and len(checklist_level_upper)>0:
        result_df = result_df.loc[result_df['level_upper'].isin(checklist_level_upper)]
        checklist_level_upper_values = checklist_level_upper

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
