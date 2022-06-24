import numpy as np
from scipy.fftpack import dct


"""
This function performs a DCT2 operation
"""
def dct2(block, norm='ortho'):
    return dct(dct(block, norm=norm, axis=0), norm=norm, axis=1)


"""
This function performs a IDCT2 operation
"""
def idct2(block, norm='ortho'):
    dct(dct(block, type=3, norm=norm, axis=0), type=3, norm=norm, axis=1)


"""
this class opertes the 2 dimention DCT
"""
class DCT2D():
    """
    constructor
    """
    def __init__(self, norm='ortho'):
        self.norm = norm
    
    """
    performs the dct2 operation
    """
    def form(self, x):
        return dct2(x, self.norm)
    
    """
    performs the idct2 operation
    """
    def deform(self,x):
        return idct2(x, self.norm)
