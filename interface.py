import PySimpleGUI as sg
import classes

sg.theme('Dark')
col_entradas = [
    [sg.Text('Usuario:', size=10, justification='r'), sg.InputText(key='usuario')],
    [sg.Text('Senha:', size=10, justification='r'), sg.InputText(key='senha')],
]
col_botoes = [
    [sg.Button('Logar', key='logar'), sg.Button('Nova conta', key='nova conta')]
]

col_opcoes = [
    [sg.Text('Escolha tipo de conta')],
    [sg.Radio('Jogador', group_id='1', key='Jogador'),
     sg.Radio('Provedor', group_id='1', key='Provedor'),
     sg.Radio('Desenvolvedor', group_id='1', key='Desenvolvedor')]
]
col_cadastro_maquina = [
    [sg.Text('Especificação da maquina (Alta,Media,Baixa) ', size=40, ), sg.Text('%', size=2)],
    [sg.InputText(key='especificacao', size=45), sg.InputText(key='porcentagem', size=2)],
    [sg.Button('cadastar', key='cadastrar')]
]


layout = [
    [sg.Text('Login', key='cabecalho'),
     sg.Column(col_opcoes, key='opcoes', visible=False, justification='c', element_justification='c')],
    [sg.Column(col_entradas, key='entradas')],
    [sg.Column(col_botoes, key='botoes'), sg.Button('Criar', key='criar', visible=False),
     sg.Button('cadastrar maquina', key='cadastrar maquina', visible=False),
     sg.Button('sair',key='sair',visible=False),
     sg.Column(col_cadastro_maquina, key='cadastro_maquina', visible=False)]

]

window = sg.Window('Cloud Gaming login', layout=layout)


def logar(login, senha):
    for conta in classes.lista_de_contas:
        print(conta.login)
        if [login, senha] == [conta.login, conta.senha]:
            print('logado')
            return conta
    else:
        print('Usuario ou senha incorretos')
        return None


while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'nova conta':
        window['usuario'].update('')
        window['senha'].update('')
        window['botoes'].update(visible=False)
        window['opcoes'].update(visible=True)
        window['criar'].update(visible=True)
        window['cabecalho'].update(visible=False)

    if event == 'criar':
        if values['usuario'] == '' or values['senha'] == '':
            if values['usuario'] == '':
                window['usuario'].update(background_color='red')

            if values['senha'] == '':
                window['senha'].update(background_color='red')
        else:
            window['usuario'].update('', background_color=sg.theme_background_color())
            window['senha'].update('', background_color=sg.theme_background_color())
            login = values['usuario']
            if login in [conta.login for conta in classes.lista_de_contas]:
                sg.Popup('Login ja usado')
                window['usuario'].update(background_color='red')
                window['senha'].update(background_color=sg.theme_background_color())
                continue

            else:
                senha = values['senha']
                tipos = {'Provedor': classes.ContaProvedor(), 'Desenvolvedor': classes.ContaDesenvolvedor(),
                         'Jogador': classes.ContaJogador()}
                categorias = ['Provedor', 'Desenvolvedor', 'Jogador']
                for x in categorias:
                    if values[x]:
                        tipos[x].criar_conta(login, senha)
                window['botoes'].update(visible=True)
                window['opcoes'].update(visible=False)
                window['criar'].update(visible=False)
                window['cabecalho'].update(visible=True)

    if event == 'logar':
        conta = logar(values['usuario'], values['senha'])
        if conta is not None:
            window['entradas'].update(visible=False)
            window['botoes'].update(visible=False)
            if conta.tipo_da_conta == 'provedor':
                window['cabecalho'].update('Conta Provedor', visible=True)
                window['cadastrar maquina'].update(visible=True)
                print(conta)
            if conta.tipo_da_conta == 'desenvolvedor':
                window['cabecalho'].update('Conta desenvolvedor',visible=True)
                print(conta)
            if conta.tipo_da_conta == 'jogador':
                window['cabecalho'].update('Conta jogador',visible=True)
                print(conta)
            window['sair'].update(visible=True)

    if event == 'cadastrar maquina':
        window['cadastrar maquina'].update(visible=False)
        window['cadastro_maquina'].update(visible=True)

    if event == 'cadastrar':
        conta.cadastrar_maquina(values['especificacao'], int(values['porcentagem']) / 100)
        window['cadastrar maquina'].update(visible=True)
        window['cadastro_maquina'].update(visible=False)

    if event == 'sair':
        window['cabecalho'].update(visible=False)
        window['entradas'].update(visible=True)
        window['usuario'].update('', visible=True)
        window['senha'].update('', visible=True)
        window['botoes'].update(visible=True)
        window['sair'].update(visible=False)
        if conta.tipo_da_conta == 'provedor':
            window['cadastrar maquina'].update(visible=False)
            print('saindao de ',conta)
        if conta.tipo_da_conta == 'desenvolvedor':
            print('saindao de ',conta)
        if conta.tipo_da_conta == 'jogador':
            print('saindao de ',conta)
