import numpy as np
from scipy.signal import convolve2d



"""
this function performs a 4:2:0 
chromiance subsampling.
"""
def sample(y, cr, cb):
    # normalizing
    # channel values should be normalized, hence subtract 128
    y = y - 128
    cr = cr - 128
    cb = cb - 128
    
    # define subsampling factors in both horizontal and vertical directions
    SSH, SSV = 2, 2

    # creating a 2x2 kernal
    kernel = np.array([[0.25, 0.25], [0.25, 0.25]])

    # subsampling
    cr = np.repeat(np.repeat(convolve2d(cr, kernel, mode='valid')[::SSV,::SSH], 2, axis=0), 2, axis=1)
    cb = np.repeat(np.repeat(convolve2d(cb, kernel, mode='valid')[::SSV,::SSH], 2, axis=0), 2, axis=1)

    return y, cr, cb
