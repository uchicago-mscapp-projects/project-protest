import pandas as pandas
import re  
import nltk  
# nltk.download('stopwords')
from nltk.corpus import stopwords  
import numpy as np
from gensim.models import Word2Vec  
import pandas as pd
from nltk.stem.porter import *  
stemmer = PorterStemmer()  
# nltk.download('punkt')
# Monica # 

def word_similarity():
    # upload text
    df = pd.read_csv('/home/monican/capp30122/30122-project-project-protest/project_protests/clean_data/raw_data/nyt_articles.csv')
    fake_text = df['lead_paragraph'].str.cat(sep=' ')
    # for row in df.iterrows()
    # fake_text = df.iloc[500]['lead_paragraph']
    fake_text = fake_text.lower()
    # fake_text_split = fake_text.split()
    

    # clean text
    # processed_text = fake_text_split.lower()
    # print(fake_text_split)
    processed_text = re.sub('[^a-zA-Z]', ' ', fake_text)
    processed_text = re.sub(r'\s+', ' ', processed_text)
    # print("PROCESSED TEXT: ", processed_text)
    # processed_text = processed_text.split()
    sentences = nltk.sent_tokenize(processed_text)
    # print("SENTENCES: ", sentences)
    words = [nltk.word_tokenize(sent) for sent in sentences]
    # print("WORDS: ", words)
    for i in range(len(words)):
        words[i] = [w for w in words[i] if w not in stopwords.words('english')]

    # print(words)
    word2vec = Word2Vec(words, min_count = 100)
    # vocab = word2vec.wv.index_to_key
    # print("VOCAB: ", vocab)

    # v1 = word2vec.wv['legal']
    sim_words = word2vec.wv.most_similar('police')
    print(sim_words)
    return None
# model = word2vec.Word2Vec(fake_text_split, vector_size=100, window=5, min_count=10, workers=4)  
