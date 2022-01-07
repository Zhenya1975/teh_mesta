import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_templates import load_figure_template

import functions
import select_filters_tab
from dash import dash_table
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
    Output('code_table', 'children'),
    Output('number_of_rows_text', 'children'),

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
        release_all_level_3
):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    # по умолчанию result_df - это полный список всех техмест
    result_df = teh_mesta_full_list
    # фильтра должны быть пустыми. Принцип такой. Пустой фильтр - это не примененный фильтр. То есть
    # отдаются все данные, которые есть без фильтрации.
    level_1_df = pd.read_csv('data/level_1_selected_items.csv', dtype=str)

    # Список чек-боксов Level_1
    checklist_level_1_options = functions.level_checklist_data(level_1_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_1_values = []

    # Список чек-боксов Level_2
    level_2_df = pd.read_csv('data/level_2_selected_items.csv', dtype=str)
    checklist_level_2_options = functions.level_checklist_data(level_2_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_2_values = []

    # Список чек-боксов Level_3
    level_3_df = pd.read_csv('data/level_3_selected_items.csv', dtype=str)
    checklist_level_3_options = functions.level_checklist_data(level_3_df)[0]
    # на начальном экране фильтра пустые
    checklist_level_3_values = []

    #  теперь надо проверять. Если список чек-боксов не None и его длина не равна нулю, то
    # то надо включать фильтр по выбранному чек-боксу. В таблицу
    # print('checklist_level_1: ', checklist_level_1)
    if checklist_level_1 and len(checklist_level_1)>0:
        result_df = result_df.loc[result_df['level_1'].isin(checklist_level_1)]
        checklist_level_1_values = checklist_level_1

    if checklist_level_2 and len(checklist_level_2)>0:
        result_df = result_df.loc[result_df['level_2'].isin(checklist_level_2)]
        checklist_level_2_values = checklist_level_2

    if checklist_level_3 and len(checklist_level_3)>0:
        result_df = result_df.loc[result_df['level_3'].isin(checklist_level_3)]
        checklist_level_3_values = checklist_level_3


    result_df.to_csv('data/result_df.csv')


    table_list = []

    for index,row in result_df.iterrows():
        temp_dict = {}
        teh_mesto_code = row['Техническое место']

        temp_dict['Код технического места'] = teh_mesto_code
        temp_dict['Наименование технического места'] = row['Название технического места']
        table_list.append(temp_dict)
    table_df = pd.DataFrame(table_list)
    number_of_rows = len(table_df)
    number_of_rows_text = 'Количество записей: {}'.format(number_of_rows)
    # print(table_df)

    code_table = dash_table.DataTable(
        # id='table',
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict('records'),

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

    return checklist_level_1_values, checklist_level_1_options,checklist_level_2_values, checklist_level_2_options, checklist_level_3_values, checklist_level_3_options, code_table, number_of_rows_text


if __name__ == "__main__":
    app.run_server(debug=True)
