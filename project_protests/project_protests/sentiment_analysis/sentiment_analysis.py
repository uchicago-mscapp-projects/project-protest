##Author: JP Martinez
##Task: Perform simple sentiment analysis on news dataframe
##Last date updated: 03.01.23

import pandas as pandas
import os
import nltk
import numpy as np
nltk.download([
"vader_lexicon",
])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

BOUNDS = {"classifier": ([-1,0,1],["negative","positive"])}
WORDS_TO_UPDATE = {
    "protest": 0, "brutality": 0
}


def edit_sentiment_dictionary(update_dict = words_to_update):
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

    

