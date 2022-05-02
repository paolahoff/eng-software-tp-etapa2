from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem

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
        self.new_account_button_2.clicked.connect(self.new_account)

        # botoes cadastro conta
        self.voltar_cadastro_button.clicked.connect(self.voltar_cadastro)
        self.create_account_button.clicked.connect(self.criar_conta)

        # botoes jogador
        self.sairjogador_button.clicked.connect(self.sair )
        self.buscar_button.clicked.connect(self.buscar)
        self.alugar_maquina_button.clicked.connect(self.alugar_maquina)
        self.abastecer_creditos_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_abastecer_creditos))
        self.relatorio_jogador_button.clicked.connect(self.gerar_relatorio)  # chamar a funcao de relatorio

        # botoes provedor
        self.sairprovedor_button.clicked.connect(self.sair)
        self.cadastrar_maquina_button.clicked.connect(self.cadastrar_maquina)
        self.listar_maquinas_button.clicked.connect(self.listar_maquinas)
        self.relatorio_provedor_button.clicked.connect(self.gerar_relatorio)  # chamar a funcao de relatorio
        self.sacar_provedor_button.clicked.connect(self.sacar)  # sacar vai ser só um popup de quanto ele sacou?

        # botoes desenvolvedor
        self.sairdesenvolvedor_button.clicked.connect(self.sair)
        self.sacar_desenvolvedor_button.clicked.connect(self.sacar)
        self.cadastrar_jogo_button_2.clicked.connect(self.cadastrar_jogo)
        self.listar_jogos_button.clicked.connect(self.listar_jogos_desenvolvedor)
        self.relatorio_desenvolvedor_button.clicked.connect(self.gerar_relatorio)

        # botoes cadastro maquina
        self.voltar_cadastrar_maquina_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_provedor))
        self.cadastrar_button.clicked.connect(self.cadastro_maquina)

        # lista de maquinas
        self.voltar_lista_maquinas_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_provedor))
        self.excluir_maquina_button.clicked.connect(self.excluir_maquina)
        self.editar_maquina_button.clicked.connect(self.editar_maquina)

        # editar maquina
        self.voltar_edit_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listaMaquinas))
        self.adicionar_jogo_button.clicked.connect(self.adicionar_jogo)
        self.salvar_edit_maquina_button.clicked.connect(self.salvar_edit_maquina)
        # buscar
        self.voltar_busca_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_jogador))
        self.busca_lista_maquina_button.clicked.connect(self.tabela_maquinas_com_o_jogo)
        self.busca_lista_jogos_button.clicked.connect(self.tabela_jogos_da_maquina)

        # alugar maquina
        self.lista_jogos_alugar.currentTextChanged.connect(self.alterar_maquinas_disponiveis)
        self.voltar_alugar_maquina_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_jogador))
        self.alugar_button.clicked.connect(self.alugar)

        # cadastrar Jogo
        self.voltar_cadastrar_jogo_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_desenvolvedor))
        self.cadastrar_jogo_button.clicked.connect(self.cadastro_jogo)
        # lista de jogos
        self.voltar_lista_jogos_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_desenvolvedor))
        self.excluir_jogo_button.clicked.connect(self.excluir_jogo)
        self.editar_jogo_button.clicked.connect(self.editar_jogo)
        #editar jogo
        self.voltar_editar_jogo_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_lista_jogo))
        self.salvar_edit_jogo_button.clicked.connect(self.salvar_edit_jogo)

        #abastecer credito
        self.comprar_creditos_button.clicked.connect(self.abastecer_creditos)
        self.voltar_abastecer_creditos_button.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_jogador))

        # relatorio
        self.voltar_relatorio_button.clicked.connect(self.voltar_relatorio)
    def new_account(self):
        self.reset_inputs()
        self.Pages.setCurrentWidget(self.pg_cadastro)
    def voltar_cadastro(self):
        self.reset_inputs()
        self.Pages.setCurrentWidget(self.pg_login)
    def cadastrar_maquina(self):
        self.reset_inputs()
        self.Pages.setCurrentWidget(self.pg_cadastro_maquina)
    def cadastrar_jogo(self):
        self.reset_inputs()
        self.Pages.setCurrentWidget(self.pg_cadastro_jogo)
    def sair(self):
        self.reset_inputs()
        self.Pages.setCurrentWidget(self.pg_login)
    def voltar_relatorio(self):
        if self.conta.tipo_da_conta == 'jogador':
            self.Pages.setCurrentWidget(self.pg_jogador)
        elif self.conta.tipo_da_conta == 'provedor':
            self.Pages.setCurrentWidget(self.pg_provedor)
        elif self.conta.tipo_da_conta == 'desenvolvedor':
            self.Pages.setCurrentWidget(self.pg_desenvolvedor)
    def buscar(self):
        self.lista_de_jogos.clear()
        for jogo in classes.lista_de_jogos:
            self.lista_de_jogos.addItem(jogo.titulo)
        self.lista_de_maquinas.clear()
        for maquina in classes.lista_de_maquinas:
            self.lista_de_maquinas.addItem(maquina.nome)
        self.tableWidget.clear()
        self.Pages.setCurrentWidget(self.pg_buscar)
    def sacar(self):
        ganhos = self.conta.sacar_ganhos()
        msg = QMessageBox()
        msg.setText(f'Sacados:{ganhos}')
        msg.exec_()
    def tabela_maquinas_com_o_jogo(self):
        nome_jogo=self.lista_de_jogos.currentText()
        lista = self.conta.buscar_maquinas_com_jogo(nome_jogo)
        mapa = self.conta.gerar_tabela_maquinas(lista)
        self.tableWidget.setRowCount(len(mapa))
        self.tableWidget.setColumnCount(len(mapa[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(mapa[0].keys()))
        r = 0
        for x in mapa:
            self.tableWidget.setItem(r, 0, QTableWidgetItem(x['nome']))
            self.tableWidget.setItem(r, 1, QTableWidgetItem(x['especificacao']))
            r+=1
    def tabela_jogos_da_maquina(self):
        nome_maquina = self.lista_de_maquinas.currentText()
        lista = self.conta.buscar_jogos_na_maquina(nome_maquina)
        mapa = self.conta.gerar_tabela_jogos(lista)
        self.tableWidget.setRowCount(len(mapa))
        self.tableWidget.setColumnCount(len(mapa[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(mapa[0].keys()))
        r = 0
        for x in mapa:
            self.tableWidget.setItem(r, 0, QTableWidgetItem(x['titulo']))
            self.tableWidget.setItem(r, 1, QTableWidgetItem(str(x['valor'])))
            r += 1
    def abastecer_creditos(self):
        self.conta.abastecer_creditos(self.quantidade_creditos.value())
        msg = QMessageBox()
        msg.setText('Compra efetuada')
        msg.exec_()
        return

    def gerar_relatorio(self):
        if self.conta.tipo_da_conta == 'jogador':
            relatorio = self.conta.gerar_relatorio()
            q_linhas = len(relatorio)
            if q_linhas == 0:
                self.Pages.setCurrentWidget(self.pg_relatorio)
                return
            else:
                q_colunas = len(relatorio[0])
            self.tableWidget_2.setRowCount(q_linhas)
            self.tableWidget_2.setColumnCount(q_colunas)
            self.tableWidget_2.setHorizontalHeaderLabels(list(relatorio[0].keys()))
            r = 0
            for x in relatorio:
                self.tableWidget_2.setItem(r, 0, QTableWidgetItem(x['Nome']))
                self.tableWidget_2.setItem(r, 1, QTableWidgetItem(str(x['Creditos totais'])))
                self.tableWidget_2.setItem(r, 2, QTableWidgetItem(str(x['Saldo de creditos'])))
                self.tableWidget_2.setItem(r, 3, QTableWidgetItem(str(x['Horas jogadas'])))
                r += 1

        elif self.conta.tipo_da_conta == 'desenvolvedor':
            relatorio = self.conta.gerar_relatorio()
            q_linhas = len(relatorio)
            if q_linhas == 0:
                self.Pages.setCurrentWidget(self.pg_relatorio)
                return
            else:
                q_colunas = len(relatorio[0])
            self.tableWidget_2.setRowCount(q_linhas)
            self.tableWidget_2.setColumnCount(q_colunas)
            self.tableWidget_2.setHorizontalHeaderLabels(list(relatorio[0].keys()))
            r = 0
            for x in relatorio:
                self.tableWidget_2.setItem(r, 0, QTableWidgetItem(x['Titulo']))
                self.tableWidget_2.setItem(r, 1, QTableWidgetItem(str(x['Tempo jogado'])))
                self.tableWidget_2.setItem(r, 2, QTableWidgetItem(str(x['Tempo total'])))
                self.tableWidget_2.setItem(r, 3, QTableWidgetItem(str(x['Jogadores'])))
                r += 1

        elif self.conta.tipo_da_conta == 'provedor':
            relatorio = self.conta.gerar_relatorio()
            q_linhas = len(relatorio)
            if q_linhas == 0:
                self.Pages.setCurrentWidget(self.pg_relatorio)
                return
            else:
                q_colunas = len(relatorio[0])
            self.tableWidget_2.setRowCount(q_linhas)
            self.tableWidget_2.setColumnCount(q_colunas)
            self.tableWidget_2.setHorizontalHeaderLabels(list(relatorio[0].keys()))
            r = 0
            for x in relatorio:
                self.tableWidget_2.setItem(r, 0, QTableWidgetItem(x['Nome']))
                self.tableWidget_2.setItem(r, 1, QTableWidgetItem(str(x['Horas em uso'])))
                self.tableWidget_2.setItem(r, 2, QTableWidgetItem(str(x['Ganhos'])))
                self.tableWidget_2.setItem(r, 3, QTableWidgetItem(str(x['Usuarios'])))
                r += 1
        self.Pages.setCurrentWidget(self.pg_relatorio)
        return
    def alugar(self):
        if(self.conta.alugar_maquina(self.lista_maquinas_aluguel.currentText(),self.lista_jogos_alugar.currentText(), self.horas.value())):
            msg = QMessageBox()
            msg.setText('Alugado')
            msg.exec_()
            return
        else:
            msg = QMessageBox()
            msg.setText('Creditos Insuficientes')
            msg.exec_()
    def alugar_maquina(self):
        self.lista_jogos_alugar.clear()
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
        try:
            valor = float(self.novo_valor_jogo.text())
        except ValueError:
            msg = QMessageBox()
            msg.setText('entre um valor valido')
            msg.exec_()
            return
        self.conta.editar_jogo(self.nome_jogo, especificacao, valor)

        return
    def reset_inputs(self):
        self.novo_valor_jogo.clear()
        self.titulo_input.clear()
        self.valor_jogo.clear()
        self.nome_maquina_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.password_input_2.clear()
        self.username_input_2.clear()

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
        msg = QMessageBox()
        msg.setText('Máquina editada')
        msg.exec_()
        return

    def excluir_jogo(self):
        self.conta.remover_jogo(self.lista_jogos_desenvolvedor.currentText())
        self.lista_jogos_desenvolvedor.removeItem(self.lista_jogos_desenvolvedor.currentIndex())
        msg = QMessageBox()
        msg.setText('Jogo excluido')
        msg.exec_()
        return
        pass

    def editar_jogo(self):
        self.reset_inputs()
        self.nome_jogo=self.lista_jogos_desenvolvedor.currentText()
        self.Pages.setCurrentWidget(self.pg_editar_jogo)

    def listar_jogos_desenvolvedor(self):
        jogos = self.conta.listar_jogos()
        self.lista_jogos_desenvolvedor.clear()
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
            msg = QMessageBox()
            msg.setText('Jogo cadastrado')
            msg.exec_()
            return
        else:
            msg = QMessageBox()
            msg.setText('Escolha um titulo para o jogo')
            msg.exec_()
            return



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
        self.lista_maquinas_aluguel.clear()
        for item in lista:
            self.lista_maquinas_aluguel.addItem(item)

    def editar_maquina(self):
        self.Pages.setCurrentWidget(self.pg_editar)
        self.nome_maquina = self.lista_maquinas_provedor.currentText()
        self.nome_maquina_editada.setText(self.nome_maquina)
        self.lista_jogos_adicionar.clear()
        for jogo in classes.lista_de_jogos:
            self.lista_jogos_adicionar.addItem(jogo.titulo)

    def excluir_maquina(self):
        self.conta.remover_maquina(self.lista_maquinas_provedor.currentText())
        self.lista_maquinas_provedor.removeItem(self.lista_maquinas_provedor.currentIndex())
        msg = QMessageBox()
        msg.setText('Maquina excluida com sucesso')
        msg.exec_()
        return

    def listar_maquinas(self):
        self.lista_maquinas_provedor.clear()
        maquinas = self.conta.listar_maquinas()
        for maquina in maquinas:
            self.lista_maquinas_provedor.addItem(maquina)
        self.Pages.setCurrentWidget(self.pg_listaMaquinas)

    def cadastro_maquina(self):
        if self.radio_alta.isChecked():
            especificacao = 'Alta'
        elif self.radio_media.isChecked():
            especificacao = 'Media'
        elif self.radio_baixa.isChecked():
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
        msg = QMessageBox()
        msg.setText('Maquina cadastrada')
        msg.exec_()
        return

    def logar(self):
        for conta in classes.lista_de_contas:
            print(conta.login)
            if [self.username_input.text(), self.password_input.text()] == [conta.login, conta.senha]:
                print(f'logado como: {self.username_input.text()}')
                if conta.tipo_da_conta == 'jogador':
                    self.mostrador_nome_jogador.setText(self.username_input.text())
                    self.Pages.setCurrentWidget(self.pg_jogador)
                    self.conta = conta

                    return
                elif conta.tipo_da_conta == 'provedor':
                    self.mostrador_nome_provedor.setText(self.username_input.text())
                    self.Pages.setCurrentWidget(self.pg_provedor)
                    self.conta = conta

                    return
                elif conta.tipo_da_conta == 'desenvolvedor':
                    self.mostrador_nome_desenvolvedor.setText(self.username_input.text())
                    self.Pages.setCurrentWidget(self.pg_desenvolvedor)
                    self.conta = conta

                    return

        msg = QMessageBox()
        msg.setText('Login falhou, usuario ou senha incorretos')
        msg.exec_()
        return
        return None

    def criar_conta(self):

        username = self.username_input_2.text()
        senha = self.password_input_2.text()
        if username == '' or senha == '':
            msg = QMessageBox()
            msg.setText('Digite um nome de usuario e senha')
            msg.exec_()
            return
        else:
            if username in [conta.login for conta in classes.lista_de_contas]:
                msg = QMessageBox()
                msg.setText('Nome de usuario ja usado')
                msg.exec_()
                return

            else:

                if self.radio_jogador.isChecked():
                    classes.ContaJogador().criar_conta(username, senha)
                    self.password_input_2.setText('')
                    self.username_input_2.setText('')
                    msg = QMessageBox()                             #basicamente isso para retornar após pop up
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
