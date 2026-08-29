from abc import ABC, abstractmethod
from rich import inspect, print
from time import sleep
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Funcionario(ABC):

    def __init__(self, nome: str, salario: int | float):
        self.name = nome
        self._salario = salario

    def caucular_bonus(self):
        return 'O bonus Padrão é de R$00.00'

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, vlr: int | float):
        if vlr > self._salario:
            sleep(3)
            limpar_terminal()
            raise PermissionError('Você não tem permissão para aumentar o salario!')
        elif vlr < self._salario:
            sleep(3)
            limpar_terminal()
            raise PermissionError('Você não tem permissão para diminuir o salario!')


class Gerente(Funcionario):

    def caucular_bonus(self):
        return f'R${self._salario * 0.15:.2f}'

    def __str__(self):
        return f'O {self.name} ganha: R${self._salario} e tem um bonus de R${self._salario * 0.15:.2f}'


class Desenvolvedor(Funcionario):

    def caucular_bonus(self):
        return f'R${self._salario * 0.10:.2f}'

    def __str__(self):
        return f'O {self.name} ganha: R${self._salario} e tem um bonus de R${self._salario * 0.10:.2f}'


class Designer(Funcionario):

    def caucular_bonus(self):
        return f'R${self._salario * 0.08:.2f}'

    def __str__(self):
        return f'O {self.name} ganha: R${self._salario} e tem um bonus de R${self._salario * 0.08:.2f}'

# Criando os Objetos
desenvolvedor = Desenvolvedor('Anderson', 10000)
designer = Designer('João', 3000)
gerente = Gerente('Lucas', 5000)

# Testando os prints
print(desenvolvedor)
print(designer)
print(gerente)


# Duck Typing
def tentar_caucular(obj):
    try:
        print(obj.caucular_bonus())
    except Exception:
        raise ValueError('Não foi possivel Caucular o Bonus!')


# Conferir as coisas
#inspect(desenvolvedor)
#inspect(designer)
#inspect(gerente)

# Utilizando o Duck
tentar_caucular(desenvolvedor)
tentar_caucular(gerente)
tentar_caucular(designer)

# Testando se ele nega mudar o salario
desenvolvedor.salario = 20000 #Maior que o salario normal

#desenvolvedor.salario = 2000  #Menor que o salario normal
#desenvolvedor.salario = 10000 #Igual o salario normal
