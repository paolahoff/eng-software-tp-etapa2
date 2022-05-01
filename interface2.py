from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui_interface import Ui_MainWindow
import sys
import classes


# Mudei a biblioteca da interface pra usar o programinha de arrastar bloquinhos,
# adicionei no git o arquivo que ele gera e a conversao pra python que a biblioteca gera
# pip install PySide2

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cloud Gaming')
        self.conta = None
        # botoes da pagina de login
        self.login_button.clicked.connect(self.logar)
        self.new_account_button_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        # botoes cadastro conta
        self.voltar_cadastro_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        self.create_account_button.clicked.connect(self.criar_conta)

        # botoes jogador
        self.sairjogador.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        # precisamos definir como vao funcionar as operacoes aqui de baixo para poder fazer o layout delas
        self.pesquisar_jogo.clicked.connect(self.a_definir)  # chamar a funçao de pesquisar jogo
        self.alugar_maquina.clicked.connect(self.a_definir)  # chamar a funçao de alugar maquina
        self.abastecer_creditos.clicked.connect(self.a_definir)  # chamar a funçao de abastecer creditos
        self.relatorio_jogador.clicked.connect(self.a_definir)  # chamar a funcao de relatorio

        # botoes provedor
        self.sairprovedor.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        self.cadastrar_maquina.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_maquina))
        self.listar_maquinas_button.clicked.connect(self.listar_maquinas)
        self.relatorio_provedor.clicked.connect(self.a_definir)  # chamar a funcao de relatorio
        self.sacar.clicked.connect(self.a_definir)  # sacar vai ser só um popup de quanto ele sacou?

        # botoes desenvolvedor
        self.sairdesenvolvedor.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        self.cadastrar_jogo.clicked.connect(self.a_definir())
        self.listar_jogos.clicked.connect(self.a_definir())
        self.relatorio_desenvolvedor.clicked.connect(self.a_definir())

        # botoes cadastro maquina
        self.voltar_cadastrar_maquina.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_provedor))
        self.cadastrar_button.clicked.connect(self.cadastro_maquina)

        # lista de maquinas
        self.voltar_lista_maquinas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_provedor))
        self.excluir_maquina_button.clicked.connect(self.excluir_maquina)
        self.editar_maquina_button.clicked.connect(self.editar_maquina)

        # editar maquina
        self.voltar_edit.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listaMaquinas))


    def a_definir(self):
        pass
    def editar_maquina(self):
        self.Pages.setCurrentWidget(self.pg_editar)
        self.nome_maquina_editada.setText(self.lista_maquinas_provedor.currentText())

    def excluir_maquina(self):
        self.conta.remover_maquina(self.lista_maquinas_provedor.currentText())
        self.lista_maquinas_provedor.removeItem(self.lista_maquinas_provedor.currentIndex())

    def listar_maquinas(self):
        maquinas = self.conta.listar_maquinas()
        for maquina in maquinas:
            self.lista_maquinas_provedor.addItem(maquina)
        self.Pages.setCurrentWidget(self.pg_listaMaquinas)
    def cadastro_maquina(self):
        if self.radio_alta.isChecked():
            especificacao='Alta'
        elif self.radio_media.isChecked():
            especificacao='Media'
        elif self.radio_media.isChecked():
            especificacao='Baixa'
        else:
            msg = QMessageBox()
            msg.setText('Selecione uma especificacao')
            msg.exec_()
            return
        if self.nome_maquina_input.text() != '':
            self.conta.cadastrar_maquina(especificacao, self.porcentagem_input.value(), self.nome_maquina_input.text())
        else:
            msg = QMessageBox()
            msg.setText('Escolha um nome para a Maquina')
            msg.exec_()
            return

    def logar(self):
        for conta in classes.lista_de_contas:
            print(conta.login)
            if [self.username_input.text(), self.password_input.text()] == [conta.login, conta.senha]:
                print(f'logado como: {self.username_input.text()}')
                if conta.tipo_da_conta == 'jogador':
                    self.Pages.setCurrentWidget(self.pg_jogador)
                    self.conta = conta
                    return
                elif conta.tipo_da_conta == 'provedor':
                    self.Pages.setCurrentWidget(self.pg_provedor)
                    self.conta = conta
                    return
                elif conta.tipo_da_conta == 'desenvolvedor':
                    self.Pages.setCurrentWidget(self.pg_desenvolvedor)
                    self.conta = conta
                    return

        print('login falhou, usuario ou senha incorretos')
        return None

    def criar_conta(self):

        username = self.username_input_2.text()
        if username in [conta.login for conta in classes.lista_de_contas]:
            msg = QMessageBox()
            msg.setText('Nome de usuario ja usado')
            msg.exec_()
            return

        else:
            senha = self.password_input_2.text()
            if self.radio_jogador.isChecked():
                classes.ContaJogador().criar_conta(username, senha)
                self.password_input_2.setText('')
                self.username_input_2.setText('')
                msg = QMessageBox()
                msg.setText('Conta criada')
                msg.exec_()
                self.Pages.setCurrentWidget(self.pg_login)
            elif self.radio_provedor.isChecked():
                classes.ContaProvedor().criar_conta(username, senha)
                self.password_input_2.setText('')
                self.username_input_2.setText('')
                msg = QMessageBox()
                msg.setText('Conta criada')
                msg.exec_()
                self.Pages.setCurrentWidget(self.pg_login)
            elif self.radio_desenvolvedor.isChecked():
                classes.ContaDesenvolvedor().criar_conta(username, senha)
                self.password_input_2.setText('')
                self.username_input_2.setText('')
                msg = QMessageBox()
                msg.setText('Conta criada')
                msg.exec_()
                self.Pages.setCurrentWidget(self.pg_login)
            else:
                msg = QMessageBox()
                msg.setText('Selecione um tipo de conta')
                msg.exec_()
                return


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
