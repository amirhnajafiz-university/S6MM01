"""
this function checks the paddings and gives our
image paddings if needed.
"""
def give_padding(y, cr, cb, windowSize):
    # calculating the y width and y length
    yWidth, yLength = ceil(len(y[0]) / windowSize) * windowSize, ceil(len(y) / windowSize) * windowSize
    
    if (len(y[0]) % windowSize == 0) and (len(y) % windowSize == 0):
        yPadded = y.copy()
    else:
        yPadded = np.zeros((yLength, yWidth))
        for i in range(len(y)):
            for j in range(len(y[0])):
                yPadded[i, j] += y[i, j]
    
    # chrominance channels have the same dimensions, meaning both can be padded in one loop
    cWidth, cLength = ceil(len(cb[0]) / windowSize) * windowSize, ceil(len(cb) / windowSize) * windowSize
    if (len(cb[0]) % windowSize == 0) and (len(cb) % windowSize == 0):
        crPadded = cr.copy()
        cbPadded = cb.copy()
    # since chrominance channels have the same dimensions, one loop is enough
    else:
        crPadded = np.zeros((cLength, cWidth))
        cbPadded = np.zeros((cLength, cWidth))
        for i in range(len(cr)):
            for j in range(len(cr[0])):
                crPadded[i, j] += cr[i, j]
                cbPadded[i, j] += cb[i, j]
    
    return yPadded, crPadded, cbPadded, yWidth, yLength, cWidth, cLength
