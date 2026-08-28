from rich import print
from functools import singledispatchmethod

#Aula 14 --> Overloading

class Analisador:

    @singledispatchmethod
    def analisador(self,vlr):
        print(f'Não foi possivel analisar o valor {vlr}')

    @analisador.register
    def _(self,vlr:int):
        print(f'{vlr} é um numero!')

    @analisador.register
    def _(self,vlr:str):
        print(f'{vlr} é uma cadeia de caracteres!')

obj = Analisador()
obj.analisador(3)
obj.analisador('Anderson')
obj.analisador({'Idade':34})

