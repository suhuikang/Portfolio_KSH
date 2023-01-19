import data.app3_d as app3_d
from dash import html, dcc


def app3_layout():
    sample_layout = html.Div([
        html.Div([
            dcc.Markdown(children=app3_d.app3_intro_text())
            ]),
        html.Div(className="app3_main",
                 children=[
                     dcc.Markdown(children=app3_d.app3_set_text()),
                     html.Br(),
                     html.H3(children='')
                     html.Div(
                         children='''
                         '''
                     ])
                     dcc.Graph(
                        id='app3_graph',
                        figure=app3_d.app3_fig()
                     ),
                     dcc.Graph(
                         id='app3_graph_menu',
                         figure=app3_d.app3_fig_menu()
                     ),
                     dcc.Graph(
                         id='app3_graph_s_menu',
                         figure=app3_d.app3_fig_small_m()
                     ),
                     dcc.Graph(
                         id='app3_graph_age_cost',
                         figure=app3_d.app3_fig_age_cost()
                     ),
                     html.Div([
                         dcc.Graph(id='app3_graph_pop'),
                         dcc.Slider(
                             app3_d.app3_pop_slider_df()['년도'].min(),
                             app3_d.app3_pop_slider_df()['년도'].max(),
                             step = None,
                             value = app3_d.app3_pop_slider_df()['년도'].min(),
                             marks = {str(year): str(year) for year in app3_d.app3_pop_slider_df()['년도'].unique()},
                             id = 'pop-year-slider'
                         )
                     ]),
                     html.Div([
                         html.H4('지역별 외식업 이용금액'),
                         html.P("Select year:"),
                         dcc.RadioItems(
                             id='temp_cost_year',
                             options=["2017", "2018", "2019", "2020", "2021"],
                             value=app3_d.app3_temp_cost_slide_df()['2017'],
                             inline=True
                         ),
                         dcc.Graph(id="temp_cost_graph"),
                     ]),
                     dcc.Graph(
                         id='app3_f_graph',
                         figure=app3_d.app3_f_temp()
                     )
                 ]),
        html.Div(className="app3_footer")

    ],style={'margin': '10%'})

    return sample_layout