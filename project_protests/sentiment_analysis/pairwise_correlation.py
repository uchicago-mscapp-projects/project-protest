import pandas as pandas
import re  
import nltk
nltk.download([
"punkt", "stopwords"
])  
from nltk.corpus import stopwords  
import numpy as np
from gensim.models import Word2Vec  
import pathlib
import pandas as pd

# Monica Nimmagadda # 

def word_similarity(term):
    '''
    This function reads news data, calls the clean function, and creates a 
    Word2Vec model for each year of data as it relates to police and 
    Black Lives Matter. The function then creates a visualization of the combined
    data.

    Input: term (string) - the term we are looking for similarity
    Output: 2x3 chart with top 10 words per year and their corresponding
    similarity score
    '''
    nyt_filepath = pathlib.Path(__file__).parent.parent / "newspaper/nyt/raw_data/nyt_articles.csv"
    df = pd.read_csv(nyt_filepath)
    guardian_filepath = pathlib.Path(__file__).parent.parent / "newspaper/the_guardian/data/the_guardian_compiled.csv"
    df_nyt = pd.read_csv(guardian_filepath)
    df['year'] = pd.DatetimeIndex(df['date']).year
    df_nyt['year'] = pd.DatetimeIndex(df_nyt['date']).year
    df = pd.concat([df, df_nyt])
    years = sorted(df['year'].unique())
    visualization_df = []
    for year in years:
        articles_text = df.loc[df['year']==year]['lead_paragraph'].str.cat(sep=' ')
        text = clean(articles_text)
        if year == 2017:
            word2vec = Word2Vec(text, min_count = 3, window=5)
        elif year == 2023:
            continue
        else:
            word2vec = Word2Vec(text, min_count = 10, window=5)
        similar_words = word2vec.wv.most_similar(positive=[term], topn=15)
        for word, score in similar_words:
            visualization_df.append((word, score, year))
    
    return visualization_df

def clean(text):
    '''
    This function cleans the leading paragraph text from the news articles passed in.
    It also removes english stop words as defined by NLTK and adds in common
    meaningless words.
    '''
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    # splits a paragraph into sentences
    sentences = nltk.sent_tokenize(text)
    # splits a sentence into words
    words = [nltk.word_tokenize(sent) for sent in sentences]
    # removes stop words
    additional_stop_words = ['way', 'come', 'came', 'new', 'york', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'often', 'accross', 'knows', 'known', 'weeks', 'would', 'should', 'still', 'more', 'many', 'know', 'said', 'says', 'also', 'want', 'make', 'one', 'two', 'four', 'three', 'took', 'already', 'may', 'look', 'who', 'whose', 'get', 'take', 'like', 'including', 'include', 'more', 'much', 'first', 'week', 'day', 'recently','year','years']
    stop_words = stopwords.words('english') + additional_stop_words
    for i in range(len(words)):
        words[i] = [w for w in words[i] if w not in stop_words and len(w) > 2]
    return  words


