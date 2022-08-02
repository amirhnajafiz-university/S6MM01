# huffman package
# ================
from huffman.huffman import freq, do_huffman
# ================

import numpy as np



if __name__ == "__main__":
    # input array
    array = "AABEEEDRTTTT"

    # input size
    totalNumberOfBitsWithoutCompression = len(array) * 8

    # doing huffman coding
    prob = freq(array)
    encode = do_huffman(prob)

    # creating transmit
    transmit = str()
    for value in encode:
        transmit += encode[value]

    # output size
    totalNumberOfBitsAfterCompression = len(transmit)

    # output information
    print(f'Frequency:\n{prob}')
    print(f'Output:\n{encode}')

    print(f'Input size: {totalNumberOfBitsWithoutCompression} bits')
    print(f'Compressed size: {totalNumberOfBitsAfterCompression} bits')
    print(f'Compression Ratio: {np.round(totalNumberOfBitsWithoutCompression / totalNumberOfBitsAfterCompression, 3)}')
