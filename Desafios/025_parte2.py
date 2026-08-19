from abc import *
class Transporte(ABC):
    def __init__(self,distancia,frete=0):
        self.distancia = distancia
        self.frete = frete
        self.verificacao = True

    @abstractmethod
    def calcular_frete(self):
        if self.verificacao:
            return self.distancia*self.frete
        else:
            return 'A distancia segue fora do padrao!'
        

class Moto(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=0.5)

    def calcular_frete(self):
        return super().calcular_frete()
        

class Caminhão(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=1.2)
        if self.distancia < 50:
            self.verificacao = False

    def calcular_frete(self):
        return super().calcular_frete()

class Drone(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=9.5)
        if self.distancia > 10:
            self.verificacao = False

    def calcular_frete(self):
        return super().calcular_frete()

class Mostrar():
    def __init__(self,dist):
        self.distancia = dist

    def mostrar(self):
        obj1 = Moto(dist=self.distancia)
        obj2 = Caminhão(dist=self.distancia)
        obj3 = Drone(dist=self.distancia)

        print(f'Tabela de preços conforme a distancia de {self.distancia}km')
        print(f'MOTO: R${obj1.calcular_frete()}\nCaminhão: R${obj2.calcular_frete()}\nDrone: R${obj3.calcular_frete()}')

dist = 20
entrega = Mostrar(dist=dist)
entrega.mostrar()
