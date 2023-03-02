import pandas as pandas
import re  
import nltk  
from nltk.corpus import stopwords  
import numpy as np
from gensim.models import Word2Vec  
import pandas as pd
import plotly.express as px
from nltk.stem.porter import *  
import statistics
stemmer = PorterStemmer()  

# Monica # 

def word_similarity(term):
    # upload text
    df = pd.read_csv('/home/monican/capp30122/30122-project-project-protest/project_protests/clean_data/raw_data/nyt_articles.csv')
    df['year'] = pd.DatetimeIndex(df['date']).year
    years = df['year'].unique()

    for year in years:
        articles_text = df.loc[df['year']==year]['lead_paragraph'].str.cat(sep=' ')
        text = clean(articles_text)
        # mode = statistics.mode(text[0])
        word2vec = Word2Vec(text, min_count = 10)
        similar_words = word2vec.wv.most_similar(positive=[term], topn=30)
        visualize_simiilarity(similar_words, year)
    return None

def clean(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    # splits a paragraph into sentences
    sentences = nltk.sent_tokenize(text)
    # splits a sentence into words
    words = [nltk.word_tokenize(sent) for sent in sentences]
    # removes stop words
    for i in range(len(words)):
        words[i] = [w for w in words[i] if w not in stopwords.words('english')]
    return  words

def visualize_simiilarity(similar_words, year):
    title = str(year)
    df = pd.DataFrame(similar_words, columns=["word", "score"])
    hist = px.histogram(df, x="word", y="score",title=title)
    hist.update_layout(yaxis_range=[0.0, 1.0])
    # hist.update_layout(title_x: year)
    hist.show()
    return None
