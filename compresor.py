from distutils import extension
from pickletools import optimize
from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "C:\Users\diego\Downloads"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "comprimido" + filename, optimize = True, quality = 60)