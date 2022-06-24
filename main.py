from imageblock.block import ImageBlock
from dct.dct import DCT2D
from quantization.quantization import Quantization
from huffman.code import calculate_probability, HuffmanCode
from utils.reader import read_image_file
from utils.image import create_image, save_image
from converter.convert import rgb2ycbcr, ycbcr2rgb
from sampling.sample import chroma_subsampling

import numpy as np
import pickle
from multiprocessing.pool import Pool


imbl = ImageBlock(block_height=8, block_width=8)
dct2 = DCT2D()
quiz = Quantization()


def process_block(block, index):
    # DCT
    encoded = dct2.form(block)
    if index[2] == 0:
        channel_type = 'lum'
    else:
        channel_type = 'chr'
        
    # Quantization
    encoded = quiz.quantize(encoded, channel_type)

    # performing huffman coding
    # encoded = HuffmanCode(calculate_probability(encoded.tolist()))

    return encoded


if __name__ == "__main__":
    # get the input file
    path = 'assets/photo1.png' # input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')

    # convert to YCbCr
    pix = rgb2ycbcr(pix)

    # sampling image
    y = chroma_subsampling(pix[:, :, 0])
    cr = chroma_subsampling(pix[:, :, 1])
    cb = chroma_subsampling(pix[:, :, 2])

    pix = np.stack((y, cr, cb), axis=2)
    
    # creating our blocks
    blocks, indices = imbl.make_blocks(pix)

    # processing blocks
    blocks = np.array(Pool().starmap(process_block, zip(blocks, indices)))

    # saving huffman
    # with open('out.txt', 'w') as file:
    #    pickle.dump(blocks, file, protocol=pickle.HIGHEST_PROTOCOL)

    # re-assemble blocks
    pix = imbl.make_image(blocks, indices)

    # convert to jpeg
    pix = ycbcr2rgb(pix)

    # saving image
    save_image(pix, 'photo1.jpeg')

    # showing image
    create_image(pix).show()
