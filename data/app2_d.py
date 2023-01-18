import plotly.express as px
import pandas as pd

def markdown_title():
    text = '''
    # 날씨 데이터를 활용한 서울시 공공자전거 모델 
    
    교통, 복지 측면에서 큰 사회적 가치를 창출하고 있는 서울시 공공자전거 '따릉이'  
    100억원이 넘는 적자를 줄이는데 도움이 되고자 주제선정  
    
    날씨데이터와 따릉이 대여 수요의 상관관계를 찾아 모델을 학습, 평가, 강화 하는데 목적을 두었음
    
    git [코드정리후 주소 추가](https://www.miricanvas.com/v/11jsg3n](https://www.miricanvas.com/v/11jsg3n)  
    ppt [https://www.miricanvas.com/v/11jsg3n](https://www.miricanvas.com/v/11jsg3n)'''
    return text
def markdown_set():
    text = '''
    프로젝트 진행기간 : 2022.11.08 ~ 2022.11.11  
    
    개발환경  
    python, pandas, scikit-learn, plotly'''
    return text
