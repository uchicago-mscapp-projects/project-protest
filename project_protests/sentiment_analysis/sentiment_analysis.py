##Author: JP Martinez
##Task: Perform simple sentiment analysis on news dataframe
##Last date updated: 03.01.23

import pandas as pandas
import nltk
import pandas as pd
import pathlib
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
nltk.download([
"vader_lexicon",
])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

BOUNDS = {"classifier": ([-1,0,1],["negative","positive"])}
WORDS_TO_UPDATE = {
    "protest": 0, "brutality": 0
}

nyt_filepath = pathlib.Path(__file__).parent.parent/ "newspaper/nyt/raw_data/nyt_articles.csv"
guardian_filepath = pathlib.Path(__file__).parent.parent / "newspaper/the_guardian/data/the_guardian_compiled.csv"

def edit_sentiment_dictionary(update_dict = WORDS_TO_UPDATE):
    """
    Edit sentiment dictionary to exclude certain words that are common and
    neutral in the context but that the nltk dictionary classifies as negative.
    Inputs: 
        update_dict(dict): Dictionary of words to be updated in the dictionary that
        are going to be considered as neutral.
    Return:
    None, it updates vader lexicon dictionary
    """
    sia.lexicon.update(update_dict)

def sentiment_scores(filename, columns_list):
    """
    Calculate sentiment scores for the headline and lead sections of the news
    retrieve by The New York Times and The Guardian API's.
    Inputs:
    - filename: filename of csv data to open to perform the sentiment analysis in
    - columns_list: list of columns in which to calculate the sentiment score
    Returns:
    df : Updated df with new columns that classify the sentiment of the given columns

    """

    edit_sentiment_dictionary()
    
    df = pd.read_csv(filename)
    bounds, label = BOUNDS["classifier"]

    for col in columns_list:
        df[col] = df[col].astype(str) 
        if "{}".format(col) in df.columns:
            df["{}_score".format(col)] = df["{}".format(col)].apply(lambda x:
            sia.polarity_scores(x)["compound"])
            df["{}_sentiment".format(col)] = pd.cut(df["{}_score".format(col)],
            bins = bounds, labels = label, include_lowest = True, right = True)

    return df