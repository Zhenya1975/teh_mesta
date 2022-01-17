from dash import dcc, html
import dash_bootstrap_components as dbc
loading_style = {
    # 'position': 'absolute',
                 # 'align-self': 'center'
                 }
def select_filters_tab():
    select_filters_tab_block = dcc.Tab(
        label='Выбор параметров техмест',
        value='tab_select_parameters',
        children=[
            dbc.Row([
                # колонка с фильтрами
                dbc.Col(width=3,
                  children=[
                    html.P(),
                    html.Div([
                      "Уровень 1",
                      dcc.Dropdown(id="checklist_level_1", multi=True),
                  ]),
                    
                    html.P(),
                    html.Div([
                      "Уровень 2",
                      dcc.Dropdown(id="checklist_level_2", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень 3",
                      dcc.Dropdown(id="checklist_level_3", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень 4",
                      dcc.Dropdown(id="checklist_level_4", multi=True),
                  ]),
                
                 
                  ]

                ),
                
                
                dbc.Col(
                    children=[
                        html.P("Уровень 5"),
                        html.Div(style={'marginLeft': '3px'},
                                 children=[
                                     dbc.Button("Выбрать все", size="sm",
                                                id="select_all_level_5",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'}
                                                ),
                                     dbc.Button("Снять выбор", color="secondary",
                                                id="release_all_level_5",
                                                size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},
                                                ),
                                     dcc.Checklist(
                                         id='checklist_level_5',
                                         # options=regions,
                                         # value=regions_list,
                                         labelStyle=dict(display='block')),
                                     # html.Hr(className="hr"),

                                 ])
                    ]
                ),
                dbc.Col(
                    children=[
                        html.P("Вышестоящее техместо"),
                        html.Div(style={'marginLeft': '3px'},
                                 children=[
                                     dbc.Button("Выбрать все", size="sm",
                                                id="select_all_level_upper",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'}
                                                ),
                                     dbc.Button("Снять выбор", color="secondary",
                                                id="release_all_level_upper",
                                                size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},
                                                ),
                                     dcc.Checklist(
                                         id='checklist_level_upper',
                                         # options=regions,
                                         # value=regions_list,
                                         labelStyle=dict(display='block')),
                                     # html.Hr(className="hr"),

                                 ])
                    ]
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    children=[
                        html.P(id='number_of_rows_text'),
                        html.Div([
                            dbc.Button("Выгрузить Excel", id="btn-download", size="sm",
                                                style={'marginBottom': '3px',
                                                       'marginTop': '3px',
                                                       'backgroundColor': '#232632'},),
                            dcc.Download(id="download-excel")
                        ]),
                        html.P(),
                        html.Div(
                            children=[
                                html.Div(id='code_table'),
                                dcc.Loading(id='loading', parent_style=loading_style)
                            ], style={
                                # 'position': 'relative',
                                # 'display': 'flex',
                                'justify-content': 'center'
                                      }
                            ),


                    ])
            ]),
        
        ]
    )
    return select_filters_tab_block