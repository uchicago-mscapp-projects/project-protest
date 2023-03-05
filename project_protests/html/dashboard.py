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
#from .visualization.protest_viz import go_cities 

app =dash.Dash(__name__,external_stylesheets=[dbc.themes.GRID])

df = pd.read_csv("./Test_data.csv")

#fig_lisette = go_cities()

background_color = "background-color : rgb(255, 251, 250)"
style_h1 = {"text-align":"center", "border-width": "1px",
"font-family":r"Arial", "border-style": "solid"} #"background-color" : "rgb(255, 245, 238)",
style_p = {"text-align":"left","font":r"120% Arial",
"margin-left":"5cm","margin-right":"5cm"} #"background-color" : "rgb(255, 245, 238)"
style_h2 = {"text-align":"left","font":r"150% Arial", "text-decoration": "underline",
"font-weight":"bold","margin-left":"5cm","margin-right":"5cm"}  #"background-color" : "rgb(255, 245, 238)"
style_h3 = {"text-align":"left","font-family":r"Arial", "text-decoration": "underline",
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


app.layout = html.Div(style={'background-color': "rgb(255, 251, 250)",
    "color":"rgb(40,40,43)", "right-margin":"5cm","left-margin":"5cm"},
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
    html.Div(children=[dcc.Graph(id="Heatmap",figure={},style={'display': 'inline-block'}),
    html.P("Description of first analysis: Heatmap of number of protests",style={'display': 'inline-block'})]),
    #dcc.Graph(id="Heatmap",figure={}),
    #html.P("Description of first analysis: Heatmap of number of protests",style = style_p),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Police"],style = style_h2),
    dcc.Dropdown(id="select_year",
                 options=[
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021},
                     {"label":"2022","value": 2020},
                     {"label":"All years","value":"All years"}],
                 multi=False,
                 value="All years",
                 style={'width': "40%","font":"Arial"}
                 ),
    dcc.Graph(id="Years",figure={}),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["News"],style = style_h2),
    html.P("Introduction paragraph about news",style = style_p),
    html.H3(HTML_TEXT["sub_subtitles"]["coverage"], style = style_h3),
    dcc.Graph(id="News",figure={}),
    html.Br(),
    html.H3(HTML_TEXT["sub_subtitles"]["sentiment"],style = style_h3),
    dcc.Graph(id="News_sentiment",figure={}),
    html.H3(HTML_TEXT["sub_subtitles"]["pairwise"],style = style_h3),
    dcc.Graph(id="News_pairwise",figure={}),
    html.Br(),
    html.H2(HTML_TEXT["subtitles"]["Conclusion"],style = style_h2),

])

@app.callback(
    [Output(component_id="Heatmap",component_property="figure"),
    Output(component_id="Years",component_property="figure")],
    [Input(component_id = "select_city",component_property = "value"),
    Input(component_id = "select_year",component_property = "value")]
 )

def update_graph(city_selected,year_selected):
    print(city_selected)
    print(year_selected)
    dff = df.copy()
    if city_selected != "All cities":
        dff = dff[dff["City"] == city_selected]
    fig = px.line(dff, x = "Year", y = "Population", color = "City")

    dff = df.copy()
    if year_selected != "All years":
        dff = dff[dff["Year"] == year_selected]
    fig_1 = px.line(dff, x = "Year", y = "Population", color = "City")

    return [fig, fig_1]

if __name__ == "__main__":
    app.run_server(debug = True)