import pprint
from random import randint

import numpy as np
import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.text import Tokenizer

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


def tokenize_data(patterns, responses):
    tokenizer_ = Tokenizer(num_words=100)
    tokenizer_.fit_on_texts(patterns[0])
    for i in range(len(patterns[1])):
        tokenizer_.fit_on_texts(patterns[1][i])
        tokenizer_.fit_on_texts(responses[1][i])
    return tokenizer_, tokenizer_.word_index

def tokenize_sequences(patterns, responses, tokenizer_):
    for i in range(len(patterns[1])):
        patterns[1][i] = tokenizer_.texts_to_sequences(patterns[1][i])
        responses[1][i] = tokenizer_.texts_to_sequences(responses[1][i])
    return patterns, responses


df = open_json_and_make_df()
X, y = extract_data(df)
tokenizer, word_index = tokenize_data(X, y)
X, y = tokenize_sequences(X, y, tokenizer)
