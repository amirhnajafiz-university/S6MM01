from collections import Counter
import numpy as np



"""
returns a dict where the keys 
are the values of the array, 
and the values are their frequencies.
"""
def get_freq_dict(array: list) -> dict:
    data = Counter(array)
    result = {k: d / len(array) for k, d in data.items()}

    return result


"""
Return pair of symbols 
from distribution p with lowest probabilities.
"""
def lowest_prob_pair(p):
    sorted_p = sorted(p.items(), key=lambda x: x[1])
    return sorted_p[0][0], sorted_p[1][0]


"""
returns a Huffman code 
for an ensemble with distribution p.
"""
def find_huffman(p: dict) -> dict:
    # Base case of only two symbols, assign 0 or 1 arbitrarily; frequency does not matter
    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest probable pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = find_huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c
