import json
from  collections import defaultdict
from collections import Counter
import nltk
import os
import time
import pandas as pd
import numpy as np

def query(name, inv_indx):
    names = name.split()
    query = []
    data = {}
    for i in names:
        for j in inv_indx[i]:
            if j[1] not in data:
                data[j[1]] = j[0]
            else:
                data[j[1]] += j[0]
    answer = sorted(data, key=data.__getitem__, reverse = True)
    return answer