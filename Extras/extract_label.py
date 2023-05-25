import os

image_dir = "DATASET\SOCOFing\Real"

def get_gender_from_filename(filename):
    parts , etc = filename.split("__")
    gender_code = etc[0]
    gender = "Male" if gender_code == "M" else "Female"
    return gender

with open("genders.txt", "w") as f:
    for filename in os.listdir(image_dir):
        if filename.endswith(".BMP"):
            gender = get_gender_from_filename(filename)
            f.write(filename + " " + gender + "\n")
