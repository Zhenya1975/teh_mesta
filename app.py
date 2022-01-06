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

teh_mesta_full_list = pd.read_csv('data/teh_masta_full_list.csv', dtype=str)
teh_mesta_full_list['code'] = "first" + teh_mesta_full_list['Техническое место']

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
def meeting_plan_fact(checklist_level_1, select_all_level_1, release_all_level_1, checklist_level_2, select_all_level_2, release_all_level_2, checklist_level_3, select_all_level_3, release_all_level_3):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    ########### УРОВЕНЬ 1 #################
    checklist_level_1_values = []
    level_1_df = pd.read_csv('data/level_1_selected_items.csv', dtype=str)
    # Список чек-боксов Level_1
    checklist_level_1_options = functions.level_checklist_data(level_1_df)[0]
    # Полный список значений списка level_1
    checklist_level_1_full_values = functions.level_checklist_data(level_1_df)[1]

    if checklist_level_1:
        checklist_level_1_values = checklist_level_1


    # Обработчик кнопок "Снять / Выбрать" в блоке Регионы
    id_select_all_level_1_button = "select_all_level_1"
    id_release_all_level_1_button = "release_all_level_1"
    # при клике на кнопку Выбрать все - выбираем все и наоборот

    if id_select_all_level_1_button in changed_id:
        checklist_level_1_values = checklist_level_1_full_values
    elif id_release_all_level_1_button in changed_id:
        checklist_level_1_values = []

    ########### УРОВЕНЬ 2 #################
    checklist_level_2_values = []
    level_2_df = pd.read_csv('data/level_2_selected_items.csv', dtype=str)
    # Список чек-боксов Level_2
    checklist_level_2_options = functions.level_checklist_data(level_2_df)[0]
    # Полный список значений списка level_2
    checklist_level_2_full_values = functions.level_checklist_data(level_2_df)[1]

    if checklist_level_2:
        checklist_level_2_values = checklist_level_2


    # Обработчик кнопок "Снять / Выбрать" в блоке Регионы
    id_select_all_level_2_button = "select_all_level_2"
    id_release_all_level_2_button = "release_all_level_2"
    # при клике на кнопку Выбрать все - выбираем все и наоборот

    if id_select_all_level_2_button in changed_id:
        checklist_level_2_values = checklist_level_2_full_values
    elif id_release_all_level_2_button in changed_id:
        checklist_level_2_values = []

    ########### УРОВЕНЬ 3 #################
    checklist_level_3_values = []
    level_3_df = pd.read_csv('data/level_3_selected_items.csv', dtype=str)
    # Список чек-боксов Level_3
    checklist_level_3_options = functions.level_checklist_data(level_3_df)[0]
    # Полный список значений списка level_2
    checklist_level_3_full_values = functions.level_checklist_data(level_3_df)[1]

    if checklist_level_3:
        checklist_level_3_values = checklist_level_3

    # Обработчик кнопок "Снять / Выбрать"
    id_select_all_level_3_button = "select_all_level_3"
    id_release_all_level_3_button = "release_all_level_3"
    # при клике на кнопку Выбрать все - выбираем все и наоборот

    if id_select_all_level_3_button in changed_id:
        checklist_level_3_values = checklist_level_3_full_values
    elif id_release_all_level_3_button in changed_id:
        checklist_level_3_values = []


    base = r'{}'
    expr = '(?=.*{})'
    words = checklist_level_1_values + checklist_level_2_values+checklist_level_3_values
    print('words:',words)
    x = base.format(''.join(expr.format(w) for w in words))
    print(x)

    result_df = teh_mesta_full_list[teh_mesta_full_list['code'].str.contains(x)]
    result_df.to_csv('data/result_df.csv')

    return checklist_level_1_values, checklist_level_1_options, checklist_level_2_values, checklist_level_2_options, checklist_level_3_values, checklist_level_3_options





if __name__ == "__main__":
    app.run_server(debug=True)
