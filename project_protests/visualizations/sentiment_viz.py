##Author: JP Martinez
##Task: Graph sentiment analysis results
##Last date updated: 03.01.23

import pandas as pandas
import os
import nltk
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import pathlib
from project_protests.sentiment_analysis.sentiment_analysis import sentiment_scores
# nltk.download([
# "vader_lexicon",
# ])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def visualize_sentiment_scores(column):
    
    df_nyt = sentiment_scores(nyt_filepath,[column])
    df_tg = sentiment_scores(guardian_filepath, [column])
    df = pd.concat([df_nyt,df_tg])
    df["year"] = pd.DatetimeIndex(df['date']).year
    df = df[df["year"] != 2023]
    fig = make_subplots(rows=2,cols=3,subplot_titles=['2017', '2018', '2019', '2020', '2021', '2022'])
    for idx, year in enumerate(df['year'].unique()):
        chart = px.histogram(df[df['year']==year], x="{}_score".format(column), nbins = 10)
        chart.update_layout(title=str(year))
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
            
    return fig

# def visualize_sentiment_scores_2(column):
    
#     df_nyt = sentiment_scores(nyt_pathfile,[column])
#     df_tg = sentiment_scores(the_guardian_pathfile, [column])
#     df = pd.concat([df_nyt,df_tg])
#     df["year"] = pd.DatetimeIndex(df['date']).year
#     df = df[df["year"] != 2023]
#     fig = make_subplots(rows=2,cols=3)
#     for idx, year in enumerate(df['year'].unique()):
#         chart = px.histogram(df[df['year']==year], x="{}_score".format(column), color='year')
#         chart.update_layout(title=str(year))
#         if idx < 3:
#             fig.append_trace(chart.data[0], row=1, col=idx+1)
#         else:
#             fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
#     fig.show()