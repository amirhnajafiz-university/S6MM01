import numpy as np 

"""
This function converts a RGB array to YCbCr
"""
def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)

    ycbcr[:,:,[1,2]] += 128

    return np.uint8(ycbcr)


"""
This function converts a YCbCr array to RGB
"""
def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)

    rgb[:,:,[1,2]] -= 128

    rgb = rgb.dot(xform.T)

    np.putmask(rgb, rgb > 255, 255)
    np.putmask(rgb, rgb < 0, 0)

    return np.uint8(rgb)
