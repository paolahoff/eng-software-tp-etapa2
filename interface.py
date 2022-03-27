import PySimpleGUI as sg
import classes

sg.theme('Dark')
col_entradas = [
    [sg.Text('Usuario:',size=10,justification='r'),sg.InputText(key='usuario')],
    [sg.Text('Senha:',size=10,justification='r'),sg.InputText(key='senha')],
]
col_botoes = [
    [sg.Button('Logar',key='logar'), sg.Button('Nova conta',key='nova conta')]
]

col_opcoes = [
    [sg.Text('Escolha tipo de conta')],
    [sg.Radio('Jogador',group_id='1', key='Jogador'),
     sg.Radio('Provedor',group_id='1', key='Provedor'),
     sg.Radio('Desenvolvedor',group_id='1', key='Desenvolvedor')]
]

layout = [
    [sg.Column(col_opcoes,key='opcoes',visible=False,justification='c',element_justification='c',vertical_alignment='c')],
    [sg.Column(col_entradas, key='entradas')],
    [sg.Column(col_botoes,key='botoes'),sg.Button('Criar',key='criar',visible=False)]

]


window = sg.Window('Cloud Gaming login',layout=layout)


def logar(login, senha):
    for conta in classes.lista_de_contas:
        if [login, senha] == [conta.login, conta.senha]:
            print('logado')
            return conta
    else:
        print('Usuario ou senha incorretos')
        return None

while True:
    event,values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'nova conta':
        window['botoes'].update(visible=False)
        window['opcoes'].update(visible=True)
        window['criar'].update(visible=True)

    if event == 'criar':
        if values['usuario']== '' or values['senha'] == '':
            if values['usuario']== '':
                    window['usuario'].update(background_color='red')

            if values['senha'] == '':
                window['senha'].update(background_color='red')
        else:
            login = values['usuario']
            if login in [conta.login for conta in classes.lista_de_contas]:
                sg.Popup('Login ja usado')
                window['usuario'].update(background_color='red')
                window['senha'].update(background_color='')
                continue

            else:
                senha = values['senha']
                tipos = {'Provedor': classes.ContaProvedor(), 'Desenvolvedor': classes.ContaDesenvolvedor(), 'Jogador': classes.ContaJogador()}
                categorias = ['Provedor','Desenvolvedor','Jogador']
                for x in categorias:
                    if values[x]:
                        tipos[x].criar_conta(login, senha)
                window['botoes'].update(visible=True)
                window['opcoes'].update(visible=False)
                window['criar'].update(visible=False)

    if event == 'logar':
        logar(values['usuario'],values['senha'])







