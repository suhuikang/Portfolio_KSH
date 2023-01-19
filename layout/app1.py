import data.app1_d as app1_d
from dash import html, dcc


def app1_layout():
    sample_layout = html.Div([
    html.Div([

        dcc.Markdown(children=app1_d.markdown_title())]),
    html.Div([
        dcc.Markdown(children=app1_d.markdown_set())
        ]),
    html.Div([
        html.Img(src='/static/images/슬라이드16.JPG',style={'height':'100%', 'width':'100%'}),
        ]
    )
    ],style={'margin': '10%'})

    return sample_layout