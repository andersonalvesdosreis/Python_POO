from abc import *
class Poligono(ABC):

    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self,valor):
        self.valor = valor

    def perimetro(self,x):
        return 4*x

    def area(self,x):
        return x**2

    def analisar(self):
        print(f'Area: {self.area(x= self.valor)}')
        print(f'Perimetro: {self.perimetro(x= self.valor)}')

class Circulo(Poligono):
    def __init__(self,num):
        self.num = num

    def perimetro(self,x):
        return 3.14*(x**2)

    def area(self,x):
        return (2*3.14)*x

    def analisar(self):
        print(f'Considerando PI como 3,14!')
        print(f'Area: {self.area(x= self.num):.2f}')
        print(f'Perimetro: {self.perimetro(x= self.num):.2f}')

#Testes

poligono1 = Quadrado(12)
poligono1.analisar()

poligono2 = Circulo(20)
poligono2.analisar()