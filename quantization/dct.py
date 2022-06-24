import numpy as np



def perform_dct(y, cr, cb, yLength, yWidth, cWidth, cLength, windowSize):
    # get DCT of each channel
    # define three empty matrices
    yDct, crDct, cbDct = np.zeros((yLength, yWidth)), np.zeros((cLength, cWidth)), np.zeros((cLength, cWidth))

    # number of iteration on x axis and y axis to calculate the luminance cosine transform values
    hBlocksForY = int(len(yDct[0]) / windowSize)  # number of blocks in the horizontal direction for luminance
    vBlocksForY = int(len(yDct) / windowSize)  # number of blocks in the vertical direction for luminance
    # number of iteration on x axis and y axis to calculate the chrominance channels cosine transforms values
    hBlocksForC = int(len(crDct[0]) / windowSize)  # number of blocks in the horizontal direction for chrominance
    vBlocksForC = int(len(crDct) / windowSize)  # number of blocks in the vertical direction for chrominance

    for i in range(vBlocksForY):
        for j in range(hBlocksForY):
            yDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = cv2.dct(
                y[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
    
    # either crq or cbq can be used to compute the number of blocks
    for i in range(vBlocksForC):
        for j in range(hBlocksForC):
            crDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = cv2.dct(
                cr[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
            cbDct[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize] = cv2.dct(
                cb[i * windowSize: i * windowSize + windowSize, j * windowSize: j * windowSize + windowSize])
            
    return yDct, crDct, cbDct
