import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/01. BINAR CHALLANGE 01/abuse word twitter data/data.csv', encoding='latin-1')
#alay_dict = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/01. BINAR CHALLANGE 01/abuse word twitter data/new_kamusalay.csv', names = ['original', 'replacement'], encoding='latin-1')
#abusive_dict = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/01. BINAR CHALLANGE 01/abuse word twitter data/abusive.csv', encoding='latin-1')

#A. Cek Data Manual
#data
data.head(25)
data.tail(11)
abusive_dict
alay_dict

#B.Prep example on Day 1
#Sentence Tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text = "Barangnya lumayan, cuma yang saya heran xiaomi redmi note 2 ini tombol onnya memang agak rusak? Terus baterai memang cepat low bat juragan?"
text = sent_tokenize(text)
text #test output

#Word Tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "Barangnya lumayan, cuma yang saya heran xiaomi redmi note 2 ini tombol onnya memang agak rusak? Terus baterai memang cepat low bat juragan?"
text = word_tokenize(text)
text #test output
