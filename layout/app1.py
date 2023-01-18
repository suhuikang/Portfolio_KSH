import data.app1_d as app1_d
from dash import html, dcc


def app1_layout():
    sample_layout = html.Div([
    html.Div([
        html.Img(src='/static/images/pro1.jpg', style={'height':'20%', 'width':'20%'}),
        dcc.Markdown(children=app1_d.markdown_title())],
        style={'border-bottom': 'thin lightgrey solid'}),
    html.Div([
        dcc.Markdown(children=app1_d.markdown_set())
        ]),
    html.Div([
        html.Img(src='/static/images/슬라이드16.JPG',style={'height':'80%', 'width':'80%'}),
        html.Img(src='/static/images/슬라이드17.JPG',style={'height':'80%', 'width':'80%'}),
        html.Img(src='/static/images/슬라이드18.JPG',style={'height':'80%', 'width':'80%'})
        ]
    )
    ],style={'textAlign': 'center'})

    return sample_layout