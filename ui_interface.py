# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_23 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.Pages.setFrameShape(QFrame.NoFrame)
        self.pg_login = QWidget()
        self.pg_login.setObjectName(u"pg_login")
        self._2 = QVBoxLayout(self.pg_login)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pg_login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 200))
        self.frame_2.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(32)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_input = QLineEdit(self.frame_2)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setFrame(True)

        self.verticalLayout_4.addWidget(self.username_input)

        self.password_input = QLineEdit(self.frame_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password_input)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.login_button = QPushButton(self.splitter)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.splitter.addWidget(self.login_button)
        self.new_account_button_2 = QPushButton(self.splitter)
        self.new_account_button_2.setObjectName(u"new_account_button_2")
        self.new_account_button_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.splitter.addWidget(self.new_account_button_2)

        self.verticalLayout_2.addWidget(self.splitter)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self._2.addWidget(self.frame)

        self.Pages.addWidget(self.pg_login)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.horizontalLayout_14 = QHBoxLayout(self.pg_cadastro)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.pg_cadastro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 200))
        self.frame_4.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_6.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_jogador = QRadioButton(self.frame_4)
        self.radio_jogador.setObjectName(u"radio_jogador")
        self.radio_jogador.setStyleSheet(u"")
        self.radio_jogador.setChecked(False)
        self.radio_jogador.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.radio_jogador)

        self.radio_provedor = QRadioButton(self.frame_4)
        self.radio_provedor.setObjectName(u"radio_provedor")

        self.horizontalLayout.addWidget(self.radio_provedor)

        self.radio_desenvolvedor = QRadioButton(self.frame_4)
        self.radio_desenvolvedor.setObjectName(u"radio_desenvolvedor")

        self.horizontalLayout.addWidget(self.radio_desenvolvedor)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.username_input_2 = QLineEdit(self.frame_4)
        self.username_input_2.setObjectName(u"username_input_2")
        self.username_input_2.setFrame(True)

        self.verticalLayout_9.addWidget(self.username_input_2)

        self.password_input_2 = QLineEdit(self.frame_4)
        self.password_input_2.setObjectName(u"password_input_2")
        self.password_input_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.password_input_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.splitter_2 = QSplitter(self.frame_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.voltar_cadastro_button = QPushButton(self.splitter_2)
        self.voltar_cadastro_button.setObjectName(u"voltar_cadastro_button")
        self.voltar_cadastro_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.splitter_2.addWidget(self.voltar_cadastro_button)
        self.create_account_button = QPushButton(self.splitter_2)
        self.create_account_button.setObjectName(u"create_account_button")
        self.create_account_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.splitter_2.addWidget(self.create_account_button)

        self.verticalLayout_8.addWidget(self.splitter_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_14.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_jogador = QWidget()
        self.pg_jogador.setObjectName(u"pg_jogador")
        self.verticalLayout_11 = QVBoxLayout(self.pg_jogador)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.pg_jogador)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(600, 300))
        self.frame_6.setLayoutDirection(Qt.RightToLeft)
        self.frame_6.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777213, 16777215))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_12.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 60, -1, 60)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.abastecer_creditos = QPushButton(self.frame_6)
        self.abastecer_creditos.setObjectName(u"abastecer_creditos")
        self.abastecer_creditos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.abastecer_creditos)

        self.alugar_maquina = QPushButton(self.frame_6)
        self.alugar_maquina.setObjectName(u"alugar_maquina")
        self.alugar_maquina.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.alugar_maquina)

        self.pesquisar_jogo = QPushButton(self.frame_6)
        self.pesquisar_jogo.setObjectName(u"pesquisar_jogo")
        self.pesquisar_jogo.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.pesquisar_jogo)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.relatorio_jogador = QPushButton(self.frame_6)
        self.relatorio_jogador.setObjectName(u"relatorio_jogador")
        self.relatorio_jogador.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_7.addWidget(self.relatorio_jogador)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_12.addLayout(self.verticalLayout)

        self.sairjogador = QPushButton(self.frame_6)
        self.sairjogador.setObjectName(u"sairjogador")
        self.sairjogador.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_12.addWidget(self.sairjogador)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.Pages.addWidget(self.pg_jogador)
        self.pg_provedor = QWidget()
        self.pg_provedor.setObjectName(u"pg_provedor")
        self.verticalLayout_17 = QVBoxLayout(self.pg_provedor)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pg_provedor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(600, 300))
        self.frame_8.setLayoutDirection(Qt.RightToLeft)
        self.frame_8.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777213, 16777215))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_15.addWidget(self.label_4)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(30)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 60, -1, 60)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(30)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.listar_maquinas_button = QPushButton(self.frame_8)
        self.listar_maquinas_button.setObjectName(u"listar_maquinas_button")
        font = QFont()
        self.listar_maquinas_button.setFont(font)
        self.listar_maquinas_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_9.addWidget(self.listar_maquinas_button)

        self.cadastrar_maquina = QPushButton(self.frame_8)
        self.cadastrar_maquina.setObjectName(u"cadastrar_maquina")
        self.cadastrar_maquina.setFont(font)
        self.cadastrar_maquina.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_9.addWidget(self.cadastrar_maquina)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(30)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sacar = QPushButton(self.frame_8)
        self.sacar.setObjectName(u"sacar")
        self.sacar.setFont(font)
        self.sacar.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_10.addWidget(self.sacar)

        self.relatorio_provedor = QPushButton(self.frame_8)
        self.relatorio_provedor.setObjectName(u"relatorio_provedor")
        self.relatorio_provedor.setFont(font)
        self.relatorio_provedor.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_10.addWidget(self.relatorio_provedor)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)

        self.sairprovedor = QPushButton(self.frame_8)
        self.sairprovedor.setObjectName(u"sairprovedor")
        self.sairprovedor.setFont(font)
        self.sairprovedor.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_15.addWidget(self.sairprovedor)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)


        self.horizontalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_17.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_provedor)
        self.pg_desenvolvedor = QWidget()
        self.pg_desenvolvedor.setObjectName(u"pg_desenvolvedor")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_desenvolvedor)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.pg_desenvolvedor)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(600, 300))
        self.frame_10.setLayoutDirection(Qt.RightToLeft)
        self.frame_10.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(75)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777213, 16777215))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_19.addWidget(self.label_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.relatorio_desenvolvedor = QPushButton(self.frame_10)
        self.relatorio_desenvolvedor.setObjectName(u"relatorio_desenvolvedor")
        self.relatorio_desenvolvedor.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_12.addWidget(self.relatorio_desenvolvedor)

        self.listar_jogos = QPushButton(self.frame_10)
        self.listar_jogos.setObjectName(u"listar_jogos")
        self.listar_jogos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_12.addWidget(self.listar_jogos)

        self.cadastrar_jogo = QPushButton(self.frame_10)
        self.cadastrar_jogo.setObjectName(u"cadastrar_jogo")
        self.cadastrar_jogo.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_12.addWidget(self.cadastrar_jogo)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)

        self.sairdesenvolvedor = QPushButton(self.frame_10)
        self.sairdesenvolvedor.setObjectName(u"sairdesenvolvedor")
        self.sairdesenvolvedor.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_19.addWidget(self.sairdesenvolvedor)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)


        self.horizontalLayout_11.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.Pages.addWidget(self.pg_desenvolvedor)
        self.pg_cadastro_maquina = QWidget()
        self.pg_cadastro_maquina.setObjectName(u"pg_cadastro_maquina")
        self.verticalLayout_22 = QVBoxLayout(self.pg_cadastro_maquina)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.pg_cadastro_maquina)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(600, 300))
        self.frame_12.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.radio_alta = QRadioButton(self.frame_12)
        self.radio_alta.setObjectName(u"radio_alta")
        self.radio_alta.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.radio_alta)

        self.radio_media = QRadioButton(self.frame_12)
        self.radio_media.setObjectName(u"radio_media")
        self.radio_media.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.radio_media)

        self.radio_baixa = QRadioButton(self.frame_12)
        self.radio_baixa.setObjectName(u"radio_baixa")
        self.radio_baixa.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.radio_baixa)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.nome_maquina_input = QLineEdit(self.frame_12)
        self.nome_maquina_input.setObjectName(u"nome_maquina_input")
        self.nome_maquina_input.setMaximumSize(QSize(400, 100))
        self.nome_maquina_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.nome_maquina_input)

        self.porcentagem_input = QSpinBox(self.frame_12)
        self.porcentagem_input.setObjectName(u"porcentagem_input")
        self.porcentagem_input.setMaximumSize(QSize(50, 16777215))
        self.porcentagem_input.setStyleSheet(u"")
        self.porcentagem_input.setMaximum(100)
        self.porcentagem_input.setSingleStep(5)
        self.porcentagem_input.setValue(75)

        self.horizontalLayout_19.addWidget(self.porcentagem_input)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_20.addWidget(self.pushButton_4)

        self.cadastrar_button = QPushButton(self.frame_12)
        self.cadastrar_button.setObjectName(u"cadastrar_button")
        self.cadastrar_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_20.addWidget(self.cadastrar_button)

        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setFlat(True)

        self.horizontalLayout_20.addWidget(self.pushButton_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.voltar_cadastrar_maquina = QPushButton(self.frame_12)
        self.voltar_cadastrar_maquina.setObjectName(u"voltar_cadastrar_maquina")
        self.voltar_cadastrar_maquina.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_7.addWidget(self.voltar_cadastrar_maquina)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.horizontalLayout_17.addWidget(self.frame_12)


        self.verticalLayout_22.addWidget(self.frame_11)

        self.Pages.addWidget(self.pg_cadastro_maquina)
        self.pg_listaMaquinas = QWidget()
        self.pg_listaMaquinas.setObjectName(u"pg_listaMaquinas")
        self.horizontalLayout_21 = QHBoxLayout(self.pg_listaMaquinas)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.pg_listaMaquinas)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(600, 300))
        self.frame_14.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_14)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(50)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_18.addWidget(self.label_7)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lista_maquinas_provedor = QComboBox(self.frame_14)
        self.lista_maquinas_provedor.setObjectName(u"lista_maquinas_provedor")

        self.horizontalLayout_22.addWidget(self.lista_maquinas_provedor)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.editar_maquina_button = QPushButton(self.frame_14)
        self.editar_maquina_button.setObjectName(u"editar_maquina_button")
        self.editar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_5.addWidget(self.editar_maquina_button)

        self.excluir_maquina_button = QPushButton(self.frame_14)
        self.excluir_maquina_button.setObjectName(u"excluir_maquina_button")
        self.excluir_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_5.addWidget(self.excluir_maquina_button)


        self.horizontalLayout_23.addLayout(self.verticalLayout_5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_23)

        self.voltar_lista_maquinas = QPushButton(self.frame_14)
        self.voltar_lista_maquinas.setObjectName(u"voltar_lista_maquinas")
        self.voltar_lista_maquinas.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_18.addWidget(self.voltar_lista_maquinas)


        self.verticalLayout_21.addLayout(self.verticalLayout_18)


        self.horizontalLayout_16.addWidget(self.frame_14)


        self.horizontalLayout_21.addWidget(self.frame_13)

        self.Pages.addWidget(self.pg_listaMaquinas)
        self.pg_editar = QWidget()
        self.pg_editar.setObjectName(u"pg_editar")
        self.verticalLayout_26 = QVBoxLayout(self.pg_editar)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.pg_editar)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(600, 300))
        self.frame_16.setLayoutDirection(Qt.LeftToRight)
        self.frame_16.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_25.addWidget(self.label_8)

        self.nome_maquina_editada = QLabel(self.frame_16)
        self.nome_maquina_editada.setObjectName(u"nome_maquina_editada")
        self.nome_maquina_editada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.nome_maquina_editada)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(30)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.Adicionar_jogo = QPushButton(self.frame_16)
        self.Adicionar_jogo.setObjectName(u"Adicionar_jogo")
        self.Adicionar_jogo.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_26.addWidget(self.Adicionar_jogo)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.radio_baixo_edit = QRadioButton(self.frame_16)
        self.radio_baixo_edit.setObjectName(u"radio_baixo_edit")

        self.horizontalLayout_24.addWidget(self.radio_baixo_edit)

        self.radio_media_edit = QRadioButton(self.frame_16)
        self.radio_media_edit.setObjectName(u"radio_media_edit")

        self.horizontalLayout_24.addWidget(self.radio_media_edit)

        self.radio_alta_edit = QRadioButton(self.frame_16)
        self.radio_alta_edit.setObjectName(u"radio_alta_edit")

        self.horizontalLayout_24.addWidget(self.radio_alta_edit)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)


        self.gridLayout.addLayout(self.horizontalLayout_25, 0, 0, 1, 2)

        self.salvar_edit = QPushButton(self.frame_16)
        self.salvar_edit.setObjectName(u"salvar_edit")
        self.salvar_edit.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.gridLayout.addWidget(self.salvar_edit, 1, 1, 1, 1)

        self.porcentagem_edit = QSpinBox(self.frame_16)
        self.porcentagem_edit.setObjectName(u"porcentagem_edit")
        self.porcentagem_edit.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.porcentagem_edit, 1, 0, 1, 1)


        self.horizontalLayout_26.addLayout(self.gridLayout)


        self.verticalLayout_24.addLayout(self.horizontalLayout_26)

        self.voltar_edit = QPushButton(self.frame_16)
        self.voltar_edit.setObjectName(u"voltar_edit")
        self.voltar_edit.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_24.addWidget(self.voltar_edit)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)


        self.horizontalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_26.addWidget(self.frame_15)

        self.Pages.addWidget(self.pg_editar)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.Pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.Pages.addWidget(self.page_5)

        self.verticalLayout_23.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.pushButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#fdfdfd;\">LOGIN</span></p></body></html>", None))
        self.username_input.setInputMask("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.new_account_button_2.setText(QCoreApplication.translate("MainWindow", u"New Account", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">CADASTRO</span></p></body></html>", None))
        self.radio_jogador.setText(QCoreApplication.translate("MainWindow", u"Jogador", None))
        self.radio_provedor.setText(QCoreApplication.translate("MainWindow", u"Provedor", None))
        self.radio_desenvolvedor.setText(QCoreApplication.translate("MainWindow", u"Desenvolvedor", None))
        self.username_input_2.setInputMask("")
        self.username_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.voltar_cadastro_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.create_account_button.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Jogador</span></p></body></html>", None))
        self.abastecer_creditos.setText(QCoreApplication.translate("MainWindow", u"Abastecer Creditos", None))
        self.alugar_maquina.setText(QCoreApplication.translate("MainWindow", u"Alugar Maquina", None))
        self.pesquisar_jogo.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Jogo", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.relatorio_jogador.setText(QCoreApplication.translate("MainWindow", u"Relatorio", None))
        self.sairjogador.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#f0f0f0;\">Provedor</span></p></body></html>", None))
        self.listar_maquinas_button.setText(QCoreApplication.translate("MainWindow", u"Lista de Maquinas", None))
        self.cadastrar_maquina.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Maquina", None))
        self.sacar.setText(QCoreApplication.translate("MainWindow", u"Sacar", None))
        self.relatorio_provedor.setText(QCoreApplication.translate("MainWindow", u"Relatorios", None))
        self.sairprovedor.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Desenvolvedor</span></p></body></html>", None))
        self.relatorio_desenvolvedor.setText(QCoreApplication.translate("MainWindow", u"Relatorios", None))
        self.listar_jogos.setText(QCoreApplication.translate("MainWindow", u"Listar Jogos", None))
        self.cadastrar_jogo.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Jogo", None))
        self.sairdesenvolvedor.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Cadastar Maquina</span></p></body></html>", None))
        self.radio_alta.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.radio_media.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.radio_baixa.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.nome_maquina_input.setText("")
        self.nome_maquina_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da maquina", None))
        self.porcentagem_input.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_4.setText("")
        self.cadastrar_button.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_11.setText("")
        self.voltar_cadastrar_maquina.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Lista de Maquinas</span></p></body></html>", None))
        self.editar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.excluir_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.voltar_lista_maquinas.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Editar Maquina</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.nome_maquina_editada.setText(QCoreApplication.translate("MainWindow", u"Maquina X", None))
        self.Adicionar_jogo.setText(QCoreApplication.translate("MainWindow", u"Adicionar Jogo", None))
        self.radio_baixo_edit.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.radio_media_edit.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.radio_alta_edit.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.salvar_edit.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(accessibility)
        self.porcentagem_edit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.porcentagem_edit.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.voltar_edit.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

