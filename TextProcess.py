#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:58:23 2019

@author: m1ghtfr3e
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import string
from gensim.summarization import summarize
import string

# opening and reading the file (input)
filename = input("enter your filename here:  ")
f = open(filename)
File = f.read()

token = nltk.tokenize.word_tokenize(File)
predicate = lambda x:x not in string.punctuation
Token = list(filter(predicate, token))
print("\n Your text has {} characters \n".format(len(Token)))

# #pos tag the text (based on Token)
Tag = nltk.pos_tag(Token)

StopWords = set(stopwords.words('german'))
Text_sansst = nltk.FreqDist(w.lower() for w in Token if w not in 
                            StopWords)
Text_sans_stop = list(Text_sansst.keys())

TextSum = summarize(File)

fdist = nltk.FreqDist(Tag)
Most_word = fdist.most_common(20)
print("\n See an overview of your most used words:  \n", Most_word)

fdist.plot(10)

see_sum = input("\n Wanna get an overview of your text?")
if see_sum == 'yes':
    print("\n", TextSum)
else:
    print("ciao")


f.close()
