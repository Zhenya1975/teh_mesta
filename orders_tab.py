from dash import dcc, html
import dash_bootstrap_components as dbc
loading_style = {
    # 'position': 'absolute',
    # 'align-self': 'center'
                 }
def orders_tab():
    orders_tab_block = dcc.Tab(
        label='Заказы',
        value='tab_orders',
        children=[
            dbc.Row(justify="start",
            children = [
              html.Div([
                dbc.Button("Выгрузить заказы xlsx", id="btn-download-orders", size="sm",
                                    style={'marginBottom': '3px',
                                            'marginTop': '3px',
                                            'backgroundColor': '#232632'},),
                dcc.Download(id="download-excel-orders")
              ]),
              
            ]),

            dbc.Row([
                # колонка с фильтрами
                dbc.Col(width=4,
                  children=[
                    html.P(),
                    html.Div([
                      "Уровень 1",
                      dcc.Dropdown(id="checklist_level_1_orders_tab", multi=True),
                  ]),
                    
                    html.P(),
                    html.Div([
                      "Уровень 2",
                      dcc.Dropdown(id="checklist_level_2_orders_tab", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень 3",
                      dcc.Dropdown(id="checklist_level_3_orders_tab", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень 4",
                      dcc.Dropdown(id="checklist_level_4_orders_tab", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень 5",
                      dcc.Dropdown(id="checklist_level_5_orders_tab", multi=True),
                  ]),

                  html.P(),
                    html.Div([
                      "Уровень Вышестоящее техместо",
                      dcc.Dropdown(id="checklist_level_upper_orders_tab", multi=True),
                  ]),
                  ]
                ),
                dbc.Col(width=8,
                    children=[
                        html.P(id='number_of_rows_text_orders_tab'),
                        
                        html.P(),
                        html.Div(
                            children=[
                                html.Div(id='orders_table_orders_tab'),
                                dcc.Loading(id='loading_orders_tab', parent_style=loading_style)
                            ], style={
                                # 'position': 'relative',
                                # 'display': 'flex',
                                'justify-content': 'center'
                                      }
                            ),


                    ]),
                
            ]),
            #dbc.Row([
                
            #]),
        
        ]
    )
    return orders_tab_block