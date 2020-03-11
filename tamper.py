import cv2
from PIL import Image as im

from Image import Image
def tamper():
  img = cv2.imread(input('enter path to the image : '), 1)

  per=int(input('enter tamaer % : '))
  start=(100-per)//2
  end=start+per
  img[int(512*(start/100)):int(512*(end/100)),int(512*(start/100)):int(512*(end/100)),:]=255
  im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img = im.fromarray(im_rgb, 'RGB')
  img.save(input('enter the path to save tamptered image : '))
  img.show()

