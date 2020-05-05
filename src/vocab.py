#!/bin/python3
from utils.reader import extract_text as et
from utils.tokenizer import hindi_tokenizer as ht

def preprocess_corpus(path_to_corpus):
    strings = et(path_to_corpus)
    sentences = ht(strings)
    return sentences

sentences = preprocess_corpus('utils/output.hi')
d = {}
for sentence in sentences:
    for token in sentence:
        try:
            d[token]+=1
        except:
            d.update({token:1})

import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

tmp = []
f = open('vocab.txt', 'w')
for d in sorted_d:
    tmp = [d[0]]+tmp

for token in tmp:
    print(token, file = f)
