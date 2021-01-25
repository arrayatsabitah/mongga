import PySimpleGUI as sg

kolom1=[
    [sg.In(size=(40,1),key='-INPUT-')], #key tu kayak nama objek itu kek nama variabel
    [sg.Button('Tombol Ganti Text',key='-TOMBOL1-')],
    [sg.Submit('Submit')]
]
kolom2=[
    [sg.Text('Text akan berubah',key='-TEXT-')],
]
layout=[
    [sg.Column(kolom1)], #ngebentuk kolom baru
    [sg.VSeparator()],
    [sg.Column(kolom2)]
]
#biar bisa di run, harus ada semua yg dibawah
window=sg.Window('Tes UI',layout)

#event berhubungan dengan key, event yg udah ada itu EXIT (builtin)

while True:
    event, values = window.read()
    if event=='EXIT' or event==sg.WIN_CLOSED:  #Jadi kalo event di exit atau eventnya window closed
        break   #maka jadi False
    if event=='-TOMBOL1-':   #Ngebaca kalo si tombol1 dipencet
        text=values['-INPUT-']
        window['-TEXT-'].update(text)

window.close()  #tutup window