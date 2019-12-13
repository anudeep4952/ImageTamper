import cv2
from PIL import Image as pil

from Image import Image
from tamperDetect import tamperDetect

img = cv2.imread('testImages/lenaTampered.png', 1)

b, g, r = cv2.split(img)

x = Image(b)
x = x.binaryDecompose()
wmB = x[2]
x1 = Image(g)
x1 = x1.binaryDecompose()
wmG = x1[2]
x2 = Image(r)
x2 = x2.binaryDecompose()
wmR= x2[2]


img = cv2.imread('testImages/lenaTampered.png', 1)
img=cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

b, g, r = cv2.split(img)

tiB=Image(b).binaryDecompose()
tiG=Image(g).binaryDecompose()
tiR=Image(r).binaryDecompose()

img=tamperDetect(wmR,wmB,wmG,tiR,tiB,tiG)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = pil.fromarray(img)
img.show()

