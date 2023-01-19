from flask import Flask
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import json
from flask import render_template
import layout.app1 as app1_lay
import layout.app2 as app2_lay
import layout.app3 as app3_lay

# ---------
# stylesheets-------

external_stylesheets_1 = ["app1_style.css"]
external_stylesheets_2 = ["app2_style.css"]
external_stylesheets_3 = ["app3_style.css"]

# -------------------------------
app = Flask(__name__)
#
app1 = Dash(__name__, server=app, url_base_pathname='/keyword/', assets_url_path="app1_style.css")
app2 = Dash(__name__, server=app, url_base_pathname='/ddareung/', assets_url_path="app2_style.css")
app3 = Dash(__name__, server=app, url_base_pathname='/jeju/', assets_url_path="app3_style.css")


# -----------------------------------------------
# route
# -----------------------------------------------

@app.route("/")
def index():
    return render_template('index.html')

# -----------------------------------------------
# layout
# -----------------------------------------------


app1.layout = app1_lay.app1_layout()

app2.layout = app2_lay.app2_layout()

app3.layout = app3_lay.app3_layout()

@app3.callback(
    Output('app3_graph_pop', 'figure'),
    Input('pop-year-slider', 'value'))
def app3_fig_pop(selected_year):
    df = pd.read_csv('./assets/년도 및 지역별 인구(년 평균).csv', index_col=0)
    df = df[df['년도'] == selected_year]
    dpop = df.sort_values('방문인구')

    fig = px.bar(dpop, x=["방문인구", "근무인구", "거주인구"], y='지역',
             title='지역별 인구(평균)',
             height=800)

    fig.update_layout(transition_duration=500)

    return fig

@app3.callback(
    Output("temp_cost_graph", "figure"),
    Input("temp_cost_year", "value"))
def app3_temp_cost(temp_cost_year):
    df = pd.read_csv('./assets/지역별 외식업 이용금액.csv',index_col=0)
    geo=json.load(open('./assets/HangJeongDong_ver20230101.geojson', encoding='utf-8'))
    fig = px.choropleth(
        df, geojson=geo, color=temp_cost_year,
        locations="temp", featureidkey="properties.temp",
        projection="mercator",color_continuous_scale='Blues')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_text='지역별 외식업 이용금액')
    return fig

if __name__ == "__main__":
    # app.debug = True
    app.run()
