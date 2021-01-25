import cv2

#buat file handler gambar
#img = cv2.imread('gambarbaru.jpg')

#buat nunjukin gambar
#v2.imshow('Gambar 1',img)
#cv2.waitKey(0) #durasi selamanya, kalo 1000 berarti 1000 milisecond muncul gambarnya

#buat buka video/webcam
cap = cv2.VideoCapture('D://EXplOration in Jakarta/20191123_154257.mp4')
#kalo pake 0, buka webcam
#kalo isi pake path video, buka video

#kode cap.set
cap.set(3,640) #atur dimensi lebar
cap.set(4,480) #atur tinggi
cap.set(10,1000) #atur brightness

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #buat close pencet q
        break
