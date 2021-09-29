from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Seu nome:'), sg.Input(key="Usuario", size=(20,1))],
    [sg.Button('Continuar', size=(20,1))]
]

#janela
janela = sg.Window('Delivery', layout)

#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Continuar":
        if valores['Usuario'] == "Matheus":
            print("FUNCIONOU")
        else:
            print('ERRADO')
