# importing required libraries of opencv
import cv2
import numpy as np



def withinClassVariance(thr,hist):
    WB=sum(hist[:thr])/(64*64)

    if sum(hist[:thr])==0 or sum(hist[thr:])==0 :
        return  np.inf

    meanB=0
    for i in range(thr):
        meanB+=(i*hist[i])
    meanB/=sum(hist[:thr])

    varB=0
    for i in range(thr):
              varB+=((i-meanB)**2)*hist[i]
    varB/=sum(hist[:thr])

    WF = sum(hist[thr:]) / (64*64)

    meanF = 0
    for i in range(thr ,len(hist)):
        meanF += (i * hist[i])

    meanF /= sum(hist[thr:])

    varF = 0
    for i in range(thr ,len(hist)):
        varF += ((i - meanF) ** 2) * hist[i]
    varF/=sum(hist[thr:])

    return WB*varB+WF*varF


# reads an input image



def codedOSTU(img):
# img = cv2.imread('testImages/lena.png',0)

# find frequency of pixels in range 0-255
  histr = cv2.calcHist([img],[0],None,[256],[0,256])
  histr=[int(i) for i in histr]

  a=[int(i) for i in range(1,254)]
  t,v=0,np.inf
  for i in a:
    if  withinClassVariance(i,histr)<v:
       t,v=i,withinClassVariance(i,histr)

  ret, thresh1 = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
  return(ret,thresh1)


#ret, thresh1 = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)


# while True:
#     cv2.imshow("Frame", thresh1)
#     key = cv2.waitKey(1) & 0xFF
#     # if the q key was pressed, break from the loop
#     if key == ord("q"):
#         break
# cv2.destroyAllWindows()
#
# x, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# print("otsu",x)
# while True:
#     cv2.imshow("Frame", img)
#     key = cv2.waitKey(1) & 0xFF
#     # if the q key was pressed, break from the loop
#     if key == ord("q"):
#         break
# cv2.destroyAllWindows()

#withinClassVariance(3,[8,7,2,6,9,4])
