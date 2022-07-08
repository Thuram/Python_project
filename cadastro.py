from ctypes.wintypes import SIZE
from PySimpleGUI import PySimpleGUI as sg

#Layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario'), sg.Sizer(h_pixels,v_pixels)=(20,1)],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*'), sg.Sizer(h_pixels,v_pixels)=(20,1)],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entar')]
]
#Janela
janela = sg.Window('Tela de login', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'gustavo' and valores['senha'] == '123456':
            print('Bem vindo')