import numpy as np
from scipy.fftpack import dct, idct


"""
This function performs a DCT2 operation
"""
def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')


"""
This function performs a IDCT2 operation
"""
def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')
