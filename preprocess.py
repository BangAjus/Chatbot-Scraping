import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy
import numpy as np
from pickle import load
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

nltk.download('stopwords')

def clean_corpus(text):

    stop_words = stopwords.words('english')
    ps = PorterStemmer()
    nlp = spacy.load('en_core_web_sm')

    text = text.lower()
    text = re.findall(r'[a-z]+', text)

    text = [i for i in text if i not in stop_words]

    text = nlp(" ".join(text))
    text = [i.lemma_ for i in text]

    text = [ps.stem(i) for i in text]

    return " ".join(text)

maxlen = 5

def preprocessing(text,
                  maxlen=maxlen):
    
    tokenizer = load(open('Model Cooking/tokenizer.pkl', 'rb'))

    text = clean_corpus(text)
    text = tokenizer.texts_to_sequences([text])
    text = np.array(text).reshape(-1)
    text = pad_sequences([text], maxlen=maxlen)

    return text