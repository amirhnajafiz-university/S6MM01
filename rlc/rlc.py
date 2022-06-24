import numpy as np



"""
In case the trim_zeros function returns 
an empty array, add a zero to the array 
to use as the DC component.
"""
def trim(array: np.ndarray) -> np.ndarray:
    trimmed = np.trim_zeros(array, 'b')

    if len(trimmed) == 0:
        trimmed = np.zeros(1)

    return trimmed


 """
finds the intermediary stream representing 
the zigzags.
format for DC components is <size><amplitude>
format for AC components is <run_length, size> <Amplitude of non-zero>
"""
def run_length_encoding(array: np.ndarray) -> list:
    # encoded output
    encoded = list()
    # initializing the run length
    run_length = 0
    # end of block
    eob = ("EOB",)

    for i in range(len(array)):
        for j in range(len(array[i])):
            trimmed = trim(array[i])
            if j == len(trimmed):
                encoded.append(eob)  # EOB
                break
            if i == 0 and j == 0:  # for the first DC component
                encoded.append((int(trimmed[j]).bit_length(), trimmed[j]))
            elif j == 0:  # to compute the difference between DC components
                diff = int(array[i][j] - array[i - 1][j])
                if diff != 0:
                    encoded.append((diff.bit_length(), diff))
                else:
                    encoded.append((1, diff))
                run_length = 0
            elif trimmed[j] == 0:  # increment run_length by one in case of a zero
                run_length += 1
            else:  # intermediary steam representation of the AC components
                encoded.append((run_length, int(trimmed[j]).bit_length(), trimmed[j]))
                run_length = 0
            # send EOB
        if not (encoded[len(encoded) - 1] == eob):
            encoded.append(eob)
    return encoded
