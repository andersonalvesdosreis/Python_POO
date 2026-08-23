from rich import inspect,print
from time import sleep
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
class Diario:
    def __init__(self,senha):
        self.__segredos = []
        self.__senha = str(senha)

    @property
    def escrever(self):
        return self.__segredos

    @escrever.setter
    def escrever(self,msg = ""):
        self.__segredos.append(msg)

    @property
    def acessar(self):
        return self.__senha

    @acessar.setter
    def acessar(self,tentativa):
        if tentativa == self.__senha:
            print('Um momento, Abrindo o diario...')
            sleep(3)
            limpar_terminal()
            print(f'Tudo que está escrito no Diario:\n{self.__segredos}')
        else:
            raise PermissionError (f'A senha {tentativa} não foi encontrada!')

diario1 = Diario('@#And')
diario1.escrever = 'Ola Mundo'
diario1.escrever = 'Este é o Desafio de numero 029!'
diario1.escrever = 'Começei a estudar python em Novembro de 2025, Parece como se fosse ontem kkkkkk'
#inspect(diario1)
#diario1.acessar = '@#Nnd'
diario1.acessar = '@#And'