#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:50:50 2019

@author: m1ghtfr3e
"""
import nltk
from nltk.corpus import stopwords
from gensim.summarization import summarize

print("""Welcome to this Text Analyzer. The functions
      are still quite basic and might be not too useful
      right now as not all modules work very well.
      code of this program will be edited and updated
      continously...
Overview of options and how to enter them:
     [keys behind the advice are commands to use]
> see the most used words in your text (mw)

> look for a keyword in your text (skey)

> get a summarazation of the text (sumt)
""")

# open text file and make corpus out of it
filename = input("please enter name of your file:  ")
f = open(filename)
text = f.read()
text_s = text.split()
Text = nltk.Text(text_s)

Count_text = int(len(Text))
print("\n", Count_text, "\n")


# set stopwords and remove from text
def stopWord():
    global Text_sansst
    StopWords = set(stopwords.words('german'))
    Text_sansst = nltk.FreqDist(w.lower() for w in Text if w not in
                                StopWords)
    Text_sans_stop = Text_sansst.keys()
    return print(Text_sans_stop)


# get frequency of text without stopwords
def mostWord():
    global Mostwords
    Mostwords = nltk.FreqDist(Text_sansst)
    Mosttext = Mostwords.most_common(15)
    print(Mosttext)
    return Mostwords.plot(15)


# pos-tag the text .. based on Mostwords
def tagWord():
    Tag = nltk.pos_tag(Mostwords)
    print(Tag)


# get concordance of a specific word
def concWord():
    Keyword = input("Put in your Keyword:  ")
    Con = Text.concordance(Keyword)
    print("\n", Con, "\n")


# text summarazation
def sumWord():
    sumText = summarize(text)
    print("\n", sumText)


def main():

    opt = input("choose your action: ")
    if opt == 'mw':
        mostWord()
        return
    if opt == 'skey':
        concWord()
        return
    if opt == 'sumt':
        sumWord()
        return
    else:
        ("..bye...")


while True:
    main()


f.close()
