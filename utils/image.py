from PIL import Image
import numpy as np



"""
This function reads an image into an numpy array
"""
def read_image_file(path):
    # Opening the image file
    pic = Image.open(path, 'r')
    width, height = pic.size

    return np.asarray(pic), width, height   # returning the image as array with image size


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
