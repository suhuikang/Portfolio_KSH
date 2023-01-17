import data.app2_d as app2_d
from dash import html, dcc


def app2_layout():
    markdown_title = '''
    # 날씨 데이터를 활용한 서울시 공공자전거 모델
    [https://www.miricanvas.com/v/11jsg3n](https://www.miricanvas.com/v/11jsg3n)'''
    markdown_set = '''
    프로젝트 진행기간 : 2022.11.08 ~ 2022.11.11  
    개발환경  
    - python
    - pandas
    - scikit-learn
    - plotly'''
    sample_layout = html.Div([
    html.Div([
        html.Img(src='/static/images/2_title.jpg'),
        dcc.Markdown(children=markdown_title)],
        style={'border-bottom': 'thin lightgrey solid'}),
    html.Div([
        dcc.Markdown(children=markdown_set)
        ]),
    html.Div([
        html.Img(src='/static/images/2_all.jpg'),
        # dcc.Markdown(children=markdown_text2)
    ])

        ],style={'textAlign': 'center'})

    return sample_layout