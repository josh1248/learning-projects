import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

from .generate_data import generateTrainingData

def train_model():
    print("training model now...")

    inputs, outputs = generateTrainingData()

    train_inputs, val_inputs, train_outputs, val_outputs = train_test_split(np.array(inputs), np.array(outputs), test_size=0.7, random_state=42)

    model = Sequential([
        Dense(128, input_dim=9, activation='relu'),  # Input layer with 9 inputs
        Dense(128, activation='relu'),               # Hidden layer
        Dense(9, activation='softmax')               # Output layer with 9 outputs for the 9 possible moves
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

    model.fit(train_inputs, train_outputs, validation_data=(val_inputs, val_outputs), epochs=100)

    print("model trained.")

    return model

def select_move(model, board: list[int]):
    print('oh')
    prediction = model.predict(np.array(board))
    print(prediction)
    return np.argmax(prediction)

