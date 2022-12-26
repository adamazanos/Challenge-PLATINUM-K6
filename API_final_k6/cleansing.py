import pandas as pd
import re

df_slang = pd.read_csv(r"https://raw.githubusercontent.com/adamazanos/Challenge-PLATINUM-K6/master/twitter_abuse/new_kamusalay.csv", encoding='latin=1', header=None)
df_slang = df_slang.rename(columns={0: 'slang', 1: 'formal'})

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
list_stopwords = set(stopwords.words('indonesian'))

def data_cleaning (tweet):
    #Replace enter
    c1 = re.sub ('\\n','', tweet)
    #Replace RT tag in tweet
    c2 = re.sub ('RT',' ', c1)
    #Replace mention username in tweet
    c3 = re.sub ('USER', ' ', c2)
    #Replace URL (http:// or https://) in tweet
    c4 = re.sub ('(http|https):\/\/s+', ' ', c3)
    #Replace punctuation
    c5 = re.sub ('[^0-9a-zA-Z]+', ' ', c4)
    #Replace emoticon
    c6 = re.sub ('x[a-z0-9]{2}', ' ', c5)
    #Replace Number
    c7 = re.sub ("\d+", ' ', c6)
    #Replace extra space
    c8 = re.sub ('  +', '', c7)
    return c8

def case_folding (tweet):
    return tweet.lower()

def slang_normalization(tweets):
    res = ''
    for item in tweets.split():
        if item in df_slang['slang'].values:
            res += df_slang[df_slang['slang'] == item]['formal'].iloc[0]
        else:
            res += item
        res += ' '
    return res

def stopword_removal(tweet):
    resp = ''
    for item in tweet.split():
        if item not in list_stopwords:
            resp += item
        resp +=' '
    clean = re.sub('  +', ' ', resp)
    return clean

def data_prepocessing(tweet):
    tweet = data_cleaning(tweet)
    tweet = case_folding(tweet)
    tweet = slang_normalization(tweet)
    tweet = stopword_removal(tweet)
    return tweet
