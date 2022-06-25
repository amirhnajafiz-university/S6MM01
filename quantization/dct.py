import numpy as np
from scipy.fftpack import dct



"""
this function performs a 2D DCT
and returns the YCrCb.
"""
def perform_dct(y, cr, cb, yWidth, yLength, cWidth, cLength, windowSize):
    # get DCT of each channel
    # define three empty matrices
    yDct, crDct, cbDct = np.zeros((yLength, yWidth)), np.zeros((cLength, cWidth)), np.zeros((cLength, cWidth))

    # number of iteration on x axis and y axis to calculate the luminance cosine transform values
    hbY = int(len(yDct[0]) / windowSize)  # number of blocks in the horizontal direction for luminance
    vbY = int(len(yDct) / windowSize)  # number of blocks in the vertical direction for luminance
    # number of iteration on x axis and y axis to calculate the chrominance channels cosine transforms values
    hbC = int(len(crDct[0]) / windowSize)  # number of blocks in the horizontal direction for chrominance
    vbC = int(len(crDct) / windowSize)  # number of blocks in the vertical direction for chrominance

    for i in range(vbY):
        for j in range(hbY):
            yDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = dct(
                y[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize],
                norm='ortho'
            )
    
    # either crq or cbq can be used to compute the number of blocks
    for i in range(vbC):
        for j in range(hbC):
            crDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = dct(
                cr[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize],
                norm='ortho'
            )
            cbDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = dct(
                cb[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize],
                norm='ortho'
            )
            
    return yDct, crDct, cbDct
