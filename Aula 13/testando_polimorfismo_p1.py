from rich import print
from abc import ABC , abstractmethod

class Pessoa:
    def __init__(self,nome:str = '',idade:int = 0):
        self._nome = nome
        self._idade = idade

    def analisar_dados(self):
        print(f'O(a) {self._nome} analisa sistemas com {self._idade} anos')

    def gerencia_sistema(self):
        print(f'O(a) {self._nome} gerencia sistemas com {self._idade}')

class CO(Pessoa):
    def gerencia_sistema(self):
        print(f'O(a) {self.__class__.__name__} {self._nome}\ngerencia sistemas com {self._idade} anos de forma exepcional!')

class Funcionario(Pessoa):
    pass

class Gerente(Pessoa):
    def gerencia_sistema(self):
        print(f'O(a) {self.__class__.__name__} {self._nome}\ngerencia enormes sistemas sem nenhuma dificuldade com {self._idade}')

    def analisar_dados(self):
        print(f'O(a) {self.__class__.__name__} {self._nome}\nanalisa enormes dados sem nenhuma dificuldade com {self._idade}')

#Testes de 3 pessoas diferentes!

pessoa1 = CO('Anderson',16)
pessoa2 = Funcionario('Maria',23)
pessoa3 = Gerente('João',32)

#Testando CO

pessoa1.analisar_dados()
pessoa1.gerencia_sistema()

#Testando Funcionario

pessoa2.analisar_dados()
pessoa2.gerencia_sistema()

#Testando Gerente

pessoa3.analisar_dados()
pessoa3.gerencia_sistema()
