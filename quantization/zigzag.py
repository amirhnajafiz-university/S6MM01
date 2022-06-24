from rlc.iterate import zigzag



"""
this function performs the zigzags on our matrix.
"""
def get_zigzags(y, cr, cb, windowSize):
    # number of iteration on x axis and y axis to calculate the luminance cosine transform values
    hBlocksForY = int(len(y[0]) / windowSize)  # number of blocks in the horizontal direction for luminance
    vBlocksForY = int(len(y) / windowSize)  # number of blocks in the vertical direction for luminance
    # number of iteration on x axis and y axis to calculate the chrominance channels cosine transforms values
    hBlocksForC = int(len(cr[0]) / windowSize)  # number of blocks in the horizontal direction for chrominance
    vBlocksForC = int(len(cr) / windowSize)  # number of blocks in the vertical direction for chrominance

    # and another 3 for the zigzags
    yZigzag = np.zeros(((vBlocksForY * hBlocksForY), windowSize * windowSize))
    crZigzag = np.zeros(((vBlocksForC * hBlocksForC), windowSize * windowSize))
    cbZigzag = np.zeros(((vBlocksForC * hBlocksForC), windowSize * windowSize))

    for i in range(vBlocksForY):
        for j in range(hBlocksForY):
            yZigzag[i * j] += zigzag(
                y[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
    yZigzag = yZigzag.astype(np.int16)

    # either crq or cbq can be used to compute the number of blocks
    for i in range(vBlocksForC):
        for j in range(hBlocksForC):
            crZigzag[i * j] += zigzag(
                cr[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
            cbZigzag[i * j] += zigzag(
                cb[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
    crZigzag = crZigzag.astype(np.int16)
    cbZigzag = cbZigzag.astype(np.int16)

    return yZigzag, crZigzag, cbZigzag
