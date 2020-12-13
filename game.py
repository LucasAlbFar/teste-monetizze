import random
from tabulate import tabulate


class Jogo:
    def __init__(self, qtd_dezenas, total_jogos):
        self._quantidade_dezenas = self.qtd_dezenas = qtd_dezenas
        self._total_jogos = total_jogos
        self._resultado = []
        self._jogos = []

    @property
    def qtd_dezenas(self):
        return self._quantidade_dezenas

    @property
    def resultado(self):
        return self._resultado

    @property
    def total_jogos(self):
        return self._total_jogos

    @property
    def jogos(self):
        return self._jogos

    @qtd_dezenas.setter
    def qtd_dezenas(self, qtd_dezenas):
        if self.validar_qtd_dezenas(qtd_dezenas):
            self._quantidade_dezenas = qtd_dezenas
        else:
            raise ValueError("Quantidade de dezenas inválida")

    @resultado.setter
    def resultado(self, resultado):
        self._resultado = resultado

    @total_jogos.setter
    def total_jogos(self, total_jogos):
        self._total_jogos = total_jogos

    @jogos.setter
    def jogos(self, jogos):
        self._jogos.append(jogos)

    @staticmethod
    def validar_qtd_dezenas(qtd_dezenas):
        if (qtd_dezenas >= 6) & (qtd_dezenas <= 10):
            return True
        else:
            return False

    def __gerador(self, qtd_dezenas):
        numeros_gerados = []
        loop = 0
        while loop < qtd_dezenas:
            numero = random.randint(1,60)
            if not self.numero_no_array(numero, numeros_gerados):
                numeros_gerados.append(numero)
                loop += 1
        return sorted(numeros_gerados)

    @staticmethod
    def numero_no_array(numero, array_numeros):
        if numero in array_numeros:
            return True
        else:
            return False

    def fazer_jogos(self):
        qtd_jogos = self.total_jogos

        for jogo in range(qtd_jogos):
            jogada = self.__gerador(self.qtd_dezenas)
            self.jogos = jogada

    def realizar_sorteio(self):
        dezenas = 6
        self.resultado = self.__gerador(6)

    def conferir_resultado(self):
        lista_acertos = [0]*len(self.jogos)

        for i in range(len(self.jogos)):
            acertos = 0
            for sorteado in self.resultado:
                if sorteado in self.jogos[i]:
                    acertos += 1
                    lista_acertos[i] = acertos
        return lista_acertos

    def tabela_html(self):
        tabela = []
        lista_acertos = self.conferir_resultado()

        for i in range(len(self.jogos)):
            tabela.append(str(self.jogos[i]))
            tabela.append(str(lista_acertos[i]))

        print(tabulate(tabela, tablefmt='html'))

    def __str__(self):
        return f'Quantidade Dezenas: {self.qtd_dezenas} - Resultado: {self.resultado} - Total Jogos: {self.total_jogos} - Jogos: {self.jogos}'
