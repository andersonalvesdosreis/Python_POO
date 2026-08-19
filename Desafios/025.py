from abc import *
class Transporte(ABC):
    def __init__(self,distancia,frete=0):
        self.distancia = distancia
        self.frete = frete
        self.verficacao = True

    @abstractmethod
    def caucular_frete(self):
        if self.verificacao:
            return self.distancia*self.frete
        else:
            return 'A distancia segue fora do padrao!'
        

class Moto(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=0.5)

    def caucular_frete(self):
        return super().caucular_frete()
        

class Caminhão(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=1.2)
        if self.distancia < 50:
            self.verificacao = False

    def caucular_frete(self):
        return super().caucular_frete()

class Drone(Transporte):
    def __init__(self,dist):
        super().__init__(distancia=dist,frete=9.5)
        if self.distancia > 10:
            self.verificacao = False

    def caucular_frete(self):
        return super().caucular_frete()

#Teste:

dist = 20
entrega = Drone(dist=dist)

print(f'O total do frete foi: R${entrega.caucular_frete()}')
