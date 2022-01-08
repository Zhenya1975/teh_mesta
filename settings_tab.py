from dash import dcc, html
import dash_bootstrap_components as dbc

def settings_tab():
    settings_tab_block = dcc.Tab(
        label='Настройки',
        value='tab_settings',
        children=[
            dbc.Row([
                dbc.Col(
                    children=[
                        html.P("Выбор фильтров уровня 1"),
                    ])
                ])

        ])
    return settings_tab_block