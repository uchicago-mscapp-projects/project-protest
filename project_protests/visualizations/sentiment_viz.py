import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import nltk
import pathlib
from sentiment_analysis.sentiment_analysis import sentiment_scores

nyt_filepath = pathlib.Path(__file__).parent.parent/ "newspaper/nyt/raw_data/nyt_articles.csv"
the_guardian_filepath = pathlib.Path(__file__).parent.parent / "newspaper/the_guardian/data/the_guardian_compiled.csv"

def columns():
    columns = ['abstract', 'headline', 'lead_paragraph']
    for col in columns:
        visualize_sentiment_scores(col)


def visualize_sentiment_scores(column):
    df_nyt = sentiment_scores(nyt_filepath,[column])
    df_tg = sentiment_scores(the_guardian_filepath, [column])
    df = pd.concat([df_nyt,df_tg])
    df["year"] = pd.DatetimeIndex(df['date']).year
    df = df[df["year"] != 2023]
    
    years = list(df['year'].unique())
    years.sort()
    fig = make_subplots(rows=2,cols=3, 
        subplot_titles=['2017', '2018', '2019', '2020', '2021', '2022'],)

    
    for idx, year in enumerate(years):
        chart = px.histogram(df[df['year']==year], x="{}_score".format(column), nbins=10)
        chart.update_layout(title=str(year))
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
    
    for i,_ in enumerate(fig.data):
        fig.data[i].marker.color = "#1e4477"

    # edit axis labels
    fig['layout']['xaxis']['title']='Score'
    fig['layout']['yaxis']['title']='Count'

    fig['layout']['xaxis2']['title']='Score'
    fig['layout']['yaxis2']['title']='Count'
    
    fig['layout']['xaxis3']['title']='Score'
    fig['layout']['yaxis3']['title']='Count'
    
    fig['layout']['xaxis4']['title']='Score'
    fig['layout']['yaxis4']['title']='Count'

    fig['layout']['xaxis5']['title']='Score'
    fig['layout']['yaxis5']['title']='Count'
    
    fig['layout']['xaxis6']['title']='Score'
    fig['layout']['yaxis6']['title']='Count'

    return fig.show()