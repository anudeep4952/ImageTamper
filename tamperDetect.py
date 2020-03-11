import numpy as np
import cv2
from PIL import Image

from otsu import codedOSTU

array = [[8, 7, 8, 7, 8, 7, 8, 7],
         [7, 6, 5, 6, 5, 6, 5, 8],
         [8, 5, 4, 3, 4, 3, 6, 7],
         [7, 6, 3, 4, 3, 4, 5, 8],
         [8, 5, 4, 3, 4, 3, 6, 7],
         [7, 6, 3, 4, 3, 4, 5, 8],
         [8, 5, 6, 5, 6, 5, 6, 7],
         [7, 8, 7, 8, 7, 8, 7, 8]]


def tamperDetect(wmR, wmB, wmG, tiR, tiB, tiG):
    global array
    imgR = np.array([0 for i in range(64 * 64)], dtype=np.uint8).reshape(64, 64)
    imgB = np.array([0 for i in range(64 * 64)], dtype=np.uint8).reshape(64, 64)
    imgG = np.array([0 for i in range(64 * 64)], dtype=np.uint8).reshape(64, 64)

    for i in range(8):
        for j in range(8):
            xR = np.absolute(np.subtract(tiR[array[i][j]], (wmR[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64]))) % 254
            xB = np.absolute(np.subtract(tiB[array[i][j]], (wmB[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64]))) % 254
            xG = np.absolute(np.subtract(tiG[array[i][j]], (wmG[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64]))) % 254

            imgR = np.add(imgR, xR)
            imgB = np.add(imgB, xB)
            imgG = np.add(imgG, xG)

    img = np.add(imgR, np.add(imgG, imgB))
    l = [img]
    #x, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret,img=codedOSTU(img)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    l.append(img)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    l.append(img)
    return l


# img = np.array(img).astype(np.uint8)


def restore(test):
    b, g, r = cv2.split(test)
    b = calculate(b)
    g = calculate(g)
    r = calculate(r)
    return cv2.merge([b, g, r])


def calculate(test):
    array = [[8, 3, 6, 7],
             [5, 4, 3, 4],
             [4, 3, 4, 5],
             [7, 6, 3, 8]]
    eight = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)
    seven = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)
    six = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)
    five = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)
    four = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)
    three = np.array([0 for i in range(128 * 128)], dtype=np.uint8).reshape(128, 128)

    for i in range(4):
        for j in range(4):
            if array[i][j] == 8:
                eight = np.logical_or(eight, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])
            elif array[i][j] == 7:
                seven = np.logical_or(seven, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])
            elif array[i][j] == 6:
                six = np.logical_or(six, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])
            elif array[i][j] == 5:
                five = np.logical_or(five, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])
            elif array[i][j] == 4:
                four = np.logical_or(four, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])
            elif array[i][j] == 3:
                three = np.logical_or(three, test[i * 128: (i + 1) * 128, j * 128: (j + 1) * 128])

    return eight * 128 + seven * 64 + six * 32 + five * 16 + four * 8 + three * 4
