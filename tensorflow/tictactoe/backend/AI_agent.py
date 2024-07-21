import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from .generate_data import generateTrainingData

def train_model():
    print("training model now...")

    train_inputs, train_outputs, test_inputs, test_outputs = (np.array(arr) for arr in generateTrainingData(training_data_proportion=0.7))

    model = Sequential([
        Dense(128, input_dim=9, activation='relu'),  # Input layer with 9 inputs
        Dense(128, activation='relu'),               # Hidden layer
        Dense(128, activation='relu'),               # Hidden layer
        Dense(9, activation='softmax')               # Output layer with 9 outputs for the 9 possible moves
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_inputs, train_outputs, validation_data=(test_inputs, test_outputs), epochs=100)

    print("model trained.")

    return model

def select_move(model, board: list[int]):
    # https://stackoverflow.com/questions/45499757/expected-shape-none-8-but-got-array-with-shape-8-1
    prediction = model.predict(np.array([np.array(board)]).reshape(1, 9))
    return int(np.argmax(prediction)), np.ndarray.tolist(prediction)

