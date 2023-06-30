import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Conv2D, Input, Dense, MaxPool2D, BatchNormalization, GlobalAvgPool2D
import pandas as pd

df = pd.read_csv("D:/mnist/mnist_train.csv", encoding="utf-8")
X = df.iloc[:, 1:].values.reshape(-1, 28, 28, 1)
y = df.iloc[:, 0]
print(len)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    Input(shape=(28,28,1)),
    Conv2D(32, (3,3), activation="relu"),
    Conv2D(64, (3,3), activation="relu"),
    MaxPool2D(),
    BatchNormalization(),

    Conv2D(128, (3,3), activation="relu"),
    MaxPool2D(),
    BatchNormalization(),
    
    GlobalAvgPool2D(),
    Dense(64, activation="relu"),
    Dense(64, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")
model.fit(X_train, y_train, batch_size=64, epochs=3, validation_split=0.2)
model.evaluate(X_test, y_test, batch_size=64)

model.save("nlp_model.h5")

