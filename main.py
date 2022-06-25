from utils.image import *
from utils.convert import rgb2ycbcr

from quantization.sampling import sample
from quantization.quantization import quantize
from quantization.zigzag import get_zigzags

from huffman.huffman import find_huffman, freq

from rlc.rlc import rlc_coding

import numpy as np
import os
import time
from datetime import datetime
import pickle



INPUT_DIR = 'in'
OUTPUT_DIR = 'out'


if __name__ == "__main__":
    # check the output directory
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    
    print(f'[OK][{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}] Begin ...')
    
    # get the input file
    path = input("[Enter the file path] > ")

    start_time = time.time()
    pix, width, height = read_image_file(os.path.join(INPUT_DIR, path))

    print(f'[OK] Input file: {os.path.join(INPUT_DIR, path)}')
    print(f'[OK] Image read: {width}x{height}')

    # converting to YCrCb
    start_time = time.time()
    pix = rgb2ycbcr(pix)
    print(f'[OK][{time.time() - start_time}s] Convert to YCrCb: {pix.shape}')

    # showing the YCrCb image
    create_image(pix).show()

    y = np.zeros((height, width), np.float32) + pix[:, :, 0]
    cr = np.zeros((height, width), np.float32) + pix[:, :, 1]
    cb = np.zeros((height, width), np.float32) + pix[:, :, 2]

    # size of the image in bits before compression
    totalNumberOfBitsWithoutCompression = len(y) * len(y[0]) * 8 + len(cb) * len(cb[0]) * 8 + len(cr) * len(cr[0]) * 8
    print(f'[INFO] Total input: {np.round(totalNumberOfBitsWithoutCompression / 1024, 5)} kb')

    # sampleing
    start_time = time.time()
    y, cr, cb = sample(y, cr, cb)
    print(f'[OK][{time.time() - start_time}s] Chroma subsampling')

    # quantizing
    start_time = time.time()
    y, cr, cb, ws = quantize(y, cr, cb)
    print(f'[OK][{time.time() - start_time}s] Quantized')

    # zigzags
    start_time = time.time()
    y, cr, cb = get_zigzags(y, cr, cb, ws)
    print(f'[OK][{time.time() - start_time}s] Performing ZigZag iteration')

    start_time = time.time()
    # find the run length encoding for each channel
    # then get the frequency of each component in order to form a Huffman dictionary
    yEncoded = rlc_coding(y)
    yHuffman = find_huffman(freq(yEncoded))

    crEncoded = rlc_coding(cr)
    crHuffman = find_huffman(freq(crEncoded))

    cbEncoded = rlc_coding(cb)
    cbHuffman = find_huffman(freq(cbEncoded))

    print(f'[OK][{time.time() - start_time}s] Huffman coding')

    # saving encodeds
    with open(os.path.join(OUTPUT_DIR, "encode_" + path.split('.')[0] + ".pickle"), "wb") as myFile:
        pickle.dump(yEncoded, myFile, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(crEncoded, myFile, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(cbEncoded, myFile, protocol=pickle.HIGHEST_PROTOCOL)
    
    # saving huffman trees
    with open(os.path.join(OUTPUT_DIR, "htrees_" + path.split('.')[0] + ".pickle"), "wb") as myFile:
        pickle.dump(yHuffman, myFile, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(crHuffman, myFile, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(cbHuffman, myFile, protocol=pickle.HIGHEST_PROTOCOL)
    
    print('[OK] Output files created')

    # calculate the number of bits to transmit for each channel
    # and write them to an output file
    yBitsToTransmit, crBitsToTransmit, cbBitsToTransmit = str(), str(), str()
    with open(os.path.join(OUTPUT_DIR, path.split('.')[0] + ".asfh"), "w") as file: 
        for value in yEncoded:
            yBitsToTransmit += yHuffman[value]

        for value in crEncoded:
            crBitsToTransmit += crHuffman[value]

        for value in cbEncoded:
            cbBitsToTransmit += cbHuffman[value]

        file.write(yBitsToTransmit + "\n" + crBitsToTransmit + "\n" + cbBitsToTransmit)

    # total number of bites after compression
    totalNumberOfBitsAfterCompression = len(yBitsToTransmit) + len(crBitsToTransmit) + len(cbBitsToTransmit)
    
    print(f'[INFO] Compressed image size: {np.round(totalNumberOfBitsAfterCompression / 1024, 5)} kb')
    print(f'[INFO] Compression Ratio: {np.round(totalNumberOfBitsWithoutCompression / totalNumberOfBitsAfterCompression, 3)}')
    print(f'[OK][{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}] Done')
