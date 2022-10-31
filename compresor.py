from distutils import extension
from pickletools import optimize
from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/Users/Diego/Downloads/"
picturesFolder = "/Users/diego/OneDrive/Imágenes/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "comprimido_" + filename, optimize = True, quality = 60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]:
            musicFolder = "/Users/Diego/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
