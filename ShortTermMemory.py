# Tyler Koenig
# CS379 Machine Learning
# November 9, 2021
# Description: This algorithm will generate text based on a text file

# Libraries
import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

# Load File
dataset = r"C:\Users\Tyler\Downloads\alice_in_wonderland.txt"
rawText = open(dataset, 'r', encoding='utf-8').read()

# Convert to lowercase
rawText = rawText.lower()

# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(rawText)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# Summarize text file
n_chars = len(rawText)
n_vocab = len(chars)

print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# Prepare and encode dataset
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = rawText[i:i + seq_length]
    seq_out = rawText[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)

print("Total Patterns: ", n_patterns)

# Reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

# Normalize
X = X / float(n_vocab)

# One hot encode the output variable
y = np_utils.to_categorical(dataY)

# Define LTSM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

# Network Weights
dataset = "weights-improvement-19-1.9435.hdf5"
model.load_weights(dataset)
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Select random seed
start = numpy.random.randint(0, len(dataX) - 1)
pattern = dataX[start]
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")

# Generate Text
for i in range(1000):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(n_vocab)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    seq_in = [int_to_char[value] for value in pattern]
    sys.stdout.write(result)
    pattern.append(index)
    pattern = pattern[1:len(pattern)]
print("\nDone.")
