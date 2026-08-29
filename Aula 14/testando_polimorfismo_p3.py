from rich import print , inspect
from functools import singledispatchmethod

#Aula 14 --> Overloading

class Carteira:
    def __init__(self ,saldo:float|int = 0):
        self.__saldo = saldo

    def __iadd__(self, other:int|float):
        self.__saldo = self.__saldo + other
        return self
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.getter
    def saldo(self):
        raise PermissionError('Você não tem permição para acessar isso!')

    def __str__(self):
        return (f'Você Possui R${self.__saldo}')

carteira1 = Carteira(200)
carteira1 += 20
print(carteira1)


#Caso tente rodar o programa retorna erro!
# --> carteira1.saldo(3000)

#inspect(carteira1)