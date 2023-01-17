import data.app1_d as app1_d
from dash import html, dcc


def app1_layout():
    markdown_title = '''
    # 쇼핑키워드 검색량 기반 분석
    
    쇼핑키워드 카테고리 별 검색량을 기반으로  
    카테고리 별 상품키워드 추천 및 제품 검색량 변화에 따른 기업의 주가변화 확인에 목표를 둠
    
    [쇼핑키워드 ppt](https://www.miricanvas.com/v/11ptcya)
    [https://www.miricanvas.com/v/11ptcya](https://www.miricanvas.com/v/11ptcya)'''
    
    markdown_set='''
    프로젝트 진행기간 : 2022.10.17 ~ 2022.10.21

    개발환경
    - python
    - request, selenium
    - pandas
    - matplotlib, seaborn
    '''


    sample_layout = html.Div([
    html.Div([
        html.Img(src='/static/images/슬라이드1.jpg'),
        dcc.Markdown(children=markdown_title)],
        style={'border-bottom': 'thin lightgrey solid'}),
    html.Div([
        dcc.Markdown(children=markdown_set)
        ]),
    html.Div([
        html.Img(src='/static/images/슬라이드16.JPG'),
        html.Img(src='/static/images/슬라이드17.JPG'),
        html.Img(src='/static/images/슬라이드18.JPG')
        # dcc.Markdown(children=markdown_text2)
    ])

        ])

    return sample_layout