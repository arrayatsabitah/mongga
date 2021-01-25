import PySimpleGUI as sg

kolom1=[ #semua yang ada dikurung pertama berarti bagian dari kolom 1, dan menandakan kolom1
    [sg.Text('Baris 1 kolom 1'),sg.Text('ini kolom tambahan')], #ada dua kolom soalnya ada 2 objek didalem kurung siku
    [sg.Text('Baris 2 kolom 1')] #berarti ini ada dua baris
]

kolom2=[
    [sg.Text('Baris 1 kolom 2')], #untuk setiap ada kurung siku nunjukin satu baris, kalo dimasukin sesuatu didalem kurung siku, berarti nambah kolom
    [sg.Text('Baris 2 kolom 2')],
    [sg.Button('Tombol',key='-BUT-')],
    [sg.Submit('Submit')],
    [sg.Cancel('Cancel')],
    [sg.Checkbox('Checkbox')],
    [sg.Image(key='-IMA-')],
    [sg.In(key='-IN-',size=(40,1))]
]

layout=[
    #[sg.Column(kolom1)],
    [sg.Column(kolom2)]

]

window = sg.Window('Aplikasi Latihan',layout)
print(dir(window))

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

window.close()