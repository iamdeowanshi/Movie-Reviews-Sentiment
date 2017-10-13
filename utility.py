import re
import nltk
import numpy as np
from collections import Counter
from nltk.corpus import stopwords

WORD = re.compile(r'\w+')
WORD_LIST = stopwords.words('english')
extra_words = ['movie', 'movies','film', 'films','hollywood','series','scene','scene','characters','story']
WORD_LIST.extend(extra_words)

def preprocess(reviews):
    result = []
    for review in reviews:
        cleanedHtml = cleanhtml(review)
        text_vector = text_to_vector(cleanedHtml)
        preProcessedData = remove_stop_words(text_vector)
        result.append(preProcessedData)
    return  result

def remove_stop_words(words):
    result = []
    for word in words:
        if word not in WORD_LIST:
            result.append(word)
    return Counter(result)

def text_to_vector(text):
     words = WORD.findall(text)
     words = [item.lower() for item in words]
     return words

def stemmer(words):
    result = []
    for word in words:
        result.append(porter.stem(word))
    return result

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html).lower()
  return cleantext


