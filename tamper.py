import cv2
from PIL import Image as im

from Image import Image

img = cv2.imread('testImages/lenaWaterMarked.png', 1)

#img[210:350,230:360,:]=255
im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = im.fromarray(im_rgb, 'RGB')
img.save('testImages/lenaTampered.png')
img.show()

# img=cv2.imread('testImages/lenaTampered.png',1)
# b,g,r=cv2.split(img)
# b=Image(b).binaryDecompose()
# g=Image(g).binaryDecompose()
# r=Image(r).binaryDecompose()
#
# rgb = cv2.merge([b[2]*128, g[2]*128, r[2]*128])
# im_rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
# img = im.fromarray(im_rgb, 'RGB')
# img.show()
#
