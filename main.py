from imageblock.block import ImageBlock
from dct.dct import DCT2D
from quantization.quantization import Quantization
from huffman.code import calculate_probability, HuffmanCode
from utils.reader import read_image_file
from utils.image import create_image
from converter.convert import rgb2ycbcr, ycbcr2rgb
from sampling.sample import chroma_subsampling
import pickle


if __name__ == "__main__":
    imbl = ImageBlock(block_height=8, block_width=8)
    dct2 = DCT2D()
    quiz = Quantization()


    # get the input file
    path = input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')

    # convert to YCbCr
    pix = rgb2ycbcr(pix)

    # sampling image
    pix = chroma_subsampling(pix)
    
    # creating our blocks
    blocks, indices = imbl.make_blocks(pix)

    # proccesing blocks
    for i in range(len(blocks)):
        block = blocks[i]

        # performing a DCT2
        encoded = dct2.form(block)

        # quantizing
        if indices[i][2] == 0:
            c_type = 'lum'
        else:
            c_type = 'chr'
        encoded = quiz.quantize(encoded, c_type)

        # performing huffman coding
        encoded = HuffmanCode(calculate_probability(encoded))

        blocks[i] = block

    # saving huffman
    with open('out.txt', 'w') as file:
        pickle.dump(blocks, file, protocol=pickle.HIGHEST_PROTOCOL)

    # re-assemble blocks
    pix = imbl.make_image(blocks, indices)

    # convert to jpeg
    pix = ycbcr2rgb(pix)

    # saving image
    create_image(pix)
