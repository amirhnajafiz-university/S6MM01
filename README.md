# JPEG-compression

Compress our images into JPEG standard.<br />
Using YCrCb, Chroma Subsampling, Quantization, RLC and Huffman algorithms.

## How to use?
Clone into the repository:
```shell
git clone https://github.com/amirhnajafiz/JPEG-compression.git
```

After that install the dependencies:
```shell
pip install -r requirements.txt
```

Put your images in _in_ directory.

Now run the project:
```shell
python main.py
```

Enter the file name:
```shell
[Enter the file path] > myfile.png
```

Now you should have these files in _out_ directory:
```shell
|_ out/
    |_ myfile.asfh (compressed file)
    |_ encode_myfile.pickle
    |_ htrees_myfile.pickle
```

You can see the image codes in *encode_myfile.pickle* and huffman trees in *htrees_myfile.pickle*.
