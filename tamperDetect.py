import numpy as np
import cv2
from PIL import Image

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
            xR = np.absolute(np.subtract(tiR[array[i][j]], (wmR[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64])))%255
            xB = np.absolute(np.subtract(tiB[array[i][j]], (wmB[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64])))%255
            xG = np.absolute(np.subtract(tiG[array[i][j]], (wmG[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64])))%255


            imgR = np.add(imgR, xR)
            imgB = np.add(imgB, xB)
            imgG = np.add(imgG, xG)

    img=np.add(imgR,np.add(imgG,imgB))

    x,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return img
#img = np.array(img).astype(np.uint8)