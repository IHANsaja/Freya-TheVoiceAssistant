import random
import pickle
import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

# Initialize the lemmatizer
lem = WordNetLemmatizer()

# Load intents from the JSON file
with open('data.json') as file:
    intents = json.load(file)

# Initialize empty lists for words, classes, and training data
words = []
classes = []
training_data = []

# Iterate through each intent
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize and lemmatize each word in the pattern
        words.extend(nltk.word_tokenize(pattern))
        training_data.append((pattern, intent['tag']))

    if intent['tag'] not in classes:
        classes.append(intent['tag'])

# Lemmatize words and remove duplicates
words = [lem.lemmatize(word.lower()) for word in words if word.isalnum()]
words = sorted(set(words))

# Save words and classes as pickled files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Create the training dataset
X_train = []
y_train = []

for pattern, tag in training_data:
    bag = [1 if lem.lemmatize(word.lower()) in pattern.lower() else 0 for word in words]
    X_train.append(bag)

    output = [0] * len(classes)
    output[classes.index(tag)] = 1
    y_train.append(output)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Create and compile the model with updated optimizer
model = Sequential()
model.add(Dense(128, input_shape=(len(X_train[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]), activation='softmax'))

# Use the updated optimizer configuration
optimizer = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)

# Save the trained model
model.save('Freya v2.11.h5')
print("Model trained and saved!")