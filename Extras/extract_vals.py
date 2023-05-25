from skimage import io
from skimage.transform import resize
import numpy as np
import os

input_dir = "DATASET\SOCOFing\Real"
label_file = "Extras\genders.txt"

with open(label_file, 'r') as f:
    lines = f.readlines()

label_dict = {}
for line in lines:
    filename, label = line.strip().split()
    label_dict[filename] = label

x_test = []
y_test = []
for filename in os.listdir(input_dir):
    if filename.endswith(".BMP") or filename.endswith(".png"):
        img = io.imread(os.path.join(input_dir, filename), as_gray=True)
        img = resize(img, (96, 96))

        img = img.astype('float32') / 255.0
        x_test.append(img)
        y_test.append(label_dict[filename])

x_test = np.array(x_test)
y_test = np.array(y_test)

y_test = np.where(y_test == 'Male', 0, 1)

np.save("x_test.npy", x_test)
np.save("y_test.npy", y_test)
