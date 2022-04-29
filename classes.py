import time
import pickle
#from typing_extensions import Self #Isso aqui bugou qq é isso?


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
        lista_de_maquinas.append(self)
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
        return self
    
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

    def buscar_jogo(self,titulo):
        for jogo in self.__jogos:
            if jogo == titulo:
                return True
        
        return False

    def buscar_jogo_listado(self,titulo):
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                return jogo
       
        return None

    def calcular_ganhos(self):           #Acho que vai ser melhor fazer a busca desse jeito, por mais que seja 
        if self.__jogos is None:         #mais longo, pois vai ser mais fácil de guardar no banco de dados vulgo TXT
            print("Nenhum jogo cadastrado")
            for titulo_jogo in self.__jogos:
                jogo = self.buscar_jogo_listado(titulo_jogo)
                self.ganhos += jogo.calcular_ganhos()
            return self.ganhos

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
        maquina = Maquina().criar_maquina(especificacoes, porcentagem_uso ,nome)
        self.__maquinas.append(maquina.nome)
        pass

    def listar_maquinas(self):
        return self.__maquinas

    def buscar_maquina(self, nome_maquina):
        for maquina in self.__maquinas:
            if maquina == nome_maquina:
                return True

        return False

    def buscar_maquina_listada(self, nome_maquina):
        for maquina_listada in lista_de_maquinas:
            if maquina_listada.nome == nome_maquina:
                return maquina_listada
        return None

    def remover_maquina(self ,nome_maquina):
        if self.buscar_maquina(nome_maquina):                   #Busca se tem o nome da maquina na lista do provedor
            self.__maquinas.remove(nome_maquina)                #Remove o nome da maquina da lista de maquinas
            maquina_listada = self.buscar_maquina_listada       #Busca a maquina na lista de maquinas
            lista_de_maquinas.remove(maquina_listada)           #Remove a maquina da lista de maquinas
            return True
        else:   
            return False

    def editar_maquina(self, nome_maquina, nome_novo, especificacoes, porcentagem_uso):
        if self.buscar_maquina(nome_maquina):
            maquina = self.buscar_maquina_listada(nome_maquina)
            maquina.editar(nome_novo, especificacoes, porcentagem_uso)
            if nome_novo is not nome_maquina:
                self.__maquinas = list(map(lambda x: x.replace(nome_maquina, nome_novo), self.__maquinas)) #Se o nome novo for diferente altera ele também na lista do provedor
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


def inicializar_dados():
    with open('dados/contas', 'rb') as arquivo_contas:
        lista_de_contas.extend(pickle.load(arquivo_contas))
        #print(lista_de_contas)
    
    with open('dados/maquinas', 'rb') as arquivo_maquinas:
        lista_de_maquinas.extend(pickle.load(arquivo_maquinas))
    
    with open('dados/jogos', 'rb') as arquivo_jogos:
        lista_de_jogos.extend(pickle.load(arquivo_jogos))

    return

def salvar_dados():
    with open('dados/contas', 'wb') as arquivo_contas:
        pickle.dump(lista_de_contas,arquivo_contas)
    
    with open('dados/maquinas', 'wb') as arquivo_maquinas:
        pickle.dump(lista_de_maquinas,arquivo_maquinas)
    
    with open('dados/jogos', 'wb') as arquivo_jogos:
        pickle.dump(lista_de_jogos,arquivo_jogos)


if __name__ == '__main__':
    inicializar_dados()
    print(lista_de_contas[0].login)
    #conta = ContaProvedor()
    #conta.criar_conta('waldas','123')
    salvar_dados()
    pass
# aa
