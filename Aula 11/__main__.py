from classes import *
from rich import inspect

av1 = Avaliacao('Anderson','Portugues',10)
av1.set_nota = 7
inspect(av1)

av2 = AvaliacaoComPropety('Anderson','Portugues',10)
av2.nota = 200
inspect(av2)