from collections import Counter
from string import punctuation
import pandas as pd
import numpy as np
import json
import nltk

class Indexer:

    def __init__(self, parsed):
        self.stemmer = nltk.stem.RSLPStemmer()
        self.parsed = parsed
        
    def get_index(self, attr = None, stopwords_enabled = True, stemming_enabled = True):
        inverted_index = {}
        i = 0
        dictionary = list(punctuation)
        if stopwords_enabled:
            dictionary += list(nltk.corpus.stopwords.words('portuguese'))
        for idx in self.parsed:
            idx = idx.lower()
            idx = ''.join([i for i in idx if not i.isdigit() and i not in list(punctuation)])
            text = idx.split()
            if stemming_enabled:
                text = [((attr+'.') if attr else '')+self.stemmer.stem(t) for t in text if t not in dictionary]
            else:
                text = [((attr+'.') if attr else '')+t for t in text if t not in dictionary]
            freq = Counter(text)
            for word in freq:
                if word not in inverted_index:
                    inverted_index[word] = {}
                inverted_index[word][i] = freq[word]
            i += 1
        return inverted_index

    # review this
    def compress_index(self):
        inverted_index = {}
        i = 0
        
        for idx in self.parsed:
            text = idx.split()
            freq = Counter(text)
            for word in freq:
                inverted_index[word].append((i, freq[word]))
            i += 1
        for word in inverted_index:
            inverted_index[word].sort(reverse=False)
            interval = []
            prev = 0
            acc = 0
            for x in inverted_index[word]:
                acc = x[0] - prev
                prev = x[0]
                interval.append((acc, x[1]))
            inverted_index[word] = interval
        return inverted_index