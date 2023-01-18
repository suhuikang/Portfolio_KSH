import data.app2_d as app2_d
from dash import html, dcc


def app2_layout():

    sample_layout = html.Div([
    html.Div([
        html.Img(src='/static/images/pro2.jpg', style={'height':'20%', 'width':'20%'}),
        dcc.Markdown(children=app2_d.markdown_title())],
        style={'border-bottom': 'thin lightgrey solid'}),
    html.Div([
        dcc.Markdown(children=app2_d.markdown_set())
        ]),
    html.Div([
        html.Img(src='/static/images/2_all.jpg',style={'height':'80%', 'width':'80%'}),
        # dcc.Markdown(children=markdown_text2)
    ])

        ],style={'textAlign': 'center'})

    return sample_layout