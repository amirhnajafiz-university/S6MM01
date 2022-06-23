from PIL import Image
import numpy as np
from utils.reader import read_image_file
from converter.convert import rgb2ycbcr


if __name__ == "__main__":
    path = input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')

    pix = rgb2ycbcr(pix)

    img = Image.fromarray((np.asarray(pix) * 255).astype(np.uint8))
    img.show()
