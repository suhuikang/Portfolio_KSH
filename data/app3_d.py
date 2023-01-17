import plotly.express as px
import pandas as pd


def app3_intro_text():
    app3_intro = '''
    # 제주 예비창업자를 위한 업종분석  

    제주형 실패보장제를 통해 창업에 도전하고 싶은 예비창업자들을 위한 분석  

    '''
    return app3_intro


def app3_fig():
    dfff = pd.read_csv('./assets/업종별 카드매출.csv', index_col=0)
    fig = px.line(dfff, x='연월', y=['건강보조식품 소매업', '골프장 운영업', '과실 및 채소 소매업', '관광 민예품 및 선물용품 소매업',
       '그외 기타 분류안된 오락관련 서비스업', '그외 기타 스포츠시설 운영업', '그외 기타 종합 소매업',
       '기타 갬블링 및 베팅업', '기타 대형 종합 소매업', '기타 수상오락 서비스업', '기타 외국식 음식점업',
       '기타 주점업', '기타음식료품위주종합소매업', '내항 여객 운송업', '마사지업', '면세점', '버스 운송업',
       '비알콜 음료점업', '빵 및 과자류 소매업', '서양식 음식점업', '수산물 소매업', '슈퍼마켓',
       '스포츠 및 레크레이션 용품 임대업', '여관업', '여행사업', '욕탕업', '육류 소매업', '일반유흥 주점업',
       '일식 음식점업', '자동차 임대업', '전시 및 행사 대행업', '정기 항공 운송업', '중식 음식점업',
       '차량용 가스 충전업', '차량용 주유소 운영업', '체인화 편의점', '피자, 햄버거, 샌드위치 및 유사 음식점업',
       '한식 음식점업', '호텔업', '화장품 및 방향제 소매업', '휴양콘도 운영업', '택시 운송업'], title='업종별 매출')

    return fig

def app3_fig_menu():
    df = pd.read_csv('./assets/메뉴별 외식업 매출.csv', index_col=0)
    fig = px.line(df, y=['과일/샐러드류', '구이류', '국/탕/찌개/전골류', '기타', '김치류', '냉채/무침류', '데침/삶음류',
       '떡류', '만두류', '면류', '묵류', '밥류', '볶음류', '빙과류', '빵/과자류', '음료류',
       '장/장아찌류', '적/꼬치류', '전/부침류', '조림류', '주류', '죽류', '찜류', '추가/사리',
       '튀김류', '회류'], title='메뉴별 외식업 매출')

    return fig

def app3_fig_small_m():
    df = pd.read_csv('./assets/소분류업종별 이용금액.csv')
    fig = px.line(df, x='연월',y=['갈매기살', '갈비/삼겹살', '갈치/생선구이', '게장전문', '고기부페', '고등어전문', '곰장어전문',
       '곱창/양구이전문', '국수/만두/칼국수', '굴요리전문', '기사식당', '기타고기요리', '기타서양음식전문',
       '꼬치구이전문점', '나이트클럽', '낙지/오징어', '냉면집', '닭갈비전문', '닭내장/닭발요리', '닭도리탕전문',
       '도너츠전문', '도시락전문점', '돈가스전문점', '돌구이요리전문', '돌솥/비빔밥전문점', '동남아음식전문점',
       '두부요리전문', '떡/한과', '떡볶이전문', '라면김밥분식', '룸살롱/단란주점', '막창구이', '매운탕전문',
       '민물장어전문', '민속주점', '바닷가재/게요리전문', '바베큐전문', '버섯전문점', '보리밥전문', '복전문',
       '부대찌개/섞어찌개', '부페', '불고기전문', '불닭전문', '빠/카페', '사철탕전문', '삼계탕전문',
       '샌드위치/브런치/샐러드', '생과일주스전문점', '생선찜전문', '샤브샤브전문', '설렁탕집', '소주방/포장마차',
       '수산물전문음식점', '순대전문점', '순두부전문', '스낵', '스테이크전문점', '스파게티전문점', '쌈밥전문',
       '아구전문', '아이스크림/빙수', '오리고기전문', '옻닭전문', '와플/파이/디저트', '우동전문점', '이자까야',
       '일반유흥주점', '일반한식/백반', '일식', '재첩국전문', '전통찻집/인삼찻집', '정통양식/경양식', '제과점',
       '조개구이전문', '족발/보쌈전문', '죽전문점', '중국음식', '찐빵/만두', '찜닭전문점', '참치전문점',
       '철판구이요리전문', '초밥전문', '추어탕전문', '카레전문점', '커피전문점', '케익전문점', '콩나물국밥',
       '토스트전문', '토종닭전문', '파전전문', '패밀리레스토랑', '패스트푸드', '퓨전음식전문', '피자전문',
       '한식부페', '한정식전문', '핫도그', '해물찜/탕전문', '해장국/감자탕', '호두과자', '호떡/붕어빵',
       '호프/맥주', '홍어전문', '황태전문', '횟집', '후라이드/양념치킨', '탕수육전문점', '해물부페',
       '보드게임카페'], title='외식업 소분류업종별 이용금액')

    return fig

def app3_fig_age_cost():
    df= pd.read_csv('./assets/나이별 외식업 이용금액 현황.csv')
    fig = px.line(df,x='base_year_month',y=['20대 이하', '30대', '40대', '50대', '60대', '70대 이상'],
                  title='나이별 외식업 이용금액 현황')
    return fig


def app3_fig_pop(selected_year):
    df = pd.read_csv('./assets/년도 및 지역별 인구(년 평균).csv')
    dpop = df.sort_values('거주인구')

    fig = px.bar(dpop, x=["방문인구", "근무인구", "거주인구"], y='지역',
             title='2021년 지역별 인구(평균)',
             width=800, height=800)

    fig.update_layout(transition_duration=500)

    return fig


def app3_pop_slider_df():
    df = pd.read_csv('./assets/년도 및 지역별 인구(년 평균).csv',index_col=0)
    return df

def app3_temp_cost_slide_df():
    df = pd.read_csv('./assets/지역별 외식업 이용금액.csv')
    return df

def app3_f_temp():
    df=pd.read_csv('./assets/지역별 폐업 수.csv')
    ff=df['temp'].value_counts()
    fig=px.bar(ff,title='지역별 폐업한 일반음식점(외식업)수')
    return fig