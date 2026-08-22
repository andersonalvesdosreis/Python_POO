import random
import os
from time import sleep
from abc import *
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
class Personagem(ABC):
    def __init__(self,nome='',vida=0):
        golpes = ["soco", "chute", "voadora", "ataque por trás"]
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
        self.dano = 0
        self.nova_vida = 0

    def atacar(self,alvo=object,dano=1):
        dano_gerado = random.randint(1,dano)
        golpe_escolhido = random.choice(self.golpes)
        self.dano = dano_gerado
        if self.dano > alvo.vida:
            print(f'{self.nome} atacou {alvo.nome} com {golpe_escolhido} de força {dano}')
            print(f'{alvo.nome} recebeu {self.dano} de dano!')
            print(f'\033[31mO {alvo.nome} Morreu!\033[m')
        else:
            alvo.vida = alvo.vida - dano_gerado
            print(f'{self.nome} atacou {alvo.nome} com {golpe_escolhido} de força {dano}')
            print(f'{alvo.nome} recebeu {self.dano} de dano!')
            print(f'\033[31mVida de {self.nome}: {self.vida}\nVida de {alvo.nome}: {alvo.vida}\033[m')

    @abstractmethod
    def curar(self):
        pass

class Mostrar(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)

    def mostrar(self,obj = object):
        print(f'O {obj.__class__} possui:\nNome: {self.nome}\nVida: {self.vida}\nGolpes: {self.golpes}')

class Mago(Personagem,Mostrar):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Golpe de poder supremo'
        self.golpes.append(novo_golpe)
        self.cura = random.randint(1,vida)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Mago {self.nome}, lançou um feitiço de cura!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')

    def mostrar(self, obj=object):
        return super().mostrar(obj)
    
class Guerreiro(Personagem,Mostrar):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Espadada Mortal'
        self.golpes.append(novo_golpe)
        self.cura = random.randint(1,vida)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Guerreiro {self.nome}, colocou uma bandagem!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')

    def mostrar(self, obj=object):
        return super().mostrar(obj)

class Arqueiro(Personagem,Mostrar):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Lançou uma flecha de fogo'
        self.golpes.append(novo_golpe)
        self.cura = random.randint(1,vida)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Arqueiro {self.nome}, usou suas ervas medicinais para se curar!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')

    def mostrar(self, obj=object):
        return super().mostrar(obj)

#Exemplos:

personagem1 = Guerreiro('Björn',vida=2000)
personagem2 = Arqueiro('Artemis',vida=2000)
personagem3 = Mago('Aldous',vida=2000)

#Mostrar:

personagem1.mostrar()
sleep(3)
limpar_terminal()
personagem2.mostrar()
sleep(3)
limpar_terminal()
personagem3.mostrar()
sleep(3)
limpar_terminal()

#Primeiros ataques:

personagem1.atacar(personagem3,dano=2000)
sleep(3)
limpar_terminal()
personagem2.atacar(personagem1,dano=2000)
sleep(3)
limpar_terminal()
personagem3.atacar(personagem2,dano=2000)
sleep(3)
limpar_terminal()

#Mostrar Depois do Primeiro ataque!:

personagem1.mostrar()
sleep(3)
limpar_terminal()
personagem2.mostrar()
sleep(3)
limpar_terminal()
personagem3.mostrar()
sleep(3)
limpar_terminal()