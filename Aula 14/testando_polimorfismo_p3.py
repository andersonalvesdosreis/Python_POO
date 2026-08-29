from rich import print , inspect
from functools import singledispatchmethod

#Aula 14 --> Overloading

class Carteira:
    def __init__(self,nome:str = '', saldo:float|int = 0):
        self._nome = nome
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.getter
    def saldo(self):
        raise PermissionError('Você não tem permição para acessar isso!')

    def __str__(self):
        return (f'O(a) {self._nome}\nPossui R${self.__saldo}')

carteira1 = Carteira('Anderson',200)
print(carteira1)
#carteira1.saldo(3000)
inspect(carteira1)