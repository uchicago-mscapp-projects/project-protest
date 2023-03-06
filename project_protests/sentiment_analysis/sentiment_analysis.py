##Author: JP Martinez
##Task: Perform simple sentiment analysis on news dataframe
##Last date updated: 03.01.23

import pandas as pandas
import os
import nltk
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import pathlib
nltk.download([
"vader_lexicon",
])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

BOUNDS = {"classifier": ([-1,0,1],["negative","positive"])}
WORDS_TO_UPDATE = {
    "protest": 0, "brutality": 0
}

nyt_pathfile = pathlib.Path(__file__).parent.parent.parent / "clean_data/raw_data/nyt_articles.csv"
the_guardian_pathfile = pathlib.Path(__file__).parent.parent / "api_requests/the_guardian/data/the_guardian_compiled.csv"

def edit_sentiment_dictionary(update_dict = WORDS_TO_UPDATE):
    """
    Edit sentiment dictionary to exclude certain words that are common and
    neutral in the context but that the nltk dictionary classifies as negative
    """
    sia.lexicon.update(update_dict)

def sentiment_scores(filename, columns_list):
    """
    Calculate sentiment scores for the headline and lead sections of the news
    retrieve by The New York Times and The Guardian API's.
    Inputs:
     - filename: filename of csv data to open to perform the sentiment analysis in
    
    Returns:
    df : Updated df with new columns that classify the sentiment of the given columns

    """

    edit_sentiment_dictionary()
    
    df = pd.read_csv(filename)
    bounds, label = BOUNDS["classifier"]
    for col in columns_list:
        if "{}".format(col) in df.columns:
            df["{}_score".format(col)] = df["{}".format(col)].apply(lambda x:
            sia.polarity_scores(x)["compound"])
            df["{}_sentiment".format(col)] = pd.cut(df["{}_score".format(col)],
            bins = bounds, labels = label, include_lowest = True, right = True)

    return df

    
def visualize_sentiment_scores(column):
    
    df_nyt = sentiment_scores(nyt_pathfile,[column])
    df_tg = sentiment_scores(the_guardian_pathfile, [column])
    df = pd.concat([df_nyt,df_tg])
    df["year"] = pd.DatetimeIndex(df['date']).year
    df = df[df["year"] != 2023]
    fig = make_subplots(rows=2,cols=3)
    for idx, year in enumerate(df['year'].unique()):
        chart = px.histogram(df[df['year']==year], x="{}_score".format(column), color='year')
        chart.update_layout(title=str(year))
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
    fig.show()

def visualize_sentiment_scores_2(column):
    
    df_nyt = sentiment_scores(nyt_pathfile,[column])
    df_tg = sentiment_scores(the_guardian_pathfile, [column])
    df = pd.concat([df_nyt,df_tg])
    df["year"] = pd.DatetimeIndex(df['date']).year
    df = df[df["year"] != 2023]
    fig = make_subplots(rows=2,cols=3)
    for idx, year in enumerate(df['year'].unique()):
        chart = px.histogram(df[df['year']==year], x="{}_score".format(column), color='year')
        chart.update_layout(title=str(year))
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
    fig.show()