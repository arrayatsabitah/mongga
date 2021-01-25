import cv2
import numpy as np

#0 item, 511 putih
#np.zeros array isi 0 semua
img = np.zeros((512,512)) #array ukuran 512x512 isinya 0 semua jadi item
img3 = np.zeros((256,512))
img4 = np.zeros((512,512))+511 #511 putih
img5 = np.zeros((512,512),np.uint8)+200 #ngubah isi array ga cuma 0 1 jadi skala 255, ditambah 200 jadi grayscale

img2 = np.zeros((512,512,3),np.uint8) #3 bikin RGB, uint8 buat skala 255 biar berwarna
#kayak di crop, dan bagian yang di crop itu diwarnain beda2
img2[:256,:256]=255,0,0
img2[256:,:256]=0,255,0
img2[:256,256:]=0,0,255
img2[256:,256:]=100,100,100

cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img5',img5)
cv2.waitKey(0)

