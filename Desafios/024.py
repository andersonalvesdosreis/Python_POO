from abc import *
class BebidaQuente(ABC):

    def ferver_agua(self):
        return 'Fervendo a Agua a 100 graus Celsius'

    def misturar(self):
        pass

    def servir(self):
        pass

    def preparar(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        return 'Passando em agua pressurizada'

    def servir(self):
        return 'Servindo em xicara pequena'

    def preparar(self):
        print(f'---- Inicio ----\n1 - {super().ferver_agua()}\n2 - {self.misturar()}\n3 - {self.servir()}\n---- FIM ----')

class Cha(BebidaQuente):

    def misturar(self):
        return 'Mergulhando o sachê de ervas na agua'

    def servir(self):
        return 'Servindo em caneca'

    def preparar(self):
        print(f'---- Inicio ----\n1 - {super().ferver_agua()}\n2 - {self.misturar()}\n3 - {self.servir()}\n---- FIM ----')

class Leite(BebidaQuente):

    def misturar(self):
        return 'Passando por vapor pressurizado pelo bico do leite'

    def servir(self):
        return 'Servindo junto do Café'

    def preparar(self):
        print(f'---- Inicio ----\n1 - {super().ferver_agua()}\n2 - {self.misturar()}\n3 - {self.servir()}\n---- FIM ----')

#Testes:

obj1 = Cafe()
obj1.preparar()

obj2 = Cha()
obj2.preparar()

obj3 = Leite()
obj3.preparar()

