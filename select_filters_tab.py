from dash import dcc, html
import dash_bootstrap_components as dbc

def select_filters_tab():
    select_filters_tab_block = dcc.Tab(
        label='Выбор параметров техмест',
        value='tab_select_parameters',
        children=[
            dbc.Row([
                dbc.Col(
                    children=[
                        html.P("Уровень 1"),
                        html.Div(style={'marginLeft': '3px'},
                                 children=[
                                     dbc.Button("Выбрать все", size="sm",
                                                id="select_all_level_1",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'}
                                                ),
                                     dbc.Button("Снять выбор", color="secondary",
                                                id="release_all_level_1",
                                                size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},
                                                ),
                                     dcc.Checklist(
                                         id='checklist_level_1',
                                         # options=regions,
                                         # value=regions_list,
                                         labelStyle=dict(display='block')),
                                     # html.Hr(className="hr"),

                                     html.P(),
                                 ])
                    ]
                ),
                dbc.Col(
                    children=[
                        html.P("Уровень 2"),
                        html.Div(style={'marginLeft': '3px'},
                                 children=[
                                     dbc.Button("Выбрать все", size="sm",
                                                id="select_all_level_2",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'}
                                                ),
                                     dbc.Button("Снять выбор", color="secondary",
                                                id="release_all_level_2",
                                                size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},
                                                ),
                                     dcc.Checklist(
                                         id='checklist_level_2',
                                         # options=regions,
                                         # value=regions_list,
                                         labelStyle=dict(display='block')),
                                     # html.Hr(className="hr"),

                                     html.P(),
                                 ])
                    ]
                ),
                dbc.Col(
                    children=[
                        html.P("Уровень 3"),
                        html.Div(style={'marginLeft': '3px'},
                                 children=[
                                     dbc.Button("Выбрать все", size="sm",
                                                id="select_all_level_3",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'}
                                                ),
                                     dbc.Button("Снять выбор", color="secondary",
                                                id="release_all_level_3",
                                                size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},
                                                ),
                                     dcc.Checklist(
                                         id='checklist_level_3',
                                         # options=regions,
                                         # value=regions_list,
                                         labelStyle=dict(display='block')),
                                     # html.Hr(className="hr"),


                                 ])
                    ]
                )
            ]),
            dbc.Row([
                dbc.Col(
                    children=[
                        html.P(),
                        html.Div(id='code_table'),
                    ])
            ])
        ]
    )
    return select_filters_tab_block