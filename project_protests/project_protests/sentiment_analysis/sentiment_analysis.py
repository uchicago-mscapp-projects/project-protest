import pandas as pandas
import nltk
nltk.download([
"vader_lexicon",
])
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

##Author: JP Martinez
##Task: Perform sentiment analysis on news dataframe
##Last date updated: 02.27.23

words_to_update = {
    "protest": 0, "murder": 0, "brutality": 0
}

def edit_sentiment_dictionary(update_dict = words_to_update):
    """
    Edit sentiment dictionary to exclude certain words that are common and
    neutral in the context but that the nltk dictionary classifies as negative
    """
    sia.lexicon.update(update_dict)

def sentiment_scores(df, columns_list):
    """
    Calculate sentiment scores for the headline and lead sections of the news
    retrieve by The New York Times and The Guardian API's.
    Inputs:
     - df: Dataframe
    
    Returns:
    df : Updated df with new columns that classify the sentiment of the given columns

    """
    edit_sentiment_dictionary()

    for col in columns_list:
        if "{}".format(col) in df.columns:
            df["{}_score".format(col)] = df["{}".format_col].apply(lambda x:
            sia.polarity_scores(x)["compound"])
            df["{}_sentiment".format(col)] = np.select([df["{}_score".format(col)] < 0, 
            df["{}_score".format(col)] == 0, df["{}_score".format(col)] > 0],[-1, 0, 1])

    return df
    

