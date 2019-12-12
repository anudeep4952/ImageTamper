import numpy as np

from Image import Image

one_bit_img = np.array([0 for i in range(512 * 512)], dtype=np.uint8).reshape(512, 512)


def substitute(rstart, rend, cstart, cend, arr):
    one_bit_img[rstart:rend, cstart:cend] = arr


def generateWM1(img):
    x = Image(img)
    dict = x.binaryDecompose()

    array = [[8, 3, 6, 7],
             [5, 4, 3, 4],
             [4, 3, 4, 5],
             [7, 6, 3, 8]]

    for i in range(4):
        for j in range(4):
            substitute(i * 128, (i + 1) * 128, j * 128, (j + 1) * 128, dict[array[i][j]])

    return one_bit_img
