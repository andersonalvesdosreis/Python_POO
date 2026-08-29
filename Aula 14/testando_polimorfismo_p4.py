from rich import print

#Aula 14 --> Overloading

class Porta:
    def abrir(self):
        print('Girar a massaneta e empurre a porta')

class Empresa:
    def abrir(self):
        print('Cadastre um novo CNPJ')

class Ovo:
    def abrir(self):
        print('Quebre a casca')

class Pedra:
    pass

def tentar_abrir(obj):
    try:
        obj.abrir()
    except:
        print(f'Encotrei problemas ao tentar abrir {obj.__class__.__name__}')


obj1 = Porta()
obj2 = Empresa()
obj3 = Ovo()
obj4 = Pedra()

tentar_abrir(obj1)
tentar_abrir(obj2)
tentar_abrir(obj3)
tentar_abrir(obj4)
