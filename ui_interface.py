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
        MainWindow.resize(1060, 594)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_47 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
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
        self.abastecer_creditos_button = QPushButton(self.frame_6)
        self.abastecer_creditos_button.setObjectName(u"abastecer_creditos_button")
        self.abastecer_creditos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.abastecer_creditos_button)

        self.alugar_maquina_button = QPushButton(self.frame_6)
        self.alugar_maquina_button.setObjectName(u"alugar_maquina_button")
        self.alugar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.alugar_maquina_button)

        self.buscar = QPushButton(self.frame_6)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_6.addWidget(self.buscar)


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
        self.verticalLayout_36 = QVBoxLayout(self.frame_16)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_27.addWidget(self.label_8)

        self.nome_maquina_editada = QLabel(self.frame_16)
        self.nome_maquina_editada.setObjectName(u"nome_maquina_editada")
        font1 = QFont()
        font1.setPointSize(12)
        self.nome_maquina_editada.setFont(font1)
        self.nome_maquina_editada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.nome_maquina_editada)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(50)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lista_jogos_adicionar = QComboBox(self.frame_16)
        self.lista_jogos_adicionar.setObjectName(u"lista_jogos_adicionar")

        self.verticalLayout_24.addWidget(self.lista_jogos_adicionar)

        self.adicionar_jogo_button = QPushButton(self.frame_16)
        self.adicionar_jogo_button.setObjectName(u"adicionar_jogo_button")
        self.adicionar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_24.addWidget(self.adicionar_jogo_button)


        self.horizontalLayout_26.addLayout(self.verticalLayout_24)

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

        self.salvar_edit_maquina_button = QPushButton(self.frame_16)
        self.salvar_edit_maquina_button.setObjectName(u"salvar_edit_maquina_button")
        self.salvar_edit_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.gridLayout.addWidget(self.salvar_edit_maquina_button, 1, 1, 1, 1)

        self.porcentagem_edit = QSpinBox(self.frame_16)
        self.porcentagem_edit.setObjectName(u"porcentagem_edit")
        self.porcentagem_edit.setMaximumSize(QSize(50, 50))

        self.gridLayout.addWidget(self.porcentagem_edit, 1, 0, 1, 1)


        self.horizontalLayout_26.addLayout(self.gridLayout)


        self.verticalLayout_25.addLayout(self.horizontalLayout_26)

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

        self.verticalLayout_25.addWidget(self.voltar_edit)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)


        self.verticalLayout_36.addLayout(self.verticalLayout_27)


        self.horizontalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_26.addWidget(self.frame_15)

        self.Pages.addWidget(self.pg_editar)
        self.pg_buscar = QWidget()
        self.pg_buscar.setObjectName(u"pg_buscar")
        self.verticalLayout_34 = QVBoxLayout(self.pg_buscar)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.pg_buscar)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(600, 300))
        self.frame_18.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.busca_lista_maquina = QPushButton(self.frame_18)
        self.busca_lista_maquina.setObjectName(u"busca_lista_maquina")
        self.busca_lista_maquina.setGeometry(QRect(41, 214, 109, 19))
        self.busca_lista_maquina.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.lista_de_jogos = QComboBox(self.frame_18)
        self.lista_de_jogos.setObjectName(u"lista_de_jogos")
        self.lista_de_jogos.setGeometry(QRect(50, 140, 73, 18))
        self.lista_de_maquinas = QComboBox(self.frame_18)
        self.lista_de_maquinas.setObjectName(u"lista_de_maquinas")
        self.lista_de_maquinas.setGeometry(QRect(420, 130, 73, 18))
        self.busca_lista_jogos = QPushButton(self.frame_18)
        self.busca_lista_jogos.setObjectName(u"busca_lista_jogos")
        self.busca_lista_jogos.setGeometry(QRect(401, 221, 84, 19))
        self.busca_lista_jogos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 80, 78, 16))
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(400, 80, 111, 16))
        self.tableWidget = QTableWidget(self.frame_18)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(170, 50, 211, 192))
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 0, 92, 29))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.voltar_busca = QPushButton(self.frame_18)
        self.voltar_busca.setObjectName(u"voltar_busca")
        self.voltar_busca.setGeometry(QRect(250, 270, 42, 19))
        self.voltar_busca.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_29.addWidget(self.frame_18)


        self.verticalLayout_34.addWidget(self.frame_17)

        self.Pages.addWidget(self.pg_buscar)
        self.pg_alugar_maquina = QWidget()
        self.pg_alugar_maquina.setObjectName(u"pg_alugar_maquina")
        self.verticalLayout_35 = QVBoxLayout(self.pg_alugar_maquina)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.pg_alugar_maquina)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(600, 300))
        self.frame_20.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_20)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_23.addWidget(self.label_13)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setSpacing(15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_14)

        self.lista_jogos_alugar = QComboBox(self.frame_20)
        self.lista_jogos_alugar.setObjectName(u"lista_jogos_alugar")
        self.lista_jogos_alugar.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_31.addWidget(self.lista_jogos_alugar)


        self.verticalLayout_33.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_15)

        self.lista_maquinas_aluguel = QComboBox(self.frame_20)
        self.lista_maquinas_aluguel.setObjectName(u"lista_maquinas_aluguel")
        self.lista_maquinas_aluguel.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_32.addWidget(self.lista_maquinas_aluguel)


        self.verticalLayout_33.addLayout(self.horizontalLayout_32)


        self.verticalLayout_23.addLayout(self.verticalLayout_33)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_49.addWidget(self.label_20)

        self.horas = QSpinBox(self.frame_20)
        self.horas.setObjectName(u"horas")
        self.horas.setMinimum(1)
        self.horas.setMaximum(5)

        self.horizontalLayout_49.addWidget(self.horas)


        self.verticalLayout_23.addLayout(self.horizontalLayout_49)

        self.alugar_button = QPushButton(self.frame_20)
        self.alugar_button.setObjectName(u"alugar_button")

        self.verticalLayout_23.addWidget(self.alugar_button)

        self.voltar_alugar_maquina = QPushButton(self.frame_20)
        self.voltar_alugar_maquina.setObjectName(u"voltar_alugar_maquina")
        self.voltar_alugar_maquina.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_23.addWidget(self.voltar_alugar_maquina)


        self.horizontalLayout_30.addWidget(self.frame_20)


        self.verticalLayout_35.addWidget(self.frame_19)

        self.Pages.addWidget(self.pg_alugar_maquina)
        self.pg_cadastro_jogo = QWidget()
        self.pg_cadastro_jogo.setObjectName(u"pg_cadastro_jogo")
        self.verticalLayout_39 = QVBoxLayout(self.pg_cadastro_jogo)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.pg_cadastro_jogo)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(600, 300))
        self.frame_22.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_22)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(48)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_16 = QLabel(self.frame_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_38.addWidget(self.label_16)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(30)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, -1, -1)
        self.radio_jogo_alta = QRadioButton(self.frame_22)
        self.radio_jogo_alta.setObjectName(u"radio_jogo_alta")
        self.radio_jogo_alta.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_34.addWidget(self.radio_jogo_alta)

        self.radio_jogo_media = QRadioButton(self.frame_22)
        self.radio_jogo_media.setObjectName(u"radio_jogo_media")
        self.radio_jogo_media.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_34.addWidget(self.radio_jogo_media)

        self.radio_jogo_baixa = QRadioButton(self.frame_22)
        self.radio_jogo_baixa.setObjectName(u"radio_jogo_baixa")
        self.radio_jogo_baixa.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_34.addWidget(self.radio_jogo_baixa)


        self.verticalLayout_37.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.titulo_input = QLineEdit(self.frame_22)
        self.titulo_input.setObjectName(u"titulo_input")
        self.titulo_input.setMaximumSize(QSize(400, 100))
        self.titulo_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.titulo_input)

        self.valor_jogo = QLineEdit(self.frame_22)
        self.valor_jogo.setObjectName(u"valor_jogo")
        self.valor_jogo.setMaximumSize(QSize(50, 16777215))
        self.valor_jogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.valor_jogo)


        self.verticalLayout_37.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_5 = QPushButton(self.frame_22)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_36.addWidget(self.pushButton_5)

        self.cadastrar_jogo_button = QPushButton(self.frame_22)
        self.cadastrar_jogo_button.setObjectName(u"cadastrar_jogo_button")
        self.cadastrar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.horizontalLayout_36.addWidget(self.cadastrar_jogo_button)

        self.pushButton_12 = QPushButton(self.frame_22)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setFlat(True)

        self.horizontalLayout_36.addWidget(self.pushButton_12)


        self.verticalLayout_37.addLayout(self.horizontalLayout_36)


        self.verticalLayout_38.addLayout(self.verticalLayout_37)

        self.voltar_cadastrar_jogo = QPushButton(self.frame_22)
        self.voltar_cadastrar_jogo.setObjectName(u"voltar_cadastrar_jogo")
        self.voltar_cadastrar_jogo.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_38.addWidget(self.voltar_cadastrar_jogo)


        self.verticalLayout_40.addLayout(self.verticalLayout_38)


        self.horizontalLayout_33.addWidget(self.frame_22)


        self.verticalLayout_39.addWidget(self.frame_21)

        self.Pages.addWidget(self.pg_cadastro_jogo)
        self.pg_lista_jogo = QWidget()
        self.pg_lista_jogo.setObjectName(u"pg_lista_jogo")
        self.verticalLayout_47 = QVBoxLayout(self.pg_lista_jogo)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.pg_lista_jogo)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(600, 300))
        self.frame_25.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_25)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setSpacing(50)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_18 = QLabel(self.frame_25)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 16777215))
        self.label_18.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_45.addWidget(self.label_18)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lista_jogos_desenvolvedor = QComboBox(self.frame_25)
        self.lista_jogos_desenvolvedor.setObjectName(u"lista_jogos_desenvolvedor")

        self.horizontalLayout_43.addWidget(self.lista_jogos_desenvolvedor)


        self.horizontalLayout_42.addLayout(self.horizontalLayout_43)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(6)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.editar_jogo_button = QPushButton(self.frame_25)
        self.editar_jogo_button.setObjectName(u"editar_jogo_button")
        self.editar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_46.addWidget(self.editar_jogo_button)

        self.excluir_jogo_button = QPushButton(self.frame_25)
        self.excluir_jogo_button.setObjectName(u"excluir_jogo_button")
        self.excluir_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_46.addWidget(self.excluir_jogo_button)


        self.horizontalLayout_42.addLayout(self.verticalLayout_46)


        self.verticalLayout_45.addLayout(self.horizontalLayout_42)

        self.voltar_lista_jogos = QPushButton(self.frame_25)
        self.voltar_lista_jogos.setObjectName(u"voltar_lista_jogos")
        self.voltar_lista_jogos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_45.addWidget(self.voltar_lista_jogos)


        self.verticalLayout_44.addLayout(self.verticalLayout_45)


        self.horizontalLayout_41.addWidget(self.frame_25)


        self.verticalLayout_47.addWidget(self.frame_23)

        self.Pages.addWidget(self.pg_lista_jogo)
        self.pg_editar_jogo = QWidget()
        self.pg_editar_jogo.setObjectName(u"pg_editar_jogo")
        self.verticalLayout_52 = QVBoxLayout(self.pg_editar_jogo)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.pg_editar_jogo)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(600, 300))
        self.frame_27.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_27)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_19 = QLabel(self.frame_27)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_32.addWidget(self.label_19)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.novo_radio_jogo_alta = QRadioButton(self.frame_27)
        self.novo_radio_jogo_alta.setObjectName(u"novo_radio_jogo_alta")
        self.novo_radio_jogo_alta.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_alta.setStyleSheet(u"font-size: 14px;\n"
"	")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_alta)

        self.novo_radio_jogo_media = QRadioButton(self.frame_27)
        self.novo_radio_jogo_media.setObjectName(u"novo_radio_jogo_media")
        self.novo_radio_jogo_media.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_media.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_media)

        self.novo_radio_jogo_baixa = QRadioButton(self.frame_27)
        self.novo_radio_jogo_baixa.setObjectName(u"novo_radio_jogo_baixa")
        self.novo_radio_jogo_baixa.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_baixa.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_baixa)


        self.verticalLayout_32.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.novo_titulo_input = QLineEdit(self.frame_27)
        self.novo_titulo_input.setObjectName(u"novo_titulo_input")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.novo_titulo_input.sizePolicy().hasHeightForWidth())
        self.novo_titulo_input.setSizePolicy(sizePolicy)
        self.novo_titulo_input.setMaximumSize(QSize(400, 30))
        self.novo_titulo_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.novo_titulo_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.novo_titulo_input)

        self.novo_valor_jogo = QLineEdit(self.frame_27)
        self.novo_valor_jogo.setObjectName(u"novo_valor_jogo")
        self.novo_valor_jogo.setMaximumSize(QSize(50, 16777215))
        self.novo_valor_jogo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.novo_valor_jogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.novo_valor_jogo)


        self.verticalLayout_32.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.pushButton_7 = QPushButton(self.frame_27)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_46.addWidget(self.pushButton_7)

        self.salvar_edit_jogo_button = QPushButton(self.frame_27)
        self.salvar_edit_jogo_button.setObjectName(u"salvar_edit_jogo_button")
        self.salvar_edit_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #51484F; color:black}")

        self.horizontalLayout_46.addWidget(self.salvar_edit_jogo_button)

        self.pushButton_14 = QPushButton(self.frame_27)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setFlat(True)

        self.horizontalLayout_46.addWidget(self.pushButton_14)


        self.verticalLayout_32.addLayout(self.horizontalLayout_46)

        self.voltar_editar_jogo = QPushButton(self.frame_27)
        self.voltar_editar_jogo.setObjectName(u"voltar_editar_jogo")
        self.voltar_editar_jogo.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButtonshover{background-color: #fff; color:black}")

        self.verticalLayout_32.addWidget(self.voltar_editar_jogo)


        self.verticalLayout_48.addLayout(self.verticalLayout_32)


        self.horizontalLayout_48.addWidget(self.frame_27)


        self.verticalLayout_52.addWidget(self.frame_26)

        self.Pages.addWidget(self.pg_editar_jogo)
        self.pg_abastecer_creditos = QWidget()
        self.pg_abastecer_creditos.setObjectName(u"pg_abastecer_creditos")
        self.verticalLayout_31 = QVBoxLayout(self.pg_abastecer_creditos)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_28 = QFrame(self.pg_abastecer_creditos)
        self.frame_28.setObjectName(u"frame_28")
#if QT_CONFIG(accessibility)
        self.frame_28.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.frame_28.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setEnabled(True)
        self.frame_29.setMaximumSize(QSize(600, 300))
        self.frame_29.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(140, 10, 311, 41))
        self.label_21.setMaximumSize(QSize(16777215, 50))
        self.label_21.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.quantidade_creditos = QSpinBox(self.frame_29)
        self.quantidade_creditos.setObjectName(u"quantidade_creditos")
        self.quantidade_creditos.setGeometry(QRect(260, 110, 80, 35))
        sizePolicy.setHeightForWidth(self.quantidade_creditos.sizePolicy().hasHeightForWidth())
        self.quantidade_creditos.setSizePolicy(sizePolicy)
        self.quantidade_creditos.setMinimumSize(QSize(80, 35))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setWeight(50)
        self.quantidade_creditos.setFont(font2)
        self.quantidade_creditos.setLayoutDirection(Qt.LeftToRight)
        self.quantidade_creditos.setAlignment(Qt.AlignCenter)
        self.comprar_creditos_button = QPushButton(self.frame_29)
        self.comprar_creditos_button.setObjectName(u"comprar_creditos_button")
        self.comprar_creditos_button.setGeometry(QRect(260, 180, 75, 23))
        self.comprar_creditos_button.setMouseTracking(False)
        self.comprar_creditos_button.setTabletTracking(False)
        self.comprar_creditos_button.setAutoFillBackground(False)
        self.comprar_creditos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #51484F; color:black}")
        self.comprar_creditos_button.setCheckable(False)
        self.voltar_abastecer_creditos = QPushButton(self.frame_29)
        self.voltar_abastecer_creditos.setObjectName(u"voltar_abastecer_creditos")
        self.voltar_abastecer_creditos.setGeometry(QRect(260, 240, 75, 23))
        self.voltar_abastecer_creditos.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #51484F; color:black}")

        self.horizontalLayout_50.addWidget(self.frame_29)


        self.verticalLayout_31.addWidget(self.frame_28)

        self.Pages.addWidget(self.pg_abastecer_creditos)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_28 = QVBoxLayout(self.page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
#if QT_CONFIG(accessibility)
        self.frame_30.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.frame_30.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setEnabled(True)
        self.frame_31.setMaximumSize(QSize(600, 300))
        self.frame_31.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_31)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(140, 10, 311, 41))
        self.label_22.setMaximumSize(QSize(16777215, 50))
        self.label_22.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.voltar_abastecer_creditos_2 = QPushButton(self.frame_31)
        self.voltar_abastecer_creditos_2.setObjectName(u"voltar_abastecer_creditos_2")
        self.voltar_abastecer_creditos_2.setGeometry(QRect(260, 240, 75, 23))
        self.voltar_abastecer_creditos_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #51484F; color:black}")
        self.tableWidget_2 = QTableWidget(self.frame_31)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(190, 80, 191, 141))
        self.tableWidget_2.setRowCount(3)

        self.horizontalLayout_51.addWidget(self.frame_31)


        self.verticalLayout_28.addWidget(self.frame_30)

        self.Pages.addWidget(self.page)

        self.horizontalLayout_47.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.pushButton_4.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_7.setDefault(False)


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
        self.abastecer_creditos_button.setText(QCoreApplication.translate("MainWindow", u"Abastecer Creditos", None))
        self.alugar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Alugar Maquina", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Cadastrar Maquina</span></p></body></html>", None))
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
        self.adicionar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Adicionar Jogo", None))
        self.radio_baixo_edit.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.radio_media_edit.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.radio_alta_edit.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.salvar_edit_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(accessibility)
        self.porcentagem_edit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.porcentagem_edit.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.voltar_edit.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.busca_lista_maquina.setText(QCoreApplication.translate("MainWindow", u"Listar Maquinas", None))
        self.busca_lista_jogos.setText(QCoreApplication.translate("MainWindow", u"Listar Jogos", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Selecione o jogo", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Selecione uma maquina", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#fefefe;\">Busca</span></p></body></html>", None))
        self.voltar_busca.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Alugar Maquina</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Selecione o jogo:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Selecione a maquina:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Quantidade de horas", None))
        self.alugar_button.setText(QCoreApplication.translate("MainWindow", u"Alugar", None))
        self.voltar_alugar_maquina.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Cadastrar Jogo</span></p></body></html>", None))
        self.radio_jogo_alta.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.radio_jogo_media.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.radio_jogo_baixa.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.titulo_input.setText("")
        self.titulo_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo do Jogo", None))
        self.valor_jogo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.pushButton_5.setText("")
        self.cadastrar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_12.setText("")
        self.voltar_cadastrar_jogo.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Lista de Jogos</span></p></body></html>", None))
        self.editar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.excluir_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.voltar_lista_jogos.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Editar Jogo</span></p></body></html>", None))
        self.novo_radio_jogo_alta.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.novo_radio_jogo_media.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.novo_radio_jogo_baixa.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.novo_titulo_input.setText("")
        self.novo_titulo_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titulo do Jogo", None))
        self.novo_valor_jogo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.pushButton_7.setText("")
        self.salvar_edit_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pushButton_14.setText("")
        self.voltar_editar_jogo.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Abastecer Creditos</span></p></body></html>", None))
        self.comprar_creditos_button.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.voltar_abastecer_creditos.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Relatorios</span></p></body></html>", None))
        self.voltar_abastecer_creditos_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

