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
    def __init__(self, dist):
        self.distancia = dist

    def mostrar(self):

        veiculos = [
            Moto(dist=self.distancia),
            Caminhão(dist=self.distancia),
            Drone(dist=self.distancia)
        ]

        print(f'Tabela de preços conforme a distancia de {self.distancia}km:')
        print('-' * 40)
        
        for veiculo in veiculos:

            nome = veiculo.__class__.__name__ 
            resultado = veiculo.calcular_frete()
            print(f'{nome}: R${resultado}')

dist = 20
entrega = Mostrar(dist=dist)
entrega.mostrar()
