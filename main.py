from utils.reader import read_image_file
from utils.image import create_image
from converter.convert import rgb2ycbcr
from sampling.sample import chroma_subsampling


if __name__ == "__main__":
    # get the input file
    path = input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')

    # convert to YCbCr
    pix = rgb2ycbcr(pix)

    # creating the image
    img = create_image(pix)
    img.show()

    # sampling image
    spix = chroma_subsampling(pix)
    print(spix)
