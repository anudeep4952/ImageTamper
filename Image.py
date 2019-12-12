import numpy as np


class Image:

    def __init__(self, img) -> None:
        super().__init__()
        self.img = img
        self.lst = []
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                self.lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits

    def binaryDecompose(self):
        eight_bit_img = (np.array([int(i[0]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                          self.img.shape[1])
        seven_bit_img = (np.array([int(i[1]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                          self.img.shape[1])
        six_bit_img = (np.array([int(i[2]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                        self.img.shape[1])
        five_bit_img = (np.array([int(i[3]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                         self.img.shape[1])
        four_bit_img = (np.array([int(i[4]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                         self.img.shape[1])
        three_bit_img = (np.array([int(i[5]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                          self.img.shape[1])
        two_bit_img = (np.array([int(i[6]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                        self.img.shape[1])
        one_bit_img = (np.array([int(i[7]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                        self.img.shape[1])
        return {8: eight_bit_img, 7: seven_bit_img, 6: six_bit_img, 5: five_bit_img, 4: four_bit_img, 3: three_bit_img,
                2: two_bit_img, 1: one_bit_img}

    def colorDecompose(self):
        eight_bit_img = (np.array([int(i[0]) for i in self.lst], dtype=np.uint8) * 128).reshape(self.img.shape[0],
                                                                                                self.img.shape[1])
        seven_bit_img = (np.array([int(i[1]) for i in self.lst], dtype=np.uint8) * 64).reshape(self.img.shape[0],
                                                                                               self.img.shape[1])
        six_bit_img = (np.array([int(i[2]) for i in self.lst], dtype=np.uint8) * 32).reshape(self.img.shape[0],
                                                                                             self.img.shape[1])
        five_bit_img = (np.array([int(i[3]) for i in self.lst], dtype=np.uint8) * 16).reshape(self.img.shape[0],
                                                                                              self.img.shape[1])
        four_bit_img = (np.array([int(i[4]) for i in self.lst], dtype=np.uint8) * 8).reshape(self.img.shape[0],
                                                                                             self.img.shape[1])
        three_bit_img = (np.array([int(i[5]) for i in self.lst], dtype=np.uint8) * 4).reshape(self.img.shape[0],
                                                                                              self.img.shape[1])
        two_bit_img = (np.array([int(i[6]) for i in self.lst], dtype=np.uint8) * 2).reshape(self.img.shape[0],
                                                                                            self.img.shape[1])
        one_bit_img = (np.array([int(i[7]) for i in self.lst], dtype=np.uint8)).reshape(self.img.shape[0],
                                                                                        self.img.shape[1])
        return {8: eight_bit_img, 7: seven_bit_img, 6: six_bit_img, 5: five_bit_img, 4: four_bit_img, 3: three_bit_img,
                2: two_bit_img, 1: one_bit_img}
