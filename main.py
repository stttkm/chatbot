import pprint
from random import randint

import numpy as np
import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.text import Tokenizer

import json

json_file = open('data/intents.json')
data = json.load(json_file)
df = pd.json_normalize(data["intents"])

X = np.array([df['tag'], df['patterns']])
y = np.array([df['tag'], df['responses']])

tokenizer = Tokenizer(num_words=100)


for i in range(len(X[1])):
    tokenizer.fit_on_texts(X[1][i])
    word_index = tokenizer.word_index
