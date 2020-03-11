import cv2
# Reading the image in RGB mode
from PIL import Image
import Image as img
from genearte import generate

def substitute():

   img = cv2.imread(input('enter path of image:'), 1)
   img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)

   b, g, r = cv2.split(img)
   # No need of following lines:
   # b,g,r = cv2.split(img)
   r = generate(r)
   b = generate(b)
   g = generate(g)

   rgb = cv2.merge([b, g, r])
   im_rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
   img = Image.fromarray(im_rgb, 'RGB')
   img.save(input('enter path and name to save image (correct format only):'))
   img.show()

# cv2.imshow('rgb image', rgb)
# cv2.imwrite('testImages/lenaWaterMarked1.png', img)
# cv2.waitKey(0)
