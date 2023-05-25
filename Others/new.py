import os
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

data_dir = "Training\\Train\\"
model_path = "Others/model.h5"

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(96, 96, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

def extract_gender(filename):
    if filename.split("__")[1][0] == "M":
        return 1  # male
    else:
        return 0  # female

X = []
y = []
for filename in os.listdir(data_dir):
    if filename.endswith(".BMP"):
        img = tf.keras.preprocessing.image.load_img(
            os.path.join(data_dir, filename), target_size=(96, 96)
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        X.append(img_array)
        y.append(extract_gender(filename))

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print("Test accuracy:", test_acc)

history_dict = {
    "accuracy": history.history["accuracy"],
    "loss": history.history["loss"],
    "val_accuracy": history.history["val_accuracy"],
    "val_loss": history.history["val_loss"],
}

model.save(model_path)
np.save("Extras/history.npy", history_dict)
