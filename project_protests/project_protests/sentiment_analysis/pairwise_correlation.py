import pandas as pandas
import re  
import nltk  
from nltk.corpus import stopwords  
import numpy as np
from gensim.models import Word2Vec  
import pandas as pd
import plotly.express as px
from nltk.stem.porter import *  
from plotly.subplots import make_subplots
stemmer = PorterStemmer()  

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
    df = pd.read_csv('/home/monican/capp30122/30122-project-project-protest/project_protests/clean_data/raw_data/nyt_articles.csv')
    df_nyt = pd.read_csv('/home/monican/capp30122/30122-project-project-protest/project_protests/project_protests/api_requests/the_guardian/data/the_guardian_compiled.csv')
    df['year'] = pd.DatetimeIndex(df['date']).year
    df_nyt['year'] = pd.DatetimeIndex(df_nyt['date']).year
    df.merge(df_nyt[['year', 'lead_paragraph']])
    years = [2017, 2018, 2019, 2020, 2021, 2022]
    visualization_df = []
    for year in years:
        articles_text = df.loc[df['year']==year]['lead_paragraph'].str.cat(sep=' ')
        text = clean(articles_text)
        if year == 2017:
            word2vec = Word2Vec(text, min_count = 3, sg=1, window=7)
        else:
            word2vec = Word2Vec(text, min_count = 10, sg=1, window=7)
        similar_words = word2vec.wv.most_similar(positive=[term], topn=10)
        for word, score in similar_words:
            visualization_df.append((word, score, year))
    visualize_simiilarity(visualization_df)
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
    additional_stop_words = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'often', 'accross', 'knows', 'known', 'weeks', 'would', 'should', 'still', 'more', 'many', 'know', 'said', 'says', 'also', 'want', 'make', 'one', 'two', 'four', 'three', 'took', 'already', 'may', 'look', 'who', 'whose', 'get', 'take', 'like', 'including', 'include', 'more', 'much', 'first', 'week', 'day', 'recently','year','years']
    stop_words = stopwords.words('english') + additional_stop_words
    for i in range(len(words)):
        words[i] = [w for w in words[i] if w not in stop_words and len(w) > 2]
    return  words

def visualize_simiilarity(visualization_df):
    '''
    This function takes in the similarity words list and creates bar charts
    by year for each set of words and score. 
    The resulting plot is a 2x3 chart of each year 2017-2022 and their corresponding
    top words related to "police" as seen in NYT and the Guardian data.
    '''
    df = pd.DataFrame(visualization_df, columns=["word", "score", "year"])
    fig = make_subplots(rows=2,cols=3)
    for idx, year in enumerate(df['year'].unique()):
        chart = px.bar(df[df['year']==year], x="word", y="score", color='year')
        chart.update_layout(title_text=str(year), )
        if idx < 3:
            fig.append_trace(chart.data[0], row=1, col=idx+1)
        else:
            fig.append_trace(chart.data[0], row=2, col=(idx+1)-3)
    fig.show()
    return None
