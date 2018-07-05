import json
from  collections import defaultdict
from collections import Counter
import nltk
import os
import time
import pandas as pd
import numpy as np

stemmer = nltk.stem.RSLPStemmer()

def index(parsed):
    inv_indx = defaultdict(list)
    i = 0
    for idx in parsed:
        text = idx.split()
        freq = Counter(text)
        for word in freq:
            inv_indx[word].append((freq[word], i))
        i += 1
        
    for word in inv_indx:
        inv_indx[word].sort(reverse=True)
    return inv_indx

def compressIndex(parsed):
    inv_indx = defaultdict(list)
    i = 0
    for idx in parsed:
        text = idx.split()
        freq = Counter(text)
        for word in freq:
            inv_indx[word].append((i, freq[word]))
        i += 1
        
    for word in inv_indx:
        inv_indx[word].sort(reverse=False)
        interval = []
        prev = 0
        acc = 0
        for x in inv_indx[word]:
            acc = x[0] - prev
            prev = x[0]
            interval.append((acc, x[1]))
        inv_indx[word] = interval
    return inv_indx

def transformJson(self, name, inv_indx):
    file = name+'.txt';
    with  open(file, 'w') as outfile:  
        json.dump(inv_indx, outfile)