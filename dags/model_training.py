
import tensorflow as tf
from joblib import dump
import os
from data_preprocess import data_preprocessing
from logger_config import logger

preprocessed_data = data_preprocessing()
X_train, X_test, y_train, y_test = preprocessed_data['X_train'], preprocessed_data['X_test'], preprocessed_data['y_train'], preprocessed_data['y_test']

def training_model():
    try:
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
        logger.info("Model Training Completed")
        dump(cnn, 'model.joblib')
        cnn.predict(X_test)
    except Exception as e:
        logger.error(f"Error in load data: {e}")



