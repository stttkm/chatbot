from random import randint

import numpy as np
import pandas as pd

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import SGD

import json

json_file = open('data/intents.json')
data = json.load(json_file)
df = pd.json_normalize(data["intents"])

X = np.array([df['tag'], df['patterns']])
y = np.array([df['tag'], df['responses']])
