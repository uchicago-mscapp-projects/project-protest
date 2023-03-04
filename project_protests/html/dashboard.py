####Task: Create HTML file using dash
###Author: JP Martinez
###Last Modification: 03.03.2023

import dash
import pandas as pd
#import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from text_inputs import HTML_TEXT

app =dash.Dash(__name__,assets_folder="assets")

background_color = "background-color : rgb(255, 245, 238)"
style_h1 = {"text-align":"center","background-color" : "rgb(255, 245, 238)",
"font":"Arial", "border-style": "solid"} 
style_p = {"text-align":"left","background-color" : "rgb(255, 245, 238)","font":r"120% Arial",
"margin-left":"5cm","margin-right":"5cm"}
style_h2 = {"text-align":"left","background-color" : "rgb(255, 245, 238)","font":r"Arial",
"margin-left":"5cm","margin-right":"5cm"}  


app.layout = html.Div(style={'backgroundColor': "rgb(255, 245, 238)"},
    children= [
    html.H1(HTML_TEXT["Title"],style = style_h1),
    html.P(HTML_TEXT["paragraphs"]["introduction"],style = style_p),
    html.P(HTML_TEXT["paragraphs"]["introduction_2"],style = style_p),
    html.P(HTML_TEXT["paragraphs"]["description"],style = style_p),
    html.H2(HTML_TEXT["subtitles"]["Number of protest"],style = style_h2),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "Chicago", "value": "Chicago"},
                     {"label": "LA", "value": "LA"},
                     {"label": "Minneapolis", "value": "Minneapolis"},
                     {"label": "New York", "value": "New York"},
                     {"label":"All cities","value":"All cities"}],
                 multi=False,
                 value="Chicago",
                 style={'width': "40%"}
                 ),
    dcc.Graph(id="Heatmap",figure={}),
    html.P("Description of first analysis: Heatmap of number of protests",style = style_p),
    html.H2(HTML_TEXT["subtitles"]["Police"],style = style_h2),
    dcc.Graph(id="",figure={}),
    html.H2(HTML_TEXT["subtitles"]["News_coverage"],style = style_h2),
    dcc.Graph(id="News",figure={}),
    html.H2(HTML_TEXT["subtitles"]["Sentiment_analysis"],style = style_h2),
    dcc.Graph(id="News_2",figure={}),
    html.H2(HTML_TEXT["subtitles"]["Conclusion"],style = style_h2),

])

#if __name__ == "__main__":
app.run_server(debug = True)