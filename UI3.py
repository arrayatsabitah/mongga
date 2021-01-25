import PySimpleGUI as sg
import os.path

#size (x,y) dalam jumlah karakter
kolom1=[
    [
        sg.Text('Image Foder '),
        sg.In(size=(15,1),key='-INPUT-'),
        sg.FolderBrowse(key='-BROWSE-') #outputnya tu path folder
    ],
    [
        sg.Listbox(
        values=[], size=(40,30), key='-LIST-'
        )
    ]
]

kolom2=[
    [
        sg.Text('Choose an image from list from left')
    ],
    [
        sg.Text(size=(20,1),key='-TEXT2-')
    ],
    [
        sg.Image(key='-IMG-')
    ]
]
layout=[
    [
        sg.Column(kolom1), #buat nyatain ada kolom yang ada isinya
        sg.VSeparator(),
        sg.Column(kolom2),
        sg.Submit() #buat langsung masukin objek aja
    ]
]

#biar bisa di run, harus ada semua yg dibawah
window=sg.Window('UI lagi',layout)

while True:
    event,values = window.read()  #kalo gada event, values gabisa interaksi sama windownya
    if event=='Exit' or event==sg.WIN_CLOSED:
        break
    if event=='-BROWSE-':
        folder=values['-BROWSE-']
        try:  #biar ga error, jd kalo error keluarnya kosong
            #mengambil list file di folder
            file_list=os.listdir(folder)
        except:
            file_list=[]
#filter tipe data yg diambil
        fnames=[]
        for f in file_list:
            filetotal=os.path.join(folder,f)  #ngegabungin path folder sama file
            if os.path.isfile(filetotal) and f.lower().endswith(('.jpg','.png')):
                fnames.append(f)

        window['-LIST-'].update(fnames)

    if event=='-LIST-':
        try:
            filename=os.path.join(values['-BROWSE-'],values['-LIST-'][0])
            window['-TEXT2-'].update(filename)
            window['-IMG-'].update(filename=filename)
        except:
            pass

window.close()