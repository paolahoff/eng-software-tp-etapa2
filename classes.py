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

#General Class Contada pra colocar uns hash no meio, esse é só o esqueleto)
class Conta:
    def __init__(self, Id):
        self.Id = Id
        self.login = None
        self.senha = None
        pass
    
    def __criar_conta(self, login, senha):
        pass

    def cadastrar_conta(self):
        while True:
            login = input("Digite seu login")
            senha = input("Digite sua senha")
            #faz um hash pra deixar mais seguro
            for conta in lista_de_contas:
                if conta.conferir_login(login) is True:
                    print("Nome de usuario já está em uso")
                    continue
                #salvar conta na lista de contas
                break
    
    def conferir_login(self, login):
        if login == self.login:
            return True
        else:
            return False

    def conferir_credenciais(self, login, senha):
        if login == self.login and senha == self.senha:
            return self.Id
        else:
            return None

    
#Conta Specializations
class Conta_Desenvolvedor(Conta):
    def __init__(self, jogos):
        self.__jogos = jogos #Lista de jogos

class Conta_Provedor(Conta):
    def __init__(self, maquina):
        self.__maquina = maquina

class Conta_Jogador(Conta):
    def __init__(self, creditos):
        self.__creditos = creditos

#General Class Aluguel
class Aluguel:
    def __init__(self):
        pass

#Aluguel Specializations
class Aluguel_Jogos(Aluguel):
    def __init__(self):
        pass

class Aluguel_Maquinas(Aluguel):
    def __init__(self):
        pass

#General Class Relatório
class Relatorio:
    def __init__(self):
        pass

#Relatório Specializations
class Relatorio_Desenvolvedor(Relatorio):
    def __init__(self):
        pass

class Relatorio_Provedor(Relatorio):
    def __init__(self):
        pass


def fazer_login():
    login = input("Digite seu login")
    senha = input("Digite sua senha")
