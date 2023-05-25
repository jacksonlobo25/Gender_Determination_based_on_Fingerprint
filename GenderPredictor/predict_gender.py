import numpy as np
from skimage import io
from skimage.transform import resize
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.utils.vis_utils import plot_model

model = load_model("Model\model.h5")

def predict_gender(file_path):
    x_test = np.load("GenderPredictor\\x_test.npy")
    y_test = np.load("GenderPredictor\\y_test.npy")
    fingerprint = io.imread(file_path, as_gray=True)
    fingerprint = resize(fingerprint, (96, 96))
    fingerprint = fingerprint.reshape(1, 96, 96, 1)
    fingerprint = fingerprint.astype('float32') / 255.0

    predict_x = model.predict(fingerprint) 
    val = str(predict_x[0][0])
    N = len(val)
    if N<10:
        gender = 'Male'
    else:
        gender = 'Female'
    print
    #accuracy = model.evaluate(x_test, y_test)[1]
    return f"Predicted gender is {gender}", "#1F618D", ("Helvetica", 18)


