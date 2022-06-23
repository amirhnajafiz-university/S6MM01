from PIL import Image
import numpy as np


"""
This method creates an image from input numpy array
"""
def create_image(im):
    return Image.fromarray((np.asarray(im) * 255).astype(np.uint8))
