import numpy as np

from Image import Image

two_bit_img = np.array([0 for i in range(512 * 512)], dtype=np.uint8).reshape(512, 512)


def substitute(rstart, rend, cstart, cend, arr):
    two_bit_img[rstart:rend, cstart:cend] = arr


def generateWM2(img):
    x = Image(img)
    dict = x.binaryDecompose()
    array = [[8, 7, 8, 7, 8, 7, 8, 7],
             [7, 6, 5, 6, 5, 6, 5, 8],
             [8, 5, 4, 3, 4, 3, 6, 7],
             [7, 6, 3, 4, 3, 4, 5, 8],
             [8, 5, 4, 3, 4, 3, 6, 7],
             [7, 6, 3, 4, 3, 4, 5, 8],
             [8, 5, 6, 5, 6, 5, 6, 7],
             [7, 8, 7, 8, 7, 8, 7, 8]]
    for i in range(8):
        for j in range(8):
            substitute(i * 64, (i + 1) * 64, j * 64, (j + 1) * 64, dict[array[i][j]])
    return two_bit_img
