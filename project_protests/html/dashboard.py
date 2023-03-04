####Task: Create HTML file using dash
###Author: JP Martinez
###Last Modification: 03.03.2023

import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from text_inputs import HTML_TEXT

app =dash.Dash(__name__,assets_folder="/assets",external_stylesheets=[dbc.themes.GRID])

df = pd.read_excel("Test_data.xlsx", sheet_name = "Test_1")

background_color = "background-color : rgb(255, 251, 250)"
style_h1 = {"text-align":"center", "border-width": "1px",
"font-family":r"Arial", "border-style": "solid"} 
style_p = {"text-align":"left","font":r"120% Arial",
"margin-left":"5cm","margin-right":"5cm"} 
style_h2 = {"text-align":"left","font":r"150% Arial",
"font-weight":"bold","margin-left":"5cm","margin-right":"5cm"}  

title_container = dbc.Container(
    fluid = True,
    style={
            "height": "70vh",
            "background-color": "rgb(40,40,43)",
            "color": "rgb(255, 251, 250)",
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "center",
            "align-items": "center"
        },
    children=[html.H1(HTML_TEXT["Title"],style = style_h1)]
)  


app.layout = html.Div(style={'backgroundColor': "rgb(255, 251, 250)",
    "color":"rgb(40,40,43)"},
    children= [
    title_container,
    html.Br(),
    html.P(HTML_TEXT["paragraphs"]["introduction"],style = style_p),
    html.P(HTML_TEXT["paragraphs"]["introduction_2"],style = style_p),
    html.P(HTML_TEXT["paragraphs"]["description"],style = style_p),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Number of protest"],style = style_h2),
    dcc.Dropdown(id="select_city",
                 options=[
                     {"label": "Chicago", "value": "Chicago"},
                     {"label": "LA", "value": "LA"},
                     {"label": "Minneapolis", "value": "Minneapolis"},
                     {"label": "New York", "value": "New York"},
                     {"label":"All cities","value":"All cities"}],
                 multi=False,
                 value="All cities",
                 style={'width': "40%","font":"Arial"}
                 ),
    dcc.Graph(id="Heatmap",figure={}),
    html.P("Description of first analysis: Heatmap of number of protests",style = style_p),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Police"],style = style_h2),
    dcc.Graph(id="",figure={}),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["News_coverage"],style = style_h2),
    dcc.Graph(id="News",figure={}),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Sentiment_analysis"],style = style_h2),
    dcc.Graph(id="News_2",figure={}),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Conclusion"],style = style_h2),

])

@app.callback(
    [Output(component_id="Heatmap",component_property="figure")],
    [Input(component_id = "select_city",component_property = "value")]
 )

def update_graph(city_selected):
    print(city_selected)
    dff = df.copy()
    if city_selected != "All cities":
        dff = dff[dff["City"] == city_selected]
    fig = px.line(dff, x = "Year", y = "Population")
    return [fig]

if __name__ == "__main__":
    app.run_server(debug = True)