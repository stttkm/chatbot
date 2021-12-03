from random import randint

import numpy as np
import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence

import json


def open_json_and_make_df():
    json_file = open('data/intents.json')
    data = json.load(json_file)
    pandas_df = pd.json_normalize(data["intents"])
    return pandas_df

def extract_data(data_frame):
    patterns = np.array([data_frame['tag'], data_frame['patterns']])
    responses = np.array([data_frame['tag'], data_frame['responses']])
    return patterns, responses

def tokenize_data(*args):
    tokenizer_ = Tokenizer(num_words=200, filters='!"#$%&()*+,-./:;<=>?@[\\]^`{|}~\t\n')
    for data in args:
        tokenizer_.fit_on_texts(data)
    return tokenizer_, tokenizer_.word_index


def training_data(patterns):
    tmp = []
    num_of_words = [0]*len(patterns[1])
    for i in range(len(patterns[1])):
        tmp += list(patterns[1][i])
        for el in patterns[1][i]:
            num_of_words[i] += len(el.split())
    X_ = text_to_word_sequence(' '.join(tmp))
    y_ = []
    for i in range(len(patterns[1])):
        y_ += [patterns[0][i] for _ in range(num_of_words[i])]
    assert len(X_) == len(y_)
    return X_, y_


df = open_json_and_make_df()
patterns, responses = extract_data(df)
X, y = training_data(patterns)
tokenizer, word_index = tokenize_data(X, y)
X = tokenizer.texts_to_sequences(X)
y = tokenizer.texts_to_sequences(y)
