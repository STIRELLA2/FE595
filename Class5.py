# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import redis

from flask import Flask
python get-pip.py

from pip import nltk
from zacktools import pageparser

from nltk.util import ngrams
from nltk import word_tokenize
from nltk import pos_tag

import nltk
nltk.download('averaged_perceptron_tagger')
  
pip install nltk
import nltk
nltk.download('punkt')
  

@app.route('/')
def hello():
    count=get_hit_count()
    with open("greeting.txt","r") as fh:
        greeting_text = fh.read()
    return f"{greeting_text} {count} times."

if __name__ == "main":
    
#n-gram
    
def extract_ngrams(text,num):
    n_grams = ngrams(nltk)

text = word_tokenize("There are deer.")

text


pos_tag(text)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
