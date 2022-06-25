import numpy as np
from math import ceil

from .padding import give_padding
from .dct import perform_dct



# define quantization tables
# luminance quantization table
QTY = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 48, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

# chrominance quantization table
QTC = np.array([
    [17, 18, 24, 47, 99, 99, 99, 99],  
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99]
])

"""
this method performs a quantization on our matrix
and returns the values.
"""
def quantize(y, cr, cb):
    # define window size
    windowSize = len(QTY)

    # padding
    y, cr, cb, yWidth, yLength, cWidth, cLength = give_padding(y, cr, cb, windowSize)

    # performing a dct on blocks
    yDct, crDct, cbDct = perform_dct(y, cr, cb, yWidth, yLength, cWidth, cLength, windowSize)

    # define 3 empty matrices to store the quantized values
    yq, crq, cbq = np.zeros((yLength, yWidth)), np.zeros((cLength, cWidth)), np.zeros((cLength, cWidth))

    # number of iteration on x axis and y axis to calculate the luminance cosine transform values
    hbY = int(len(yDct[0]) / windowSize)  # number of blocks in the horizontal direction for luminance
    vbY = int(len(yDct) / windowSize)  # number of blocks in the vertical direction for luminance
    # number of iteration on x axis and y axis to calculate the chrominance channels cosine transforms values
    hbC = int(len(crDct[0]) / windowSize)  # number of blocks in the horizontal direction for chrominance
    vbC = int(len(crDct) / windowSize)  # number of blocks in the vertical direction for chrominance

    for i in range(vbY):
        for j in range(hbY):
            yq[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = np.ceil(
                yDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] / QTY
            )

    # either crq or cbq can be used to compute the number of blocks
    for i in range(vbC):
        for j in range(hbC):
            crq[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = np.ceil(
                crDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] / QTC
            )
            cbq[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = np.ceil(
                cbDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] / QTC
            )
    
    print(f'[INFO] Total number of operations: {vbC * hbC + vbY * hbY}')
    
    return yq, crq, cbq, windowSize
