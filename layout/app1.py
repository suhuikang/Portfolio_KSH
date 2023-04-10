import data.app1_d as app1_d
from dash import html, dcc


def app1_layout():

    sample_layout = html.Div([
    html.Div([
        dcc.Markdown(children=app1_d.markdown_title())],
        ),
    html.Div([
        html.Img(src='/static/images/app1_all.jpg',style={'height':'100%', 'width':'100%'}),
        # dcc.Markdown(children=markdown_text2)
    ])

        ],style={'margin': '10%'})

    return sample_layout