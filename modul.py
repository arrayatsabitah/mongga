# suatu objek dikatakan class jika punya atribut __init__
class orang:
    def __init__(self, nama, umur): #init tu ngejelasin tentang saya (self)
        self.nama = nama
        self.umur = umur  # kayak buat ngenalin diri sendiri

    def jalan(self):
        print('orang jalan')

    def makan(self):
        print(self.nama + 'suka makan')

    def umurs(self, namateman):
        print('umur teman ' + namateman + ' ' + str(self.umur) + ' tahun')

#inheritance
#bikin class baru pake class yang udah ada, tapi isinya mau diganti-ganti
#mewarisi semua method yg ada di class parent (yg udah ada) (overwrite)
class orangtua(orang):
    def __init__(self,nama,umur,waktumati):
        #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
        #to keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
        self.nama=nama
        self.umur=umur
        self.waktumati=waktumati

    def sakit(self):
        print(self.nama+' suka sakit-sakitan')
    def makan(self):
        print(self.nama+'cuma bisa makna tidur')

class orangorang:
    def __init__(self,*args):
        self.arg=args
        self.counter=0

    def __iter__(self): #*args jumlah argumen tidak terbatas
        self.a= self.arg[self.counter]
        return self.a

    def __next__(self):
        self.counter += 1
        x = self.arg[self.counter]
        return x





def penjumlahan(a,b):
    sum=a+b
    return sum

def pengurangan(a,b):
    kurang=b-a
    return kurang