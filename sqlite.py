import sqlite3

#:memory: buat coba2 ga bakal disimpen
#database: bakal disimpen, bikin file database baru
conn = sqlite3.connect('db.db')
c = conn.cursor() #semua komen, query, bikin lewat c


#buat tabel didalem database
#numpuk komen
#nyuruh si c ngelakuin sesuatu pake execute
#isinya harus string, sensitif gede kecil huruf, judulnya tab, gabisa over write, pake DROP TABLE IF EXIST buat apus kalo sama
#bikin tabel didalam database
#kolom datatype
c.execute("DROP TABLE IF EXISTS tab")
c.execute("""CREATE TABLE tab
            (nama text, 
            usia INT(255),
            email text)
""")
#masukin data ke tabel
#INSERT INTO buat nambahin ke tab
#VALUES buat masukin nilainya
#c.execute("INSERT INTO tab VALUES('Xiumin',30,'xiumin@smtown.com')")
listdata = (
    ('umin',30,'xiu@gmail.com'),
    ('suho',29,'kimjuncotton@yahoo.co.kr'),
    ('baekhyun',28,'b_million@google.com'),
    ('kai',26,'beargod@gmail.co.kr'),
    ('chen',28,'chensa@yahoo.com')

)

#IMAGE -> BLOB
c.execute("DROP TABLE IF EXISTS gambar")
c.execute("""CREATE TABLE gambar
(gambar BLOB)
""")

#executemany buat masukin data lebih dr 1
c.executemany("INSERT INTO tab VALUES (?,?,?)",listdata)

#SELECT buat ngambil datanya
#primary key rowid tu buat ngasih nomer tiap baris, * buat semuanya


#ORDER BY (sort)
#DESC dari gede ke kecil, gapake DESC bakal auto aescending
#c.execute("SELECT rowid,* FROM tab ORDER BY nama")


#QUERY nyari dengan syarat pake WHERE
# n% yg huruf depannya n
#c.execute("SELECT rowid,* FROM tab WHERE nama LIKE 'b%' AND email LIKE '%@google.com'")

#UPDATE
c.execute("UPDATE tab SET nama='lay' WHERE usia=29") #ngubah data yg udah ada, suho yg usia 29 jadi lay
c.execute("SELECT rowid,* FROM tab")

#DELETE
c.execute("DELETE FROM tab WHERE rowid=5") #ngapus yg dibaris ke 5
c.execute("SELECT rowid,* FROM tab") #kalo mo ambil datanya harus ada SELECT

items = c.fetchall() #ngambil semua datanya
#data mulai dari 0 :)
for f in items:
    print(f) #ngambil baris sama kolom

for f in items:
    print(f[1]) #ngambil kolom ke 2

#print(items[2][2]) #ngambil baris ke 2 kolom ke 2

#print(items[2]) ambil data ke 2
#fetchmany tu dibatesin brp
#fetchone sebaris2/1

#IMAGE
gambar=open("Scan.jpg","rb") #rb cuma di read
gambar2=gambar.read()
gambarbaru=open("gambarbaru.jpg","wb")
#harus diubah jadi Binary
gambarsimpen = sqlite3.Binary(gambar2)
#reshape data (gambarsimpen,) jadi 1
c.execute("INSERT INTO gambar VALUES (?)",(gambarsimpen,))
c.execute("SELECT * FROM gambar")
gambarbaru.write(c.fetchone()[0]) #harus dikasih 0, soalnya sebelumnya masih tuple
gambar.close()
gambarbaru.close()
#outputnya ada gambarbaru.jpg yg sama kek foto scan

c.close()



print('database berhasil')
#relational database
#querynya cepet soalnya di data yg sama tu dihubungin aja yg punya nilai yg sama
#tp gabisa nambah table
