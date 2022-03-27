import PySimpleGUI as sg

sg.theme('Dark')
col_entradas = [
    [sg.Text('Usuario:',size=10,justification='r'),sg.InputText(key='usuario')],
    [sg.Text('Senha:',size=10,justification='r'),sg.InputText(key='senha')],
]
col_botoes = [
    [sg.Button('Logar',key='logar'), sg.Button('criar conta',key='criar conta')]
]
col_login = [
    [sg.Column(col_entradas)],
    [sg.Column(col_botoes)]
]
col_opcoes = [
    [sg.Button('Jogador', key='jogador'),
     sg.Button('Provedor', key='provedor'),
     sg.Button('Desenvolvedor', key='desenvolvedor')]
]

layout = [
    [sg.Column(col_login, key='login'),
    sg.Column(col_opcoes,key='opcoes',visible=False,justification='c',element_justification='c',vertical_alignment='c')]


]


window = sg.Window('Cloud Gaming login',layout=layout,size=(450,120))

while True:
    event,values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'criar conta':
        window['login'].update(visible=False)
        window['opcoes'].update(visible=True)


