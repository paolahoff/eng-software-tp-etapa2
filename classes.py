
lista_de_contas = []


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


class Jogo:
    def __init__(self, titulo, requisitos, valor):
        self.__titulo = titulo
        self.__requisitos = requisitos
        self.__valor = valor





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

    def baixar_jogo(self, jogo):
        self.__maquinas.jogos.append(jogo)
        pass


class ContaJogador(Conta):
    def __init__(self):
        super().__init__()
        self.__creditos = 0
        self.tipo_da_conta = 'jogador'

    def alugar_jogo(self):
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
