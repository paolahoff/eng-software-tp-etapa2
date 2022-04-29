import time
from typing_extensions import Self


lista_de_contas = []
lista_de_maquinas = []
lista_de_jogos = []


class Maquina:
    precos = {'Alta': 1, 'Media': 0.7, 'Baixa': 0.5}

    def __init__(self):
        self.nome = None
        self.__especificacoes = None
        self.__porcentagem_uso = None
        self.hora_aluguel = None
        self.em_uso = False
        self.__horas_em_uso = 0
        self.__ganhos = 0
        self.jogos = list()

    def zerar_ganhos(self):
        self.__ganhos = 0
        return

    def editar(self, nome, especificacoes, porcentagem_uso):
        self.nome = nome
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        return

    def __gerar_hora_aluguel(self):
        hora_aluguel = self.__porcentagem_uso * self.precos[self.__especificacoes]
        return hora_aluguel

    def criar_maquina(self, especificacoes, porcentagem_uso ,nome):
        self.nome = nome
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        self.hora_aluguel = self.__gerar_hora_aluguel()
        print(f'maquina {self} cadastrada')
        return self


    def buscar_jogo(self,titulo):
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                return jogo
        return None
        pass

    
    def baixar_jogo(self, titulo):
        jogo = self.buscar_jogo(titulo)
        if jogo == None:
            return None
        else:
            jogo.registrar_maquina() #pra possibilitar pesquisa por máquina ou por jogo
            self.jogos.append(jogo) # Não sei se fazemos assim ou colocando apenas o Titulo
        pass

class Jogo:
    def __init__(self):
        self.__titulo = None
        self.__requisitos = None
        self.__valor = None
        self.__desenvolvedor = None
        self.__jogadores = list()
        self.maquinas = list()
        self.tempo_jogado = 0
        self.inicio = None

    def cadastrar(self, titulo, requisitos, valor, desenvolvedor):
        self.__titulo = titulo
        self.__requisitos = requisitos
        self.__valor = valor
        self.__desenvolvedor = desenvolvedor
    
        lista_de_jogos.append(self)
        print(f'jogo {self} cadastrada')
        return Self
    
    def editar(self, titulo, requisitos, valor):
        self.__titulo = titulo
        self.__requisitos = requisitos
        self.__valor = valor

    def registrar_maquina(self, maquina):
        self.maquinas.append(maquina)

    def iniciar(self):
        self.inicio = time.time()
        return

    def encerrar(self):
        fim = time.time()
        segundos_jogados = (fim - self.inicio)
        horas_jogadas = segundos_jogados/3600
        self.tempo_jogado = horas_jogadas
        return
    
    def calcular_ganhos(self):
        ganhos = round(self.tempo_jogado) * self.__valor
        self.tempo_jogado = 0
        return ganhos
    

    def get_desenvolvedor(self): #Viajei achando que ia precisar disso, mas vou deixar aqui vai que
        return self.__desenvolvedor



class Conta:
    def __init__(self):
        self.Id = None
        self.login = None
        self.senha = None
        pass

    def criar_conta(self, login, senha):
        print(self)
        lista_de_contas.append(self)
        self.login = login
        self.senha = senha
        self.Id = len(lista_de_contas)
        return

    def sacar_creditos(self):  # Abstract method
        pass


# Conta Specializations
class ContaDesenvolvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__jogos = list()  # Lista de jogos
        self.tipo_da_conta = 'desenvolvedor'
        self.ganhos = 0

    def cadastrar_jogo(self, titulo, requisitos, valor):
        novo_jogo = Jogo()
        novo_jogo.cadastrar(titulo, requisitos, valor, self.login)
        self.__jogos.append(novo_jogo)
        pass

    def editar_jogo(self, titulo, titulo_novo, requisitos, valor):
        for jogo in self.__jogos:
            if jogo.titulo ==  titulo:
                jogo.editar(titulo_novo, requisitos, valor)
        pass

    def remover_jogo(self, titulo):
        for jogo in self.__jogos:
            if jogo.titulo ==  titulo:
                self.__jogos.remove(jogo)
        pass

    def calcular_ganhos(self):           #Acho que vai ser melhor fazer a busca desse jeito, por mais que seja 
        if self.__jogos is None:         #mais longo, pois vai ser mais fácil de guardar no banco de dados vulgo TXT
            print("Nenhum jogo cadastrado")
            for titulo_jogo in self.__jogos:
                for jogo in lista_de_jogos:
                    if jogo.titulo == titulo_jogo:
                        self.ganhos = jogo.calcular_ganhos()

    def sacar_ganhos(self):
        creditos = self.calcular_ganhos
        print(f"Sacado ganhos: R$ {creditos}")
        self.ganhos = 0
        return creditos

    def relatorio(self):
        pass


class ContaProvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__maquinas = list()
        self.jogos = None
        self.ganhos = 0
        self.tipo_da_conta = 'provedor'

    def cadastrar_maquina(self, especificacao, porcentagem ,nome):
        especificacoes = especificacao
        porcentagem_uso = porcentagem
        self.__maquinas.append(Maquina().criar_maquina(especificacoes, porcentagem_uso ,nome))
        pass

    def listar_maquinas(self):
        return self.__maquinas

    def remover_maquina(self ,nome_maquina):
        for maquina in self.__maquinas:
            if maquina.nome == nome_maquina:
                self.__maquinas.remove(maquina)
                return True
        return False

    def editar_maquina(self, nome_maquina, nome_novo, especificacoes, porcentagem_uso):
        for maquina in self.__maquinas:
            if maquina.nome == nome_maquina:
                maquina.editar(nome_novo ,especificacoes, porcentagem_uso)
                return True
        pass

    def calcular_ganhos(self):
        if self.__maquinas is None:
            print("Nenhuma maquina cadastrada")
            return None

        for maquina in self.__maquinas:
            self.ganhos += maquina.ganhos
        return self.ganhos

    def sacar_creditos(self):
        creditos = self.calcular_ganhos
        for maquina in self.__maquinas:
            maquina.zerar_ganhos()
        print(f'sacado:{creditos}')
        self.ganhos = 0
        pass

    def alterar_aluguel(self):  # Verificaremos a necessidade
        pass

    def cadastrar_jogo(self, nome_maquina, titulo):
        for maquina in lista_de_maquinas:
            if nome_maquina == maquina.nome:
                maquina.baixar_jogo(titulo)
        pass


class ContaJogador(Conta):
    def __init__(self):
        super().__init__()
        self.__creditos = 0
        self.tipo_da_conta = 'jogador'

    def alugar_maquina(self):

        pass


class Transacao:
    def _init_(self):
        self.creditos = None

        pass

    def receber_creditos(self, creditos):
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


if __name__ == '__main__':
    pass
# aa
