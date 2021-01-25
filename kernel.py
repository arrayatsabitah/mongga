import cv2
import numpy as np

img = cv2.imread('kai2.jpg')

#resized image
imgresized = cv2.resize(img,(640,480))
cv2.imshow('Gambar 1',img)
cv2.imshow('Gambar resized',imgresized)
cv2.waitKey(0)

#grayscale
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',imggray)
cv2.waitKey(0)

#kernel tu pokoknya yang paling ngubah gambar, entah makin blur atau makin kereng

#blur image ngilangin Gaussian noise dengan kernel
#(5,5) tu fungsi kernel buat ngatur seberapa blur, 1 tu sigmaX
#fungsi kernel harus n,n dan harus ganjil
imgblur1 = cv2.GaussianBlur(imgresized,(11,11),1)
imgblur10 = cv2.GaussianBlur(imgresized,(11,11),10)
imgblur5 = cv2.GaussianBlur(imgresized,(5,5),5)

cv2.imshow('Blur1',imgblur1)
cv2.imshow('Blur10',imgblur10)
cv2.imshow('Blur5',imgblur5)
cv2.waitKey(0)

#outline
imgcanny = cv2.Canny(imggray,10,300)
#ngebandingin sama threshold mana yang jadi outline mana yang ngga, 150,200 tu threshold/batas
#semakin batas bawahnya kecil, semakin banyak outline nya
#jadi kalo lebih kecil dari batas bawah, ga jadi outline
#kalo lebih gede dari batas atas, jadi outline
#kalo diantara batas bawah dan atas, kalo connect ke yg jadi outline, maka jadi outline

#dilation itu buat kerengin warna putihnya
kernel=np.ones((5,5),np.uint8) #uint8 skalanya 0:255 maka grayscale, kalo gapake jd bw
imgDilation = cv2.dilate(imgcanny,kernel,iterations=1)

#eroded ngapus garis putih yang jelas di outline
#kalo di foto biasa jd serem
imgEroded = cv2.erode(imgcanny,kernel,iterations=1)
imgEroded2 = cv2.erode(img,kernel,iterations=1)

#crop
imgcropped = img[0:200,0:200] #dianggep kayak array
#yang kiri tu sumbu y, kanan sumbu x, dimulai dari kiri atas gambar gerak ke bawah (y) dan ke kanan (x)

cv2.imshow('outline',imgcanny)
cv2.imshow('dilation',imgDilation)
cv2.imshow('erode1',imgEroded)
cv2.imshow('erode2',imgEroded2)
cv2.imshow('crop',imgcropped)
cv2.waitKey(0)