from collections import Counter
import numpy as np



"""
A Huffman Tree Node
"""
class Node:
    """
    constructor
    """
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left
        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = ''


"""
prints the huffman tree into a dictionary.
"""
def get_code(node: Node, dic: dict, val='') -> dict:
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        dic = get_code(node.left, dic, newVal)
    if(node.right):
        dic = get_code(node.right, dic, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        dic[node.symbol] = newVal
    
    return dic


"""
returns a Huffman code 
for an ensemble with distribution p.
"""
def do_huffman(p: dict) -> dict:
    # list containing unused nodes
    nodes = []
    
    # converting characters and frequencies
    # into huffman tree nodes
    for key in p:
        nodes.append(Node(p[key], key))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
    
        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]
    
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    # Huffman Tree is ready!
    dic = {}
    return get_code(nodes[0], dic)


"""
returns a dict where the keys 
are the values of the array, 
and the values are their frequencies.
"""
def freq(array: list) -> dict:
    data = Counter(array)
    result = {k: d / len(array) for k, d in data.items()}

    return result
