import data.app2_d as app2_d
from dash import html, dcc


def app2_layout():

    sample_layout = html.Div([
    html.Div([
        dcc.Markdown(children=app2_d.markdown_title())],
        ),
    html.Div([
        html.Img(src='/static/images/2_all.jpg',style={'height':'100%', 'width':'100%'}),
        # dcc.Markdown(children=markdown_text2)
    ])

        ],style={'margin': '10%'})

    return sample_layout