from utils.image import *



if __name__ == "__main__":
    # get the input file
    path = 'assets/photo1.png' # input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')
