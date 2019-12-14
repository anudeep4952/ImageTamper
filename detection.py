import cv2
from PIL import Image as pil
import numpy as np
from Image import Image
from tamperDetect import tamperDetect, restore

img = cv2.imread('testImages/testImageTampered.png', 1)

b, g, r = cv2.split(img)

x = Image(b)
lsbB=x.binaryDecompose()[1]
x = x.binaryDecompose()
wmB = x[2]

x1 = Image(g)
lsbG=x1.binaryDecompose()[1]
x1 = x1.binaryDecompose()
wmG = x1[2]

x2 = Image(r)
lsbR=x2.binaryDecompose()[1]
x2 = x2.binaryDecompose()
wmR= x2[2]



img = cv2.imread('testImages/testImageTampered.png', 1)
img=cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

b, g, r = cv2.split(img)

tiB=Image(b).binaryDecompose()
tiG=Image(g).binaryDecompose()
tiR=Image(r).binaryDecompose()

img=tamperDetect(wmR,wmB,wmG,tiR,tiB,tiG)
x=img
x=pil.fromarray(x)
x.show()
img=cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.bitwise_not(img)%254
test=cv2.merge([np.multiply(lsbB,img1),np.multiply(lsbG,img1),np.multiply(lsbR,img1)])

test=restore(test)
test = np.array(test).astype(np.uint8)
img = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
img = pil.fromarray(img)
img.show()

