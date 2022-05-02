from queue import Empty
import time
import pickle

# from typing_extensions import Self #Isso aqui bugou qq é isso? nao sei


lista_de_contas = []
lista_de_maquinas = []
lista_de_jogos = []


class Maquina:
    precos = {'Alta': 1, 'Media': 0.7, 'Baixa': 0.5}

    def __init__(self):
        self.nome = None
        self.__especificacoes = None
        self.__porcentagem_uso = None
        self.__lista_usuarios = list()
        self.hora_aluguel = None
        self.em_uso = False
        self.horas_em_uso = 0
        self.ganhos = 0
        self.jogos = list()
        self.horas_totais = 0
        self.__provedor = None
    def get_spec(self):
        return self.__especificacoes
    def zerar_ganhos(self):
        self.__ganhos = 0
        return

    def editar(self, especificacoes, porcentagem_uso):
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        return

    def __gerar_hora_aluguel(self):
        hora_aluguel = (self.__porcentagem_uso * self.precos[self.__especificacoes]) / 10 #tava muito caro comparado com o jogo, mas isso só entra quando resetarmos as contas
        return hora_aluguel

    def criar_maquina(self, especificacoes, porcentagem_uso, nome, provedor):
        self.nome = nome
        self.__especificacoes = especificacoes
        self.__porcentagem_uso = porcentagem_uso
        self.__provedor = provedor
        self.hora_aluguel = self.__gerar_hora_aluguel()
        lista_de_maquinas.append(self)
        print(f'maquina {self} cadastrada')
        return self

    def buscar_jogo(self, titulo):
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                return jogo
        return None
        pass

    def baixar_jogo(self, titulo):
        jogo = self.buscar_jogo(titulo)
        if jogo == None:
            return False
        else:
            if jogo.titulo in self.jogos:
                return False
            else:
                jogo.registrar_maquina(self.nome)  # pra possibilitar pesquisa por máquina ou por jogo
                self.jogos.append(jogo.titulo)
                return True
        
    def pegar_lista_usuarios(self):
        print('aaaaaaaaaaaaa')
        return self.__lista_usuarios
    
    def usuario_na_lista(self, nome_usuario):
        for usuario in self.__lista_usuarios:
            if usuario == nome_usuario:
                return True
        return False
        
    def adicionar_lista_usuarios(self, nome_usuario):
        if not self.usuario_na_lista(nome_usuario):
            self.__lista_usuarios.append(nome_usuario)
        return
    
    def calcular_ganhos(self):
        self.ganhos = self.horas_em_uso * self.hora_aluguel
        self.horas_totais += self.horas_em_uso
        #self.horas_em_uso = 0
        return self.ganhos

    def get_provedor(self):
        return self.__provedor

class Jogo:
    def __init__(self):
        self.titulo = None
        self.__requisitos = None
        self.__valor = None
        self.__desenvolvedor = None
        self.__jogadores = list()
        self.maquinas = list()
        self.tempo_jogado = 0
        self.inicio = None
        self.hora_aluguel = 0
        self.tempo_total = 0

    def __gerar_hora_aluguel(self):
        self.hora_aluguel = self.__valor / 100
        return self.hora_aluguel
    def get_valor(self):
        return self.__valor
    def cadastrar(self, titulo, requisitos, valor, desenvolvedor):
        self.titulo = titulo
        self.__requisitos = requisitos
        self.__valor = valor
        self.__desenvolvedor = desenvolvedor
        self.__gerar_hora_aluguel()

        lista_de_jogos.append(self)
        print(f'jogo {self} cadastrada')
        return self

        
    def listar_jogadores(self):
        return self.__jogadores

    def editar(self, requisitos, valor):
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
        horas_jogadas = segundos_jogados / 3600
        self.tempo_jogado = horas_jogadas
        return

    def calcular_ganhos(self):
        ganhos = self.tempo_jogado * self.hora_aluguel
        self.tempo_total += self.tempo_jogado
        #self.tempo_jogado = 0
        return ganhos

    def get_desenvolvedor(self):  # Viajei achando que ia precisar disso, mas vou deixar aqui vai que
        return self.__desenvolvedor

    def alugar(self, horas):
        self.tempo_jogado += horas
        return self

class Conta:
    def __init__(self):
        self.Id = None
        self.login = None
        self.senha = None
        self.__creditos = 0


    def criar_conta(self, login, senha):
        print(self)
        lista_de_contas.append(self)
        self.login = login
        self.senha = senha
        self.Id = len(lista_de_contas)
        return

    def sacar_creditos(self):  # Abstract method
        pass

    def adicionar_creditos(self, creditos):
        self.__creditos += creditos
        return

    def descontar_creditos(self, creditos):
        self.__creditos -= creditos
        return

    def zerar_creditos(self):
        self.__creditos = 0
        return
    
    def pegar_creditos(self):
        return self.__creditos
        
    def logar(self, login, senha):
        for conta in lista_de_contas:
            if conta.login == login:
                if conta.senha == senha:
                    return True #Senha correta
                return False #Senha incorreta
        return False #Usuario não existe

# Conta Specializations
class ContaDesenvolvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__jogos = list()  # Lista de jogos
        self.tipo_da_conta = 'desenvolvedor'
        self.ganhos = 0
        self.ganhos_totais = 0

    def gerar_relatorio(self):
        relatorio=RelatorioDesenvolvedor()
        return relatorio.relatorio_desenvolvedor(self)

    def verificar_jogo_duplicado(self,titulo):
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                return True
        return False

    def cadastrar_jogo(self, titulo, requisitos, valor):
        novo_jogo = Jogo()
        if not self.verificar_jogo_duplicado(titulo):
            novo_jogo.cadastrar(titulo, requisitos, valor, self.login)
            self.__jogos.append(novo_jogo.titulo)
            return True
        else:
            return False
        pass

    def editar_jogo(self, titulo, requisitos, valor):
        for jogo in self.__jogos:
            if jogo.titulo == titulo:
                jogo.editar(requisitos, valor)

        pass

    def remover_jogo(self, titulo):
        if self.buscar_jogo(titulo):
            self.__jogos.remove(titulo)
            jogo_listado = self.buscar_jogo_listado(titulo)
            lista_de_jogos.remove(jogo_listado)
            
            return True
        else:
            return False

    def buscar_jogo(self, titulo):
        for jogo in self.__jogos:
            if jogo == titulo:
                return True
        return False

    def buscar_jogo_listado(self, titulo):
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                return jogo
        return None

    def listar_jogos(self):
        return self.__jogos


    def sacar_ganhos(self):
        creditos = self.pegar_creditos()
        print(f"Sacado ganhos: R$ {creditos}")
        self.zerar_creditos()
        return creditos

    def atualizar_ganhos_totais(self, ganho):
        self.ganhos_totais += ganho
        return

    def relatorio(self):
        pass

class ContaProvedor(Conta):
    def __init__(self):
        super().__init__()
        self.__maquinas = list()
        self.jogos = None
        self.ganhos = 0
        self.tipo_da_conta = 'provedor'
        self.ganhos_totais = 0

    def gerar_relatorio(self):
        relatorio=RelatorioProvedor()
        return relatorio.relatorio_provedor(self)

    def verificar_maquina_duplicada(self, nome):
        for maquina in lista_de_maquinas:
            if maquina.nome == nome:
                return True
        return False

    def cadastrar_maquina(self, especificacao, porcentagem, nome):
        especificacoes = especificacao
        porcentagem_uso = porcentagem
        if not self.verificar_maquina_duplicada(nome):
            maquina = Maquina().criar_maquina(especificacoes, porcentagem_uso, nome, self.login)
            self.__maquinas.append(maquina.nome)
            return True
        else:
            return False


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

    def remover_maquina(self, nome_maquina):
        if self.buscar_maquina(nome_maquina):  # Busca se tem o nome da maquina na lista do provedor
            self.__maquinas.remove(nome_maquina)  # Remove o nome da maquina da lista de maquinas
            maquina_listada = self.buscar_maquina_listada(nome_maquina)  # Busca a maquina na lista de maquinas
            lista_de_maquinas.remove(maquina_listada)  # Remove a maquina da lista de maquinas
            return True
        else:
            return False

    def editar_maquina(self, nome_maquina, especificacoes, porcentagem_uso):
        if self.buscar_maquina(nome_maquina):
            maquina = self.buscar_maquina_listada(nome_maquina)
            maquina.editar(especificacoes, porcentagem_uso)
            
    def sacar_ganhos(self):
        creditos = self.pegar_creditos()
        print(f'sacado:{creditos}')
        self.zerar_creditos()
        return creditos

    def cadastrar_jogo(self, nome_maquina, titulo):
        for maquina in lista_de_maquinas:
            if nome_maquina == maquina.nome:
                maquina.baixar_jogo(titulo)

    def atualizar_ganhos_totais(self, ganho):
        self.ganhos_totais += ganho
        return

class ContaJogador(Conta):
    def __init__(self):
        super().__init__()
        self.horas_jogadas = 0
        self.tipo_da_conta = 'jogador'
        self.__creditos_totais = 0

    def gerar_relatorio(self):
        relatorio=RelatorioJogador()
        return relatorio.relatorio_jogador(self)

    def abastecer_creditos(self, creditos):
        self.__creditos_totais += creditos
        self.adicionar_creditos(creditos)
        return

    def get_creditos_totais(self):
        return self.__creditos_totais

    def buscar_maquinas_com_jogo(self, titulo):
        maquinas_com_jogo = []
        for jogo in lista_de_jogos:
            if jogo.titulo == titulo:
                maquinas_com_jogo = jogo.maquinas

        return maquinas_com_jogo

    def gerar_tabela_maquinas(self, maquinas_com_jogo):
        tabela_maquinas = []
        for nome_maquina in maquinas_com_jogo:
            for maquina in lista_de_maquinas:
                if nome_maquina == maquina.nome:
                    tabela_maquinas.append({"nome" : maquina.nome, "especificacao" : maquina.get_spec()})

        return tabela_maquinas

    def buscar_jogos_na_maquina(self, nome_maquina):
        jogos_na_maquina = []
        for maquina in lista_de_maquinas:
            if maquina.nome == nome_maquina:
                jogos_na_maquina = maquina.jogos
        
        return jogos_na_maquina

    def gerar_tabela_jogos(self, jogos_na_maquina):
        tabela_jogos = []
        for titulo_jogo in jogos_na_maquina:
            for jogo in lista_de_jogos:
                if jogo.titulo == titulo_jogo:
                    tabela_jogos.append({"titulo" : jogo.titulo, "valor" : jogo.get_valor()})

        return tabela_jogos
    def definir_aluguel(self,nome_maquina,titulo_jogo):
        maquina_ok = False
        jogo_ok = False


        for maquina in lista_de_maquinas:
            if maquina.nome == nome_maquina:
                maquina_ok = True
                break
        if not maquina_ok:
            print("erro na maquina")
            return None, None
            
        if titulo_jogo in maquina.jogos:    
            for jogo in lista_de_jogos:
                if jogo.titulo == titulo_jogo:
                    jogo_ok = True
                    break
        if not jogo_ok:
            print ("Jogo e maquina incompativeis")
            return None, None
        return maquina, jogo

    def alugar_maquina(self, nome_maquina, titulo_jogo, horas):
        maquina, jogo = self.definir_aluguel(nome_maquina, titulo_jogo) #Se não for compativel maquina e jogo serão NONE
        

        if maquina == None:
            return False  #se não deu certo o aluguel retorna FALSE pra tentar de novo

        else:
            transacao = Transacao()
            transacao.criar_transacao(self, maquina.get_provedor(),jogo.get_desenvolvedor())
            #print(self.pegar_creditos())
            if transacao.aluguel(maquina, jogo, horas):
                #print(self.pegar_creditos())
                return True
            else:
                return False

class Transacao:
    def _init_(self):
        self.jogador = None
        self.provedor = None
        self.desenvolvedor = None


    def criar_transacao(self, jogador, provedor, desenvolvedor):
        self.jogador = jogador
        self.provedor = self.buscar_conta(provedor)
        self.desenvolvedor = self.buscar_conta(desenvolvedor)

    def buscar_conta(self, login):
        for conta in lista_de_contas:
            if conta.login == login:
                return conta

    def aluguel(self,maquina, jogo, horas):
        aluguel_maquina = maquina.hora_aluguel * horas
        aluguel_jogo = jogo.hora_aluguel * horas
        aluguel_total = aluguel_jogo + aluguel_maquina

        if self.verificar_creditos_suficientes(aluguel_total):

            maquina.horas_em_uso += horas
            jogo.tempo_jogado += horas
            self.jogador.horas_jogadas += horas

            maquina.adicionar_lista_usuarios(self.jogador.login)

            self.jogador.descontar_creditos(aluguel_total)
            #print(self.jogador.pegar_creditos())

            self.provedor.adicionar_creditos(aluguel_maquina)
            self.provedor.atualizar_ganhos_totais(aluguel_maquina)

            self.desenvolvedor.adicionar_creditos(aluguel_jogo)
            self.desenvolvedor.atualizar_ganhos_totais(aluguel_jogo)

            #self.atualizar_dados()
            return True

        else:
            return False


    def verificar_creditos_suficientes(self, custo):      
        if self.jogador.pegar_creditos() >= custo:
            return True 
        else:
            return False


    def atualizar_jogador(self):
        for conta in lista_de_contas:
            if self.jogador.login == conta.login:
                conta.creditos = self.jogador.creditos
                conta.horas_jogadas = self.jogador.horas_jogadas
        pass

    
    def atualizar_provedor(self):
        for conta in lista_de_contas:
            if self.provedor.login == conta.login:
                conta.creditos = self.provedor.creditos
        pass


    def atualizar_desenvolvedor(self):
        for conta in lista_de_contas:
            if self.desenvolvedor.login == conta.login:
                conta.creditos = self.desenvolvedor.creditos
        pass

    
    def atualizar_dados(self):
        self.atualizar_jogador()
        self.atualizar_provedor()
        self.atualizar_desenvolvedor()
        pass

# General Class Relatório
class Relatorio:
    def __init__(self):
        pass


# Relatório Specializations

class RelatorioDesenvolvedor(Relatorio):
    def __init__(self):
        super().__init__()
    
    def relatorio_desenvolvedor(self, desenvolvedor):
        relatorio = []
        for titulo_jogo in desenvolvedor.listar_jogos():
            for jogo in lista_de_jogos:
                if titulo_jogo == jogo.titulo:
                    relatorio.append({"Titulo": jogo.titulo,
                                    "Tempo jogado" : jogo.tempo_jogado,
                                    "Tempo total" : jogo.tempo_total,
                                    "Jogadores" : jogo.listar_jogadores()})
        return relatorio

class RelatorioProvedor(Relatorio):
    def __init__(self):
        super().__init__()
    
    def relatorio_provedor(self, provedor):
        relatorio = []
        for nome_maquina in provedor.listar_maquinas():
            for maquina in lista_de_maquinas:
                if nome_maquina == maquina.nome:
                    relatorio.append({"Nome" : maquina.nome,
                                    "Horas em uso" : maquina.horas_em_uso,
                                    "Ganhos" : maquina.calcular_ganhos(),
                                    "Usuarios" : maquina.pegar_lista_usuarios()})
        return relatorio

class RelatorioJogador(Relatorio):
    def __init__(self):
        super().__init__()
    
    def relatorio_jogador(self, jogador):
        relatorio = []
        relatorio.append({"Nome" : jogador.login,
                        "Creditos totais" : jogador.get_creditos_totais(),
                        "Saldo de creditos" : jogador.pegar_creditos(),
                        "Horas jogadas" : jogador.horas_jogadas})
        return relatorio

def inicializar_dados():
    with open('dados/contas', 'rb') as arquivo_contas:
        lista_de_contas.extend(pickle.load(arquivo_contas))
        # print(lista_de_contas)

    with open('dados/maquinas', 'rb') as arquivo_maquinas:
        lista_de_maquinas.extend(pickle.load(arquivo_maquinas))

    with open('dados/jogos', 'rb') as arquivo_jogos:
        lista_de_jogos.extend(pickle.load(arquivo_jogos))

    return


def salvar_dados():
    with open('dados/contas', 'wb') as arquivo_contas:
        pickle.dump(lista_de_contas, arquivo_contas)

    with open('dados/maquinas', 'wb') as arquivo_maquinas:
        pickle.dump(lista_de_maquinas, arquivo_maquinas)

    with open('dados/jogos', 'wb') as arquivo_jogos:
        pickle.dump(lista_de_jogos, arquivo_jogos)


if __name__ == '__main__':
    inicializar_dados()
    print(lista_de_contas[0].login)


    
    # conta = ContaProvedor()
    # conta.criar_conta('waldas','123')
    salvar_dados()
    pass
# aa
