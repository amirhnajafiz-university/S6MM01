import numpy as np


"""
Image block will get an image and block size, then it will
change our image to blocks or builds our images from the blocks
"""
class ImageBlock():
    """
    constructor
    """
    def __init__(self, block_height=8, block_width=8):
        self.block_height = block_height
        self.block_width = block_width
        self.left_padding = self.right_padding = self.top_padding = self.bottom_padding = 0
    
    """
    takes the image array and converts it to blocks
    """
    def make_blocks(self, image):
        self.image_height = image.shape[0]
        self.image_width = image.shape[1]
        self.image_channel = image.shape[2]
    
        # Vertical padding
        if self.image_height % self.block_height != 0:
            vpad = self.image_height % self.block_height
            self.top_padding = vpad // 2 
            self.bottom_padding = vpad - self.top_padding
            image = np.concatenate((np.repeat(image[:1], self.top_padding, 0), image, 
                                    np.repeat(image[-1:], self.bottom_padding, 0)), axis=0)
            
        # Horizontal padding
        if self.image_width % self.block_width != 0:
            hpad = self.image_width % self.block_width
            self.left_padding = hpad // 2 
            self.right_padding = hpad - self.left_padding
            image = np.concatenate((np.repeat(image[:,:1], self.left_padding, 1), image, 
                                    np.repeat(image[:,-1:], self.right_padding, 1)), axis=1)
    
        # Update dimension
        self.image_height = image.shape[0]
        self.image_width = image.shape[1]

        # Create blocks
        blocks = []
        indices = []
        for i in range(0, self.image_height, self.block_height):
            for j in range(0, self.image_width, self.block_width):
                for k in range(self.image_channel):
                    blocks.append(image[i:i+self.block_height, j:j+self.block_width, k])
                    indices.append((i,j,k))
                    
        blocks = np.array(blocks)
        indices = np.array(indices)

        return blocks, indices
    
    """
    takes the blocks and indices and returns the image
    """
    def backward(self, blocks, indices):
        # Empty image array
        image = np.zeros((self.image_height, self.image_width, self.image_channel)).astype(int)
        for block, index in zip(blocks, indices):
            i, j, k = index
            image[i:i+self.block_height, j:j+self.block_width, k] = block
            
        # Remove padding
        if self.top_padding > 0:
            image = image[self.top_padding:,:,:]
        if self.bottom_padding > 0:
            image = image[:-self.bottom_padding,:,:] 
        if self.left_padding > 0:
            image = image[:,self.left_padding:,:]
        if self.right_padding > 0:
            image = image[:,:-self.right_padding,:]

        return image
