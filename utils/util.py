from PIL import Image
import numpy as np


def read_image_file(path):
    # Opening the image file
    pic = Image.open(path, 'r')
    width, height = pic.size

    return np.asarray(pic), width, height   # returning the image as array with image size
