#a=3/0
#print(a) #jelas error

try:
    x=int(input('penyebut : '))
    y=int(input('pembilang: '))
    result=y/x
except ValueError:
    print('tipe data salah')
except ZeroDivisionError:
    print('penyebut tidak boleh 0')
finally: #tetep dijalanin mengabaikan error
    print('program selesai')
if y>3:
    raise Exception('gabole') #sebenernya ga error, tp dibuat error
print(result)