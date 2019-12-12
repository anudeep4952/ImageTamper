import numpy as np
import cv2

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
            xR = abs(tiR[array[i][j]] - (wmR[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64] * (2 ** (array[i][j] - 1))))
            xB = abs(tiB[array[i][j]] - (wmB[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64] * (2 ** (array[i][j] - 1))))
            xG = abs(tiG[array[i][j]] - (wmG[i * 64: (i + 1) * 64, j * 64: (j + 1) * 64] * (2 ** (array[i][j] - 1))))
            imgR = np.add(imgR, xR)
            imgB = np.add(imgB, xB)
            imgG = np.add(imgG, xG)


            # cv2.imshow(str(i)+' '+str(j),imgR+imgG+imgB)
            # cv2.waitKey(0)

    return cv2.merge([imgB,imgG,imgR])

