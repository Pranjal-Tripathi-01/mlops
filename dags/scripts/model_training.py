import tensorflow as tf
from joblib import dump
import os
from scripts.data_preprocess import data_preprocessing

X_train, X_test, y_train, y_test= data_preprocessing()


def training_model():
    cnn = tf.keras.Sequential([
        tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(240, 240, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2), padding='valid'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    cnn.compile (
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy'])

    cnn.fit(X_train, y_train, epochs=5)
    dump(cnn, f'{os.getcwd()}/model/model.joblib')
    cnn.predict(X_test)

