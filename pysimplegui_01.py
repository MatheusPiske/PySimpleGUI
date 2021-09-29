# PySimpleGUI é uma biblioteca de interface gráfica;from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key="usuario", size=(20,1))],
    [sg.Text('Senha'), sg.Input(key="senha",password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)
#Ler os eventos
while True:
    # UNPACKING: duas variáveis separadas recebendo valores.
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Matheus' and valores['senha'] == "123456":
            print('Bem vindo à interface!')