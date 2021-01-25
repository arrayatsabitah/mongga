#modul tu sebenernya file.py yang isinya fungsi2 jd pake pycharm:)
#kalo mau buat sesuatu yang bisa dipake orang lain, pake virtual environment dan install sendiri modul2nya
import modul as md
#from modul import penjumlahan #hanya memanggil 1 function dari modul
#print(penjumlahan(haha,hehe)) #tidak usah menulis nama modul diawal function
#tidak disarankan

a=17
a=float(17)

Aya = md.orang('Aya',17)
print(Aya.nama)
print(Aya.umur)
Aya.jalan()
Aya.makan()
Aya.umurs('Kai')

#Cara tau ada method apa aja dalam suatu modul, baca di external libraries, lib terus buka aja si .py nya

#inheritance
fuad = md.orangtua('Fuad',89,100)
print(fuad.nama)
fuad.jalan() #method dari parent orang
fuad.sakit() #method tambahan dari inheritance orangtua

#iterator
komunitas = md.orangorang('Kai','Sehun','Baekhyun')
print(komunitas.arg)
for f in komunitas.arg:
    print(f)

