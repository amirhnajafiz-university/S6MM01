from PIL import Image
import numpy as np


"""
This function creates an image from input numpy array
"""
def create_image(im):
    return Image.fromarray((np.asarray(im) * 255).astype(np.uint8))


"""
This function saves our image
"""
def save_image(im, name):
    Image.fromarray((np.asarray(im) * 255).astype(np.uint8)).save(name)
