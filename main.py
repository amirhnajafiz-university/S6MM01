from utils.image import *
from utils.convert import rgb2ycbcr

from quantization.sampling import sample
from quantization.quantization import quantize
from quantization.zigzag import get_zigzags

from huffman.huffman import find_huffman, get_freq_dict

from rlc.rlc import run_length_encoding

import numpy as np 



if __name__ == "__main__":
    # get the input file
    path = 'assets/photo1.png' # input("[Enter the file path] > ")
    pix, width, height = read_image_file(path)

    print(f'Image read: {width}x{height}')

    # converting to YCrCb
    pix = rgb2ycbcr(pix)

    y = np.zeros((height, width), np.float32) + pix[:, :, 0]
    cr = np.zeros((height, width), np.float32) + pix[:, :, 1]
    cb = np.zeros((height, width), np.float32) + pix[:, :, 2]

    # size of the image in bits before compression
    totalNumberOfBitsWithoutCompression = len(y) * len(y[0]) * 8 + len(cb) * len(cb[0]) * 8 + len(cr) * len(cr[0]) * 8

    # sampleing
    y, cr, cb = sample(y, cr, cb)

    # quantizing
    y, cr, cb, ws = quantize(y, cr, cb)

    # zigzags
    y, cr, cb = get_zigzags(y, cr, cb, ws)

    # find the run length encoding for each channel
    # then get the frequency of each component in order to form a Huffman dictionary
    yEncoded = run_length_encoding(y)
    yFrequencyTable = get_freq_dict(yEncoded)
    yHuffman = find_huffman(yFrequencyTable)

    crEncoded = run_length_encoding(cr)
    crFrequencyTable = get_freq_dict(crEncoded)
    crHuffman = find_huffman(crFrequencyTable)

    cbEncoded = run_length_encoding(cb)
    cbFrequencyTable = get_freq_dict(cbEncoded)
    cbHuffman = find_huffman(cbFrequencyTable)

    # calculate the number of bits to transmit for each channel
    # and write them to an output file
    file = open("CompressedImage.asfh", "w")
    yBitsToTransmit = str()
    for value in yEncoded:
        yBitsToTransmit += yHuffman[value]

    crBitsToTransmit = str()
    for value in crEncoded:
        crBitsToTransmit += crHuffman[value]

    cbBitsToTransmit = str()
    for value in cbEncoded:
        cbBitsToTransmit += cbHuffman[value]

    if file.writable():
        file.write(yBitsToTransmit + "\n" + crBitsToTransmit + "\n" + cbBitsToTransmit)
    file.close()

    totalNumberOfBitsAfterCompression = len(yBitsToTransmit) + len(crBitsToTransmit) + len(cbBitsToTransmit)
    print(
        "Compression Ratio is " + str(
            np.round(totalNumberOfBitsWithoutCompression / totalNumberOfBitsAfterCompression, 1)))
