import cv2

from Image import Image
from WM1substitute import generateWM1
from WM2substitute import generateWM2


# Read the image in greyscale
def generate(img):

    # WaterMark 1
    WM1 = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)

    # WaterMark 2
    WM2 = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

    # Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
    img = Image(img)


    # We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
    # Multiply with 2^(n-1) and reshape to reconstruct the bit image.
    x = img.binaryDecompose()
    two_bit_img = generateWM2(WM2)
    one_bit_img = generateWM1(WM1)

    x1 = img.colorDecompose()
    two_bit_img1 = two_bit_img * 2
    watermarked_img = x1[8] + x1[7] + x1[6] + x1[5] + x1[4] + x1[3] + two_bit_img1 + one_bit_img


    return watermarked_img
