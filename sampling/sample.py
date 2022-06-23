import numpy as np


"""
This method performs a Chroma Subsampling
"""
def chroma_subsampling(x, ratio='4:2:0'):
    # No subsampling
    if ratio == '4:4:4':
        return x
    else:
        out = np.zeros((x.shape))
        # Downsample with a window of 2 in the horizontal direction
        if ratio == '4:2:2':
            for i in range(0, x.shape[0], 2):
                out[i:i+2] = np.mean(x[i:i+2], axis=0)
        # Downsample with a window of 2 in both directions
        else:
            for i in range(0, x.shape[0], 2):
                for j in range(0, x.shape[1], 2):
                    out[i:i+2, j:j+2] = np.mean(x[i:i+2, j:j+2])
        return np.round(out).astype('uint8')
