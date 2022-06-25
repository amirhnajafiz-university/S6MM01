from rlc.iterate import zigzag

import numpy as np



"""
this function performs the zigzags on our matrix.
"""
def get_zigzags(y, cr, cb, windowSize):
    # number of iteration on x axis and y axis to calculate the luminance cosine transform values
    hbC = int(len(y[0]) / windowSize)  # number of blocks in the horizontal direction for luminance
    vbY = int(len(y) / windowSize)  # number of blocks in the vertical direction for luminance
    # number of iteration on x axis and y axis to calculate the chrominance channels cosine transforms values
    hbC = int(len(cr[0]) / windowSize)  # number of blocks in the horizontal direction for chrominance
    vbC = int(len(cr) / windowSize)  # number of blocks in the vertical direction for chrominance

    # and another 3 for the zigzags
    yZigzag = np.zeros(((vbY * hbC), windowSize * windowSize))
    crZigzag = np.zeros(((vbC * hbC), windowSize * windowSize))
    cbZigzag = np.zeros(((vbC * hbC), windowSize * windowSize))

    for i in range(vbY):
        for j in range(hbC):
            yZigzag[i * j] += zigzag(
                y[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize]
            )
    yZigzag = yZigzag.astype(np.int16)

    # either crq or cbq can be used to compute the number of blocks
    for i in range(vbC):
        for j in range(hbC):
            crZigzag[i * j] += zigzag(
                cr[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize]
            )
            cbZigzag[i * j] += zigzag(
                cb[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize]
            )
    crZigzag = crZigzag.astype(np.int16)
    cbZigzag = cbZigzag.astype(np.int16)

    return yZigzag, crZigzag, cbZigzag
