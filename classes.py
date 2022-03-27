class Maquina:
    def __init__(self, especificacoes, porcentagem_uso, preco_aluguel):
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        self.__preco_aluguel = preco_aluguel
        self.em_uso = False
        self.horas_em_uso = 0


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


# Conta Specializations
class ContaDesenvolvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__jogos = list  # Lista de jogos

    def cadastrar_jogo(self, novo_jogo):
        self.__jogos.append(novo_jogo)
        pass


class ContaProvedor(Conta):
    def __init__(self, maquina, Id):
        super().__init__()
        self.__maquina = maquina
        self.jogos = None

    def baixar_jogo(self, jogo):
        self.jogos.append(jogo)
        pass


class ContaJogador(Conta):
    def __init__(self, creditos, Id):
        super().__init__()
        self.__creditos = creditos

    def alugar_jogo(self):
        pass


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
