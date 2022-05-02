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
        MainWindow.resize(1093, 624)
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
        self.verticalLayout_40 = QVBoxLayout(self.frame_2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(3456789, 40))
        self.label.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_40.addWidget(self.label)

        self.frame_41 = QFrame(self.frame_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_41)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_input = QLineEdit(self.frame_41)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.username_input.setFrame(True)
        self.username_input.setCursorPosition(0)
        self.username_input.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.username_input)

        self.password_input = QLineEdit(self.frame_41)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password_input)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_40.addWidget(self.frame_41)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.login_button = QPushButton(self.frame_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(0, 25))
        self.login_button.setMaximumSize(QSize(16777215, 25))
        self.login_button.setBaseSize(QSize(0, 0))
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_6.addWidget(self.login_button)

        self.new_account_button_2 = QPushButton(self.frame_2)
        self.new_account_button_2.setObjectName(u"new_account_button_2")
        self.new_account_button_2.setMinimumSize(QSize(0, 25))
        self.new_account_button_2.setMaximumSize(QSize(16777215, 25))
        self.new_account_button_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_6.addWidget(self.new_account_button_2)


        self.verticalLayout_40.addLayout(self.horizontalLayout_6)


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
        self.verticalLayout_41 = QVBoxLayout(self.frame_4)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_41.addWidget(self.label_2)

        self.frame_42 = QFrame(self.frame_4)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_42)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_jogador = QRadioButton(self.frame_42)
        self.radio_jogador.setObjectName(u"radio_jogador")
        self.radio_jogador.setStyleSheet(u"font-size: 14px;\n"
"")
        self.radio_jogador.setChecked(False)
        self.radio_jogador.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.radio_jogador)

        self.radio_provedor = QRadioButton(self.frame_42)
        self.radio_provedor.setObjectName(u"radio_provedor")
        self.radio_provedor.setAutoFillBackground(False)
        self.radio_provedor.setStyleSheet(u"font-size: 14px;\n"
"")
        self.radio_provedor.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_provedor)

        self.radio_desenvolvedor = QRadioButton(self.frame_42)
        self.radio_desenvolvedor.setObjectName(u"radio_desenvolvedor")
        self.radio_desenvolvedor.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout.addWidget(self.radio_desenvolvedor)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.username_input_2 = QLineEdit(self.frame_42)
        self.username_input_2.setObjectName(u"username_input_2")
        self.username_input_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.username_input_2.setFrame(True)

        self.verticalLayout_9.addWidget(self.username_input_2)

        self.password_input_2 = QLineEdit(self.frame_42)
        self.password_input_2.setObjectName(u"password_input_2")
        self.password_input_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.password_input_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.password_input_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_41.addWidget(self.frame_42)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.voltar_cadastro_button = QPushButton(self.frame_4)
        self.voltar_cadastro_button.setObjectName(u"voltar_cadastro_button")
        self.voltar_cadastro_button.setMinimumSize(QSize(0, 25))
        self.voltar_cadastro_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_cadastro_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_7.addWidget(self.voltar_cadastro_button)

        self.create_account_button = QPushButton(self.frame_4)
        self.create_account_button.setObjectName(u"create_account_button")
        self.create_account_button.setMinimumSize(QSize(0, 25))
        self.create_account_button.setMaximumSize(QSize(16777215, 25))
        self.create_account_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_7.addWidget(self.create_account_button)


        self.verticalLayout_41.addLayout(self.horizontalLayout_7)


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
        self.verticalLayout_42 = QVBoxLayout(self.frame_6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setMaximumSize(QSize(16777213, 40))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_42.addWidget(self.label_3)

        self.frame_43 = QFrame(self.frame_6)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_43)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mostrador_nome_jogador = QLabel(self.frame_43)
        self.mostrador_nome_jogador.setObjectName(u"mostrador_nome_jogador")
        self.mostrador_nome_jogador.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(14)
        self.mostrador_nome_jogador.setFont(font)
        self.mostrador_nome_jogador.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.mostrador_nome_jogador)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.buscar_button = QPushButton(self.frame_43)
        self.buscar_button.setObjectName(u"buscar_button")
        self.buscar_button.setMinimumSize(QSize(0, 25))
        self.buscar_button.setMaximumSize(QSize(16777215, 25))
        self.buscar_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_15.addWidget(self.buscar_button)

        self.alugar_maquina_button = QPushButton(self.frame_43)
        self.alugar_maquina_button.setObjectName(u"alugar_maquina_button")
        self.alugar_maquina_button.setMinimumSize(QSize(0, 25))
        self.alugar_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.alugar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_15.addWidget(self.alugar_maquina_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.relatorio_jogador_button = QPushButton(self.frame_43)
        self.relatorio_jogador_button.setObjectName(u"relatorio_jogador_button")
        self.relatorio_jogador_button.setMinimumSize(QSize(0, 25))
        self.relatorio_jogador_button.setMaximumSize(QSize(16777215, 25))
        self.relatorio_jogador_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_27.addWidget(self.relatorio_jogador_button)

        self.abastecer_creditos_button = QPushButton(self.frame_43)
        self.abastecer_creditos_button.setObjectName(u"abastecer_creditos_button")
        self.abastecer_creditos_button.setMinimumSize(QSize(0, 25))
        self.abastecer_creditos_button.setMaximumSize(QSize(16777215, 25))
        self.abastecer_creditos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_27.addWidget(self.abastecer_creditos_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_27)


        self.verticalLayout_42.addWidget(self.frame_43)

        self.sairjogador_button = QPushButton(self.frame_6)
        self.sairjogador_button.setObjectName(u"sairjogador_button")
        self.sairjogador_button.setMinimumSize(QSize(0, 25))
        self.sairjogador_button.setMaximumSize(QSize(16777215, 25))
        self.sairjogador_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_42.addWidget(self.sairjogador_button)


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
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777213, 40))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_8.addWidget(self.label_4)

        self.frame_44 = QFrame(self.frame_8)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_44)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.mostrador_nome_provedor = QLabel(self.frame_44)
        self.mostrador_nome_provedor.setObjectName(u"mostrador_nome_provedor")
        self.mostrador_nome_provedor.setMaximumSize(QSize(16777215, 30))
        self.mostrador_nome_provedor.setFont(font)
        self.mostrador_nome_provedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.mostrador_nome_provedor)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cadastrar_maquina_button = QPushButton(self.frame_44)
        self.cadastrar_maquina_button.setObjectName(u"cadastrar_maquina_button")
        self.cadastrar_maquina_button.setMinimumSize(QSize(0, 25))
        self.cadastrar_maquina_button.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        self.cadastrar_maquina_button.setFont(font1)
        self.cadastrar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_9.addWidget(self.cadastrar_maquina_button)

        self.listar_maquinas_button = QPushButton(self.frame_44)
        self.listar_maquinas_button.setObjectName(u"listar_maquinas_button")
        self.listar_maquinas_button.setMinimumSize(QSize(0, 25))
        self.listar_maquinas_button.setMaximumSize(QSize(16777215, 25))
        self.listar_maquinas_button.setFont(font1)
        self.listar_maquinas_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_9.addWidget(self.listar_maquinas_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.relatorio_provedor_button = QPushButton(self.frame_44)
        self.relatorio_provedor_button.setObjectName(u"relatorio_provedor_button")
        self.relatorio_provedor_button.setMinimumSize(QSize(0, 25))
        self.relatorio_provedor_button.setMaximumSize(QSize(16777215, 25))
        self.relatorio_provedor_button.setFont(font1)
        self.relatorio_provedor_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_10.addWidget(self.relatorio_provedor_button)

        self.sacar_button = QPushButton(self.frame_44)
        self.sacar_button.setObjectName(u"sacar_button")
        self.sacar_button.setMinimumSize(QSize(0, 25))
        self.sacar_button.setMaximumSize(QSize(16777215, 25))
        self.sacar_button.setFont(font1)
        self.sacar_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_10.addWidget(self.sacar_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout_8.addWidget(self.frame_44)

        self.sairprovedor_button = QPushButton(self.frame_8)
        self.sairprovedor_button.setObjectName(u"sairprovedor_button")
        self.sairprovedor_button.setMinimumSize(QSize(0, 25))
        self.sairprovedor_button.setMaximumSize(QSize(16777215, 25))
        self.sairprovedor_button.setFont(font1)
        self.sairprovedor_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_8.addWidget(self.sairprovedor_button)


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
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777213, 40))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_10.addWidget(self.label_5)

        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 200))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_24)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.mostrardor_nome_desenvolvedor = QLabel(self.frame_24)
        self.mostrardor_nome_desenvolvedor.setObjectName(u"mostrardor_nome_desenvolvedor")
        self.mostrardor_nome_desenvolvedor.setMaximumSize(QSize(16777215, 30))
        self.mostrardor_nome_desenvolvedor.setFont(font)
        self.mostrardor_nome_desenvolvedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.mostrardor_nome_desenvolvedor)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.relatorio_desenvolvedor_button = QPushButton(self.frame_24)
        self.relatorio_desenvolvedor_button.setObjectName(u"relatorio_desenvolvedor_button")
        self.relatorio_desenvolvedor_button.setMinimumSize(QSize(0, 25))
        self.relatorio_desenvolvedor_button.setMaximumSize(QSize(16777215, 25))
        self.relatorio_desenvolvedor_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_12.addWidget(self.relatorio_desenvolvedor_button)

        self.listar_jogos_button = QPushButton(self.frame_24)
        self.listar_jogos_button.setObjectName(u"listar_jogos_button")
        self.listar_jogos_button.setMinimumSize(QSize(0, 25))
        self.listar_jogos_button.setMaximumSize(QSize(16777215, 25))
        self.listar_jogos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_12.addWidget(self.listar_jogos_button)

        self.cadastrar_jogo_button_2 = QPushButton(self.frame_24)
        self.cadastrar_jogo_button_2.setObjectName(u"cadastrar_jogo_button_2")
        self.cadastrar_jogo_button_2.setMinimumSize(QSize(0, 25))
        self.cadastrar_jogo_button_2.setMaximumSize(QSize(16777215, 25))
        self.cadastrar_jogo_button_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_12.addWidget(self.cadastrar_jogo_button_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout_10.addWidget(self.frame_24)

        self.sairdesenvolvedor_button = QPushButton(self.frame_10)
        self.sairdesenvolvedor_button.setObjectName(u"sairdesenvolvedor_button")
        self.sairdesenvolvedor_button.setMinimumSize(QSize(0, 25))
        self.sairdesenvolvedor_button.setMaximumSize(QSize(16777215, 25))
        self.sairdesenvolvedor_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_10.addWidget(self.sairdesenvolvedor_button)


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
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_13.addWidget(self.label_6)

        self.frame_32 = QFrame(self.frame_12)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 200))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_32)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.radio_alta = QRadioButton(self.frame_32)
        self.radio_alta.setObjectName(u"radio_alta")
        self.radio_alta.setMaximumSize(QSize(100, 16777215))
        self.radio_alta.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_18.addWidget(self.radio_alta)

        self.radio_media = QRadioButton(self.frame_32)
        self.radio_media.setObjectName(u"radio_media")
        self.radio_media.setMaximumSize(QSize(100, 16777215))
        self.radio_media.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_18.addWidget(self.radio_media)

        self.radio_baixa = QRadioButton(self.frame_32)
        self.radio_baixa.setObjectName(u"radio_baixa")
        self.radio_baixa.setMaximumSize(QSize(100, 16777215))
        self.radio_baixa.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_18.addWidget(self.radio_baixa)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.nome_maquina_input = QLineEdit(self.frame_32)
        self.nome_maquina_input.setObjectName(u"nome_maquina_input")
        self.nome_maquina_input.setMaximumSize(QSize(400, 100))
        self.nome_maquina_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.nome_maquina_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.nome_maquina_input)

        self.porcentagem_input = QSpinBox(self.frame_32)
        self.porcentagem_input.setObjectName(u"porcentagem_input")
        self.porcentagem_input.setMinimumSize(QSize(65, 0))
        self.porcentagem_input.setMaximumSize(QSize(50, 16777215))
        self.porcentagem_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.porcentagem_input.setMaximum(100)
        self.porcentagem_input.setSingleStep(5)
        self.porcentagem_input.setValue(75)

        self.horizontalLayout_19.addWidget(self.porcentagem_input)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_4 = QPushButton(self.frame_32)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_20.addWidget(self.pushButton_4)

        self.cadastrar_button = QPushButton(self.frame_32)
        self.cadastrar_button.setObjectName(u"cadastrar_button")
        self.cadastrar_button.setMinimumSize(QSize(0, 25))
        self.cadastrar_button.setMaximumSize(QSize(16777215, 25))
        self.cadastrar_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_20.addWidget(self.cadastrar_button)

        self.pushButton_11 = QPushButton(self.frame_32)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setFlat(True)

        self.horizontalLayout_20.addWidget(self.pushButton_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)


        self.verticalLayout_13.addWidget(self.frame_32)

        self.voltar_cadastrar_maquina_button = QPushButton(self.frame_12)
        self.voltar_cadastrar_maquina_button.setObjectName(u"voltar_cadastrar_maquina_button")
        self.voltar_cadastrar_maquina_button.setMinimumSize(QSize(0, 25))
        self.voltar_cadastrar_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_cadastrar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_13.addWidget(self.voltar_cadastrar_maquina_button)


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
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_16.addWidget(self.label_7)

        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 200))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_33)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lista_maquinas_provedor = QComboBox(self.frame_33)
        self.lista_maquinas_provedor.setObjectName(u"lista_maquinas_provedor")
        self.lista_maquinas_provedor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")

        self.horizontalLayout_22.addWidget(self.lista_maquinas_provedor)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_22)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.editar_maquina_button = QPushButton(self.frame_33)
        self.editar_maquina_button.setObjectName(u"editar_maquina_button")
        self.editar_maquina_button.setMinimumSize(QSize(0, 25))
        self.editar_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.editar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_5.addWidget(self.editar_maquina_button)

        self.excluir_maquina_button = QPushButton(self.frame_33)
        self.excluir_maquina_button.setObjectName(u"excluir_maquina_button")
        self.excluir_maquina_button.setMinimumSize(QSize(0, 25))
        self.excluir_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.excluir_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_5.addWidget(self.excluir_maquina_button)


        self.horizontalLayout_23.addLayout(self.verticalLayout_5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_23)


        self.verticalLayout_16.addWidget(self.frame_33)

        self.voltar_lista_maquinas_button = QPushButton(self.frame_14)
        self.voltar_lista_maquinas_button.setObjectName(u"voltar_lista_maquinas_button")
        self.voltar_lista_maquinas_button.setMinimumSize(QSize(0, 25))
        self.voltar_lista_maquinas_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_lista_maquinas_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_16.addWidget(self.voltar_lista_maquinas_button)


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
        self.verticalLayout_15 = QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.frame_34 = QFrame(self.frame_16)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_34)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.nome_maquina_editada = QLabel(self.frame_34)
        self.nome_maquina_editada.setObjectName(u"nome_maquina_editada")
        self.nome_maquina_editada.setMinimumSize(QSize(0, 35))
        self.nome_maquina_editada.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.nome_maquina_editada.setFont(font2)
        self.nome_maquina_editada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.nome_maquina_editada)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(12)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(15, -1, 15, -1)
        self.lista_jogos_adicionar = QComboBox(self.frame_34)
        self.lista_jogos_adicionar.setObjectName(u"lista_jogos_adicionar")
        self.lista_jogos_adicionar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")

        self.verticalLayout_24.addWidget(self.lista_jogos_adicionar)

        self.adicionar_jogo_button = QPushButton(self.frame_34)
        self.adicionar_jogo_button.setObjectName(u"adicionar_jogo_button")
        self.adicionar_jogo_button.setMinimumSize(QSize(0, 25))
        self.adicionar_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.adicionar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_24.addWidget(self.adicionar_jogo_button)


        self.horizontalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(45)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, -1, -1, -1)
        self.radio_baixo_edit = QRadioButton(self.frame_34)
        self.radio_baixo_edit.setObjectName(u"radio_baixo_edit")
        self.radio_baixo_edit.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_24.addWidget(self.radio_baixo_edit)

        self.radio_media_edit = QRadioButton(self.frame_34)
        self.radio_media_edit.setObjectName(u"radio_media_edit")
        self.radio_media_edit.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_24.addWidget(self.radio_media_edit)

        self.radio_alta_edit = QRadioButton(self.frame_34)
        self.radio_alta_edit.setObjectName(u"radio_alta_edit")
        self.radio_alta_edit.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_24.addWidget(self.radio_alta_edit)


        self.verticalLayout_14.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.porcentagem_edit = QSpinBox(self.frame_34)
        self.porcentagem_edit.setObjectName(u"porcentagem_edit")
        self.porcentagem_edit.setMinimumSize(QSize(55, 0))
        self.porcentagem_edit.setMaximumSize(QSize(50, 30))
        self.porcentagem_edit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.porcentagem_edit.setFrame(True)
        self.porcentagem_edit.setButtonSymbols(QAbstractSpinBox.PlusMinus)

        self.horizontalLayout_26.addWidget(self.porcentagem_edit)

        self.salvar_edit_maquina_button = QPushButton(self.frame_34)
        self.salvar_edit_maquina_button.setObjectName(u"salvar_edit_maquina_button")
        self.salvar_edit_maquina_button.setMinimumSize(QSize(0, 25))
        self.salvar_edit_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.salvar_edit_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_26.addWidget(self.salvar_edit_maquina_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_25.addLayout(self.verticalLayout_14)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)


        self.verticalLayout_15.addWidget(self.frame_34)

        self.voltar_edit_button = QPushButton(self.frame_16)
        self.voltar_edit_button.setObjectName(u"voltar_edit_button")
        self.voltar_edit_button.setMinimumSize(QSize(0, 25))
        self.voltar_edit_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_edit_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_15.addWidget(self.voltar_edit_button)


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
        self.verticalLayout_45 = QVBoxLayout(self.frame_18)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))
        self.label_10.setMaximumSize(QSize(16777215, 40))
        self.label_10.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_45.addWidget(self.label_10)

        self.frame_47 = QFrame(self.frame_18)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_45 = QFrame(self.frame_47)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_45)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_11 = QLabel(self.frame_45)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(168, 0))
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_11)

        self.lista_de_jogos = QComboBox(self.frame_45)
        self.lista_de_jogos.setObjectName(u"lista_de_jogos")

        self.verticalLayout_43.addWidget(self.lista_de_jogos)

        self.busca_lista_maquina_button = QPushButton(self.frame_45)
        self.busca_lista_maquina_button.setObjectName(u"busca_lista_maquina_button")
        self.busca_lista_maquina_button.setMinimumSize(QSize(0, 25))
        self.busca_lista_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.busca_lista_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_43.addWidget(self.busca_lista_maquina_button)


        self.horizontalLayout_28.addWidget(self.frame_45)

        self.tableWidget = QTableWidget(self.frame_47)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_28.addWidget(self.tableWidget)

        self.frame_46 = QFrame(self.frame_47)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_46)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_12 = QLabel(self.frame_46)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(168, 0))
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_12)

        self.lista_de_maquinas = QComboBox(self.frame_46)
        self.lista_de_maquinas.setObjectName(u"lista_de_maquinas")

        self.verticalLayout_44.addWidget(self.lista_de_maquinas)

        self.busca_lista_jogos_button = QPushButton(self.frame_46)
        self.busca_lista_jogos_button.setObjectName(u"busca_lista_jogos_button")
        self.busca_lista_jogos_button.setMinimumSize(QSize(0, 25))
        self.busca_lista_jogos_button.setMaximumSize(QSize(16777215, 25))
        self.busca_lista_jogos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_44.addWidget(self.busca_lista_jogos_button)


        self.horizontalLayout_28.addWidget(self.frame_46)


        self.verticalLayout_45.addWidget(self.frame_47)

        self.voltar_busca_button = QPushButton(self.frame_18)
        self.voltar_busca_button.setObjectName(u"voltar_busca_button")
        self.voltar_busca_button.setMinimumSize(QSize(0, 25))
        self.voltar_busca_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_busca_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_45.addWidget(self.voltar_busca_button)


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
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 40))
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_21.addWidget(self.label_13)

        self.frame_35 = QFrame(self.frame_20)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_35)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_14 = QLabel(self.frame_35)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 16777215))
        self.label_14.setStyleSheet(u"font-size: 14px;\n"
"")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_14)

        self.lista_jogos_alugar = QComboBox(self.frame_35)
        self.lista_jogos_alugar.setObjectName(u"lista_jogos_alugar")
        self.lista_jogos_alugar.setMaximumSize(QSize(300, 16777215))
        self.lista_jogos_alugar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")

        self.horizontalLayout_31.addWidget(self.lista_jogos_alugar)


        self.verticalLayout_20.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_15 = QLabel(self.frame_35)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(150, 16777215))
        self.label_15.setStyleSheet(u"font-size: 14px;\n"
"")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_15)

        self.lista_maquinas_aluguel = QComboBox(self.frame_35)
        self.lista_maquinas_aluguel.setObjectName(u"lista_maquinas_aluguel")
        self.lista_maquinas_aluguel.setMaximumSize(QSize(300, 16777215))
        self.lista_maquinas_aluguel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")

        self.horizontalLayout_32.addWidget(self.lista_maquinas_aluguel)


        self.verticalLayout_20.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_20 = QLabel(self.frame_35)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(150, 16777215))
        self.label_20.setStyleSheet(u"font-size: 14px;\n"
"")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_20)

        self.horas = QSpinBox(self.frame_35)
        self.horas.setObjectName(u"horas")
        self.horas.setMaximumSize(QSize(300, 16777215))
        self.horas.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.horas.setLayoutDirection(Qt.LeftToRight)
        self.horas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.horas.setWrapping(False)
        self.horas.setFrame(True)
        self.horas.setAlignment(Qt.AlignCenter)
        self.horas.setMinimum(1)
        self.horas.setMaximum(5)

        self.horizontalLayout_38.addWidget(self.horas)


        self.verticalLayout_20.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.pushButton = QPushButton(self.frame_35)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setFlat(True)

        self.horizontalLayout_37.addWidget(self.pushButton)

        self.alugar_button = QPushButton(self.frame_35)
        self.alugar_button.setObjectName(u"alugar_button")
        self.alugar_button.setMinimumSize(QSize(0, 25))
        self.alugar_button.setMaximumSize(QSize(16777215, 25))
        self.alugar_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_37.addWidget(self.alugar_button)

        self.pushButton_2 = QPushButton(self.frame_35)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_37.addWidget(self.pushButton_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)


        self.verticalLayout_21.addWidget(self.frame_35)

        self.voltar_alugar_maquina_button = QPushButton(self.frame_20)
        self.voltar_alugar_maquina_button.setObjectName(u"voltar_alugar_maquina_button")
        self.voltar_alugar_maquina_button.setMinimumSize(QSize(0, 25))
        self.voltar_alugar_maquina_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_alugar_maquina_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_21.addWidget(self.voltar_alugar_maquina_button)


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
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_16 = QLabel(self.frame_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 40))
        self.label_16.setMaximumSize(QSize(16777215, 40))
        self.label_16.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_23.addWidget(self.label_16)

        self.frame_36 = QFrame(self.frame_22)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, -1, -1, -1)
        self.radio_jogo_alta = QRadioButton(self.frame_36)
        self.radio_jogo_alta.setObjectName(u"radio_jogo_alta")
        self.radio_jogo_alta.setMaximumSize(QSize(100, 16777215))
        self.radio_jogo_alta.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_34.addWidget(self.radio_jogo_alta)

        self.radio_jogo_media = QRadioButton(self.frame_36)
        self.radio_jogo_media.setObjectName(u"radio_jogo_media")
        self.radio_jogo_media.setMaximumSize(QSize(100, 16777215))
        self.radio_jogo_media.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_34.addWidget(self.radio_jogo_media)

        self.radio_jogo_baixa = QRadioButton(self.frame_36)
        self.radio_jogo_baixa.setObjectName(u"radio_jogo_baixa")
        self.radio_jogo_baixa.setMaximumSize(QSize(100, 16777215))
        self.radio_jogo_baixa.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_34.addWidget(self.radio_jogo_baixa)


        self.verticalLayout_25.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.titulo_input = QLineEdit(self.frame_36)
        self.titulo_input.setObjectName(u"titulo_input")
        self.titulo_input.setMaximumSize(QSize(300, 12345678))
        self.titulo_input.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.titulo_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.titulo_input)

        self.valor_jogo = QLineEdit(self.frame_36)
        self.valor_jogo.setObjectName(u"valor_jogo")
        self.valor_jogo.setMaximumSize(QSize(75, 16777215))
        self.valor_jogo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.valor_jogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.valor_jogo)


        self.verticalLayout_25.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.pushButton_5 = QPushButton(self.frame_36)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_36.addWidget(self.pushButton_5)

        self.cadastrar_jogo_button = QPushButton(self.frame_36)
        self.cadastrar_jogo_button.setObjectName(u"cadastrar_jogo_button")
        self.cadastrar_jogo_button.setMinimumSize(QSize(0, 25))
        self.cadastrar_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.cadastrar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_36.addWidget(self.cadastrar_jogo_button)

        self.pushButton_12 = QPushButton(self.frame_36)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setFlat(True)

        self.horizontalLayout_36.addWidget(self.pushButton_12)


        self.verticalLayout_25.addLayout(self.horizontalLayout_36)


        self.verticalLayout_23.addWidget(self.frame_36)

        self.voltar_cadastrar_jogo_button = QPushButton(self.frame_22)
        self.voltar_cadastrar_jogo_button.setObjectName(u"voltar_cadastrar_jogo_button")
        self.voltar_cadastrar_jogo_button.setMinimumSize(QSize(0, 25))
        self.voltar_cadastrar_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_cadastrar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_23.addWidget(self.voltar_cadastrar_jogo_button)


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
        self.verticalLayout_29 = QVBoxLayout(self.frame_25)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.frame_25)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))
        self.label_18.setMaximumSize(QSize(16777215, 40))
        self.label_18.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_29.addWidget(self.label_18)

        self.frame_37 = QFrame(self.frame_25)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lista_jogos_desenvolvedor = QComboBox(self.frame_37)
        self.lista_jogos_desenvolvedor.setObjectName(u"lista_jogos_desenvolvedor")
        self.lista_jogos_desenvolvedor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")

        self.horizontalLayout_43.addWidget(self.lista_jogos_desenvolvedor)


        self.horizontalLayout_42.addLayout(self.horizontalLayout_43)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(6)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.editar_jogo_button = QPushButton(self.frame_37)
        self.editar_jogo_button.setObjectName(u"editar_jogo_button")
        self.editar_jogo_button.setMinimumSize(QSize(0, 25))
        self.editar_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.editar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_46.addWidget(self.editar_jogo_button)

        self.excluir_jogo_button = QPushButton(self.frame_37)
        self.excluir_jogo_button.setObjectName(u"excluir_jogo_button")
        self.excluir_jogo_button.setMinimumSize(QSize(0, 25))
        self.excluir_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.excluir_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_46.addWidget(self.excluir_jogo_button)


        self.horizontalLayout_42.addLayout(self.verticalLayout_46)


        self.verticalLayout_27.addLayout(self.horizontalLayout_42)


        self.verticalLayout_29.addWidget(self.frame_37)

        self.voltar_lista_jogos_button = QPushButton(self.frame_25)
        self.voltar_lista_jogos_button.setObjectName(u"voltar_lista_jogos_button")
        self.voltar_lista_jogos_button.setMinimumSize(QSize(0, 25))
        self.voltar_lista_jogos_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_lista_jogos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_29.addWidget(self.voltar_lista_jogos_button)


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
        self.verticalLayout_32 = QVBoxLayout(self.frame_27)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_19 = QLabel(self.frame_27)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 40))
        self.label_19.setMaximumSize(QSize(16777215, 40))
        self.label_19.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_32.addWidget(self.label_19)

        self.frame_38 = QFrame(self.frame_27)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_38)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_9 = QLabel(self.frame_38)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_9)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.novo_radio_jogo_alta = QRadioButton(self.frame_38)
        self.novo_radio_jogo_alta.setObjectName(u"novo_radio_jogo_alta")
        self.novo_radio_jogo_alta.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_alta.setStyleSheet(u"font-size: 14px;\n"
"	")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_alta)

        self.novo_radio_jogo_media = QRadioButton(self.frame_38)
        self.novo_radio_jogo_media.setObjectName(u"novo_radio_jogo_media")
        self.novo_radio_jogo_media.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_media.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_media)

        self.novo_radio_jogo_baixa = QRadioButton(self.frame_38)
        self.novo_radio_jogo_baixa.setObjectName(u"novo_radio_jogo_baixa")
        self.novo_radio_jogo_baixa.setMaximumSize(QSize(100, 16777215))
        self.novo_radio_jogo_baixa.setStyleSheet(u"font-size: 14px;\n"
"")

        self.horizontalLayout_44.addWidget(self.novo_radio_jogo_baixa)


        self.verticalLayout_30.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_23 = QLabel(self.frame_38)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_39.addWidget(self.label_23)

        self.novo_valor_jogo = QLineEdit(self.frame_38)
        self.novo_valor_jogo.setObjectName(u"novo_valor_jogo")
        self.novo_valor_jogo.setMaximumSize(QSize(50, 16777215))
        self.novo_valor_jogo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.novo_valor_jogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.novo_valor_jogo)

        self.label_17 = QLabel(self.frame_38)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_39.addWidget(self.label_17)


        self.verticalLayout_30.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.pushButton_7 = QPushButton(self.frame_38)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_46.addWidget(self.pushButton_7)

        self.salvar_edit_jogo_button = QPushButton(self.frame_38)
        self.salvar_edit_jogo_button.setObjectName(u"salvar_edit_jogo_button")
        self.salvar_edit_jogo_button.setMinimumSize(QSize(0, 25))
        self.salvar_edit_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.salvar_edit_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.horizontalLayout_46.addWidget(self.salvar_edit_jogo_button)

        self.pushButton_14 = QPushButton(self.frame_38)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setFlat(True)

        self.horizontalLayout_46.addWidget(self.pushButton_14)


        self.verticalLayout_30.addLayout(self.horizontalLayout_46)


        self.verticalLayout_32.addWidget(self.frame_38)

        self.voltar_editar_jogo_button = QPushButton(self.frame_27)
        self.voltar_editar_jogo_button.setObjectName(u"voltar_editar_jogo_button")
        self.voltar_editar_jogo_button.setMinimumSize(QSize(0, 25))
        self.voltar_editar_jogo_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_editar_jogo_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_32.addWidget(self.voltar_editar_jogo_button)


        self.horizontalLayout_48.addWidget(self.frame_27)


        self.verticalLayout_52.addWidget(self.frame_26)

        self.Pages.addWidget(self.pg_editar_jogo)
        self.pg_abastecer_creditos = QWidget()
        self.pg_abastecer_creditos.setObjectName(u"pg_abastecer_creditos")
        self.verticalLayout_31 = QVBoxLayout(self.pg_abastecer_creditos)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_33 = QVBoxLayout(self.frame_29)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_21 = QLabel(self.frame_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 40))
        self.label_21.setMaximumSize(QSize(16777215, 40))
        self.label_21.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_33.addWidget(self.label_21)

        self.frame_39 = QFrame(self.frame_29)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_39)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(25)
        self.comprar_creditos_button = QPushButton(self.frame_39)
        self.comprar_creditos_button.setObjectName(u"comprar_creditos_button")
        self.comprar_creditos_button.setMinimumSize(QSize(150, 25))
        self.comprar_creditos_button.setMaximumSize(QSize(16777215, 25))
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
"QPushButton:hover{background-color: #787878; color:black}")
        self.comprar_creditos_button.setCheckable(False)

        self.gridLayout.addWidget(self.comprar_creditos_button, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_39)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_39)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.quantidade_creditos = QSpinBox(self.frame_39)
        self.quantidade_creditos.setObjectName(u"quantidade_creditos")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantidade_creditos.sizePolicy().hasHeightForWidth())
        self.quantidade_creditos.setSizePolicy(sizePolicy)
        self.quantidade_creditos.setMinimumSize(QSize(150, 35))
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(False)
        font3.setWeight(50)
        self.quantidade_creditos.setFont(font3)
        self.quantidade_creditos.setLayoutDirection(Qt.LeftToRight)
        self.quantidade_creditos.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.quantidade_creditos, 0, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout)


        self.verticalLayout_33.addWidget(self.frame_39)

        self.voltar_abastecer_creditos_button = QPushButton(self.frame_29)
        self.voltar_abastecer_creditos_button.setObjectName(u"voltar_abastecer_creditos_button")
        self.voltar_abastecer_creditos_button.setMinimumSize(QSize(0, 25))
        self.voltar_abastecer_creditos_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_abastecer_creditos_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_33.addWidget(self.voltar_abastecer_creditos_button)


        self.horizontalLayout_50.addWidget(self.frame_29)


        self.verticalLayout_31.addWidget(self.frame_28)

        self.Pages.addWidget(self.pg_abastecer_creditos)
        self.pg_relatorio = QWidget()
        self.pg_relatorio.setObjectName(u"pg_relatorio")
        self.verticalLayout_28 = QVBoxLayout(self.pg_relatorio)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.pg_relatorio)
        self.frame_30.setObjectName(u"frame_30")
#if QT_CONFIG(accessibility)
        self.frame_30.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.frame_30.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setEnabled(True)
        self.frame_31.setMaximumSize(QSize(600, 300))
        self.frame_31.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_31)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_22 = QLabel(self.frame_31)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 40))
        self.label_22.setMaximumSize(QSize(16777215, 40))
        self.label_22.setStyleSheet(u"background-color: rgb(53, 53, 53);")

        self.verticalLayout_37.addWidget(self.label_22)

        self.frame_40 = QFrame(self.frame_31)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_40)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tableWidget_2 = QTableWidget(self.frame_40)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(3)

        self.verticalLayout_38.addWidget(self.tableWidget_2)


        self.verticalLayout_37.addWidget(self.frame_40)

        self.voltar_relatorio_button = QPushButton(self.frame_31)
        self.voltar_relatorio_button.setObjectName(u"voltar_relatorio_button")
        self.voltar_relatorio_button.setMinimumSize(QSize(0, 25))
        self.voltar_relatorio_button.setMaximumSize(QSize(16777215, 25))
        self.voltar_relatorio_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	\n"
"	background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushButton:hover{background-color: #787878; color:black}")

        self.verticalLayout_37.addWidget(self.voltar_relatorio_button)


        self.horizontalLayout_51.addWidget(self.frame_31)


        self.verticalLayout_28.addWidget(self.frame_30)

        self.Pages.addWidget(self.pg_relatorio)

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
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome de Usuario", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.new_account_button_2.setText(QCoreApplication.translate("MainWindow", u"Nova Conta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">CADASTRO</span></p></body></html>", None))
        self.radio_jogador.setText(QCoreApplication.translate("MainWindow", u"Jogador", None))
        self.radio_provedor.setText(QCoreApplication.translate("MainWindow", u"Provedor", None))
        self.radio_desenvolvedor.setText(QCoreApplication.translate("MainWindow", u"Desenvolvedor", None))
        self.username_input_2.setInputMask("")
        self.username_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome de Usuario", None))
        self.password_input_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.voltar_cadastro_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.create_account_button.setText(QCoreApplication.translate("MainWindow", u"Criar Conta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Jogador</span></p></body></html>", None))
        self.mostrador_nome_jogador.setText(QCoreApplication.translate("MainWindow", u"mostrador_nome_jogador", None))
        self.buscar_button.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.alugar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Alugar Maquina", None))
        self.relatorio_jogador_button.setText(QCoreApplication.translate("MainWindow", u"Relatorio", None))
        self.abastecer_creditos_button.setText(QCoreApplication.translate("MainWindow", u"Abastecer Creditos", None))
        self.sairjogador_button.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#f0f0f0;\">Provedor</span></p></body></html>", None))
        self.mostrador_nome_provedor.setText(QCoreApplication.translate("MainWindow", u"mostrador_nome_provedor", None))
        self.cadastrar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Maquina", None))
        self.listar_maquinas_button.setText(QCoreApplication.translate("MainWindow", u"Lista de Maquinas", None))
        self.relatorio_provedor_button.setText(QCoreApplication.translate("MainWindow", u"Relatorios", None))
        self.sacar_button.setText(QCoreApplication.translate("MainWindow", u"Sacar", None))
        self.sairprovedor_button.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Desenvolvedor</span></p></body></html>", None))
        self.mostrardor_nome_desenvolvedor.setText(QCoreApplication.translate("MainWindow", u"mostrador_nome_desenvolvedor", None))
        self.relatorio_desenvolvedor_button.setText(QCoreApplication.translate("MainWindow", u"Relatorios", None))
        self.listar_jogos_button.setText(QCoreApplication.translate("MainWindow", u"Listar Jogos", None))
        self.cadastrar_jogo_button_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Jogo", None))
        self.sairdesenvolvedor_button.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
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
        self.voltar_cadastrar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Lista de Maquinas</span></p></body></html>", None))
        self.editar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.excluir_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.voltar_lista_maquinas_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Editar Maquina</span></p></body></html>", None))
        self.nome_maquina_editada.setText(QCoreApplication.translate("MainWindow", u"Mostrar nome Maquina ", None))
        self.adicionar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Adicionar Jogo", None))
        self.radio_baixo_edit.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.radio_media_edit.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.radio_alta_edit.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
#if QT_CONFIG(accessibility)
        self.porcentagem_edit.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.porcentagem_edit.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.salvar_edit_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.voltar_edit_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#fefefe;\">Busca</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Selecione o jogo", None))
        self.busca_lista_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Listar Maquinas", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Selecione uma maquina", None))
        self.busca_lista_jogos_button.setText(QCoreApplication.translate("MainWindow", u"Listar Jogos", None))
        self.voltar_busca_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Alugar Maquina</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Selecione o jogo:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Selecione a maquina:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Quantidade de horas:", None))
        self.pushButton.setText("")
        self.alugar_button.setText(QCoreApplication.translate("MainWindow", u"Alugar", None))
        self.pushButton_2.setText("")
        self.voltar_alugar_maquina_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
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
        self.voltar_cadastrar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Lista de Jogos</span></p></body></html>", None))
        self.editar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.excluir_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.voltar_lista_jogos_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Editar Jogo</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mostrar nome jogo", None))
        self.novo_radio_jogo_alta.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.novo_radio_jogo_media.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.novo_radio_jogo_baixa.setText(QCoreApplication.translate("MainWindow", u"Baixa", None))
        self.label_23.setText("")
        self.novo_valor_jogo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_17.setText("")
        self.pushButton_7.setText("")
        self.salvar_edit_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_14.setText("")
        self.voltar_editar_jogo_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Abastecer Creditos</span></p></body></html>", None))
        self.comprar_creditos_button.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.pushButton_6.setText("")
        self.pushButton_3.setText("")
        self.voltar_abastecer_creditos_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Relatorio</span></p></body></html>", None))
        self.voltar_relatorio_button.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi

