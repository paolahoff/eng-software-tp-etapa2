import pandas as pd


class Maquina:

    def __init__(self):
        self.__especificacoes = None
        self.__porcentagem_uso = None
        self.__preco_aluguel = None
        self.em_uso = False
        self.horas_em_uso = 0
        self.ganhos = 0

    def gerar_aluguel(self):
        return int

    def criar_maquina(self, especificacoes, porcentagem_uso):
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        self.__preco_aluguel = self.gerar_aluguel()
        return self

class Jogo:
    def __init__(self, titulo, requisitos):
        self.__titulo = titulo
        self.__requisitos = requisitos


lista_de_contas = []


# General Class Contada pra colocar uns hash no meio, esse é só o esqueleto)
def logar(login, senha):
    for conta in lista_de_contas:
        if [login, senha] == [conta.login, conta.senha]:
            print('logado')
            return conta
    else:
        print('Usuario ou senha incorretos')
        return None


class Conta:
    def __init__(self):
        self.Id = None
        self.login = None
        self.senha = None
        self.tipo_da_conta = None
        pass

    def __criar_conta(self, login, senha):
        lista_de_contas.append(self)

        self.login = login
        self.senha = senha
        self.Id = len(lista_de_contas)  # podemos fazer um jeito menos tantan de fazer isso depois
        return

    def cadastrar_conta(self):

        while True:
            login = input("Digite seu login")
            if login in [conta.login for conta in lista_de_contas]:
                print('Login ja usado')
                continue

            else:
                senha = input("Digite sua senha")
                # faz um hash pra deixar mais seguro
                self.__criar_conta(login, senha)
                return

    def sacar_creditos(self): #Abstract method
        pass


# Conta Specializations
class ContaDesenvolvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__jogos = list()  # Lista de jogos

    def cadastrar_jogo(self, novo_jogo):
        self.__jogos.append(novo_jogo)
        pass

    def editar_jogo(self):
        pass

    def remover_jogo(self):
        pass

    def relatorio(self):
        pass

class ContaProvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__maquina = None
        self.jogos = None
        self.ganhos = 0

    def cadastrar_maquina(self):
        especificacoes = input("Insira as Especificacoes")
        porcentagem_uso = input("Insira as Porcentagem de Uso")
        self.__maquina = Maquina().criar_maquina(especificacoes, porcentagem_uso)
        pass

    def remover_maquina(self):
        pass

    def editar_maquina(self):
        pass

    def __calcular_ganhos(self):
        if self.__maquina is None:
            print("Nenhuma maquina cadastrada")
            return None

        for maquina in self.__maquina:
            self.ganhos += maquina.ganhos
        return self.ganhos

    def sacar_creditos(self):
        #creditos = calcular_ganhos
        #receber_dinheiro(creditos)
        #self.ganhos = 0
        pass

    def alterar_aluguel(self): #Verificaremos a necessidade
        pass

    def baixar_jogo(self, jogo):
        self.__maquina.jogos.append(jogo)
        pass


class ContaJogador(Conta):
    def __init__(self, creditos, Id):
        super().__init__()
        self.__creditos = creditos

    def alugar_jogo(self):
        pass

class Transacao:
    def _init_(self):
        self.creditos = None
        
        pass

    def receber_creditos(self, creditos)

# General Class Aluguel
class Aluguel:
    def __init__(self):
        pass


# Aluguel Specializations
class AluguelJogos(Aluguel):
    def __init__(self):
        super().__init__()


class AluguelMaquinas(Aluguel):
    def __init__(self):
        super().__init__()


# General Class Relatório
class Relatorio:
    def __init__(self):
        pass


# Relatório Specializations
class RelatorioDesenvolvedor(Relatorio):
    def __init__(self):
        super().__init__()


class RelatorioProvedor(Relatorio):
    def __init__(self):
        super().__init__()


def fazer_login():
    login = input("Digite seu login")
    senha = input("Digite sua senha")


if __name__ == '__main__':
    pass
