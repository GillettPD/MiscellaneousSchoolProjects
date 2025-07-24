#Paul Gillett
#LING 5200
#Homework 4

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request



url = "https://languagelog.ldc.upenn.edu/nll/?p=48725"
html = request.urlopen(url).read().decode('utf8')

from bs4 import BeautifulSoup
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)

#print tokens
print("first 25 tokens: \n")
print(tokens[:25])

#collocations
text = nltk.Text(tokens)
print('\n', "collocations:")
print(text.collocations())


#lemmatize
wnl = nltk.WordNetLemmatizer()
lemma_list = [wnl.lemmatize(t) for t in tokens]
print("first 50 lemmas:", '\n')
print(lemma_list[:50])
