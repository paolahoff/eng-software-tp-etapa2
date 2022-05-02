from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide2.QtCore import QEvent, QObject
from ui_interface import Ui_MainWindow
import sys
import classes

classes.inicializar_dados()


# Mudei a biblioteca da interface pra usar o programinha de arrastar bloquinhos,
# adicionei no git o arquivo que ele gera e a conversao pra python que a biblioteca gera
# pip install PySide2

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Cloud Gaming')
        self.conta = None
        self.nome_maquina = None
        self.nome_jogo = None

        # botoes da pagina de login
        self.login_button.clicked.connect(self.logar)
        self.new_account_button_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        # botoes cadastro conta
        self.voltar_cadastro_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        self.create_account_button.clicked.connect(self.criar_conta)

        # botoes jogador
        self.sairjogador.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_login))
        # precisamos definir como vao funcionar as operacoes aqui de baixo para poder fazer o layout delas
        self.buscar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_buscar))  # chamar a funçao de pesquisar jogo
        self.alugar_maquina_button.clicked.connect(self.alugar_maquina)  # chamar a funçao de alugar maquina
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
        self.cadastrar_jogo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_jogo))
        self.listar_jogos.clicked.connect(self.listar_jogos_desenvolvedor)
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
        self.adicionar_jogo_button.clicked.connect(self.adicionar_jogo)
        self.salvar_edit_maquina_button.clicked.connect(self.salvar_edit_maquina)
        # buscar
        self.voltar_busca.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_jogador))
        # alugar maquina
        self.lista_jogos_alugar.currentTextChanged.connect(self.alterar_maquinas_disponiveis)
        self.voltar_alugar_maquina.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_jogador))
        self.alugar_button.clicked.connect(self.alugar)

        # cadastrar Jogo
        self.voltar_cadastrar_jogo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_desenvolvedor))
        self.cadastrar_jogo_button.clicked.connect(self.cadastro_jogo)
        # lista de jogos
        self.voltar_lista_jogos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_desenvolvedor))
        self.excluir_jogo_button.clicked.connect(self.excluir_jogo)
        self.editar_jogo_button.clicked.connect(self.editar_jogo)
        #editar jogo
        self.voltar_editar_jogo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_lista_jogo))
        self.salvar_edit_jogo_button.clicked.connect(self.salvar_edit_jogo)
    def alugar(self):
        if(self.conta.alugar_maquina(self.lista_maquinas_aluguel.currentText(),self.lista_jogos_alugar.currentText(), self.horas.value())):
            msg = QMessageBox()
            msg.setText('Alugado')
            msg.exec_()
            return
    def alugar_maquina(self):
        for jogo in classes.lista_de_jogos:
            self.lista_jogos_alugar.addItem(jogo.titulo)
        self.Pages.setCurrentWidget(self.pg_alugar_maquina)
    def salvar_edit_jogo(self):
        if self.novo_radio_jogo_alta.isChecked():
            especificacao = 'Alta'
        elif self.novo_radio_jogo_media.isChecked():
            especificacao = 'Media'
        elif self.novo_radio_jogo_baixa.isChecked():
            especificacao = 'Baixa'
        else:
            msg = QMessageBox()
            msg.setText('Selecione uma especificacao')
            msg.exec_()
            return
        if self.novo_titulo_input.text() != '':
            try:
                valor = float(self.novo_valor_jogo.text())
            except ValueError:
                msg = QMessageBox()
                msg.setText('entre um valor valido')
                msg.exec_()
                return
            self.conta.editar_jogo(self.nome_jogo, especificacao, valor)
        else:
            msg = QMessageBox()
            msg.setText('Escolha um titulo para o jogo')
            msg.exec_()
            return
        pass

        pass
    def salvar_edit_maquina(self):
        if self.radio_alta_edit.isChecked():
            especificacao = 'Alta'
        elif self.radio_media_edit.isChecked():
            especificacao = 'Media'
        elif self.radio_media_edit.isChecked():
            especificacao = 'Baixa'
        else:
            msg = QMessageBox()
            msg.setText('Selecione uma especificacao')
            msg.exec_()
            return
        self.conta.editar_maquina(self.nome_maquina, especificacao, self.porcentagem_input.value())
        return

    def excluir_jogo(self):
        self.conta.remover_jogo(self.lista_jogos_desenvolvedor.currentText())
        self.lista_jogos_desenvolvedor.removeItem(self.lista_jogos_desenvolvedor.currentIndex())
        pass

    def editar_jogo(self):
        self.nome_jogo=self.lista_jogos_desenvolvedor.currentText()
        self.Pages.setCurrentWidget(self.pg_editar_jogo)

    def listar_jogos_desenvolvedor(self):
        jogos = self.conta.listar_jogos()
        for jogo in jogos:
            print(jogo)
            self.lista_jogos_desenvolvedor.addItem(jogo)
        self.Pages.setCurrentWidget(self.pg_lista_jogo)

    def cadastro_jogo(self):
        if self.radio_jogo_alta.isChecked():
            especificacao = 'Alta'
        elif self.radio_jogo_media.isChecked():
            especificacao = 'Media'
        elif self.radio_jogo_baixa.isChecked():
            especificacao = 'Baixa'
        else:
            msg = QMessageBox()
            msg.setText('Selecione uma especificacao')
            msg.exec_()
            return
        if self.titulo_input.text() != '':
            try:
                valor = float(self.valor_jogo.text())
            except ValueError:
                msg = QMessageBox()
                msg.setText('entre um valor valido')
                msg.exec_()
                return
            self.conta.cadastrar_jogo(self.titulo_input.text(),especificacao, valor)
        else:
            msg = QMessageBox()
            msg.setText('Escolha um titulo para o jogo')
            msg.exec_()
            return
        pass

    def adicionar_jogo(self):
        nome_jogo = self.lista_jogos_adicionar.currentText()

        self.conta.cadastrar_jogo(self.nome_maquina,nome_jogo)

        maquina = self.conta.buscar_maquina_listada(self.nome_maquina)

        print(self.nome_maquina,nome_jogo,maquina.jogos)
        msg = QMessageBox()
        msg.setText('Jogo adicionado')
        msg.exec_()
        return

    def closeEvent(self, event):
        if event.type() == QEvent.Close:
            exit_question = QMessageBox.question(self, "Aviso de Saida", "Você realmente deseja sair?",
                                                 QMessageBox.Yes | QMessageBox.No)
            classes.salvar_dados()
            if exit_question == QMessageBox.Yes:
                event.accept()
                return True
            if exit_question == QMessageBox.No:
                event.ignore()
                return True
        else:
            event.ignore()
            return True

    def a_definir(self):
        pass

    def alterar_maquinas_disponiveis(self):
        jogo_nome = self.lista_jogos_alugar.currentText()
        lista = self.conta.buscar_maquinas_com_jogo(jogo_nome)
        for item in lista:
            self.lista_maquinas_aluguel.addItem(item)

    def editar_maquina(self):
        self.Pages.setCurrentWidget(self.pg_editar)
        self.nome_maquina = self.lista_maquinas_provedor.currentText()
        self.nome_maquina_editada.setText(self.nome_maquina)

        for jogo in classes.lista_de_jogos:
            self.lista_jogos_adicionar.addItem(jogo.titulo)

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
            especificacao = 'Alta'
        elif self.radio_media.isChecked():
            especificacao = 'Media'
        elif self.radio_media.isChecked():
            especificacao = 'Baixa'
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
