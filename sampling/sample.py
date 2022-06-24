import numpy as np
from scipy.signal import convolve2d


"""
This method performs a Chroma Subsampling
"""
def chroma_subsampling(x, ratio='4:2:0'):
    # No subsampling
    if ratio == '4:4:4':
        return x
    else:
        # Downsample with a window of 2 in the horizontal direction
        if ratio == '4:2:2':
            kernel = np.array([[0.5], [0.5]])
            out = np.repeat(convolve2d(x, kernel, mode='valid')[::2,:], 2, axis=0)
        # Downsample with a window of 2 in both directions
        else:
            kernel = np.array([[0.25, 0.25], [0.25, 0.25]])
            out = np.repeat(np.repeat(convolve2d(x, kernel, mode='valid')[::2,::2], 2, axis=0), 2, axis=1)
        return np.round(out).astype('int')
