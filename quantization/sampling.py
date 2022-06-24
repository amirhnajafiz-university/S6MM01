import cv2



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
    SSH, SSV = 2, 0

    crf = cv2.boxFilter(cr, ddepth=-1, ksize=(2, 2))
    cbf = cv2.boxFilter(cb, ddepth=-1, ksize=(2, 2))

    crSub = crf[::, ::SSH]
    cbSub = cbf[::, ::SSH]

    return y, crSub, cbSub
