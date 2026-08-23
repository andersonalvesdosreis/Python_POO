import random
import os
from time import sleep
from abc import ABC, abstractmethod

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Personagem(ABC):
    def __init__(self, nome='', vida=0):
        self.nome = nome
        self.vida = vida
        # Lista de golpes base para todos
        self.golpes = ["soco", "chute", "voadora", "ataque por trás"]
        self.dano = 0

    def atacar(self, alvo, dano_maximo=1):
        # Removido o alvo=object, agora o alvo é obrigatório na chamada do método
        dano_gerado = random.randint(1, dano_maximo)
        golpe_escolhido = random.choice(self.golpes)
        self.dano = dano_gerado
        
        # Desconta a vida independentemente se o alvo vai morrer ou não
        alvo.vida -= dano_gerado
        
        print(f'{self.nome} atacou {alvo.nome} com {golpe_escolhido} de força {self.dano}')
        
        if alvo.vida <= 0:
            alvo.vida = 0 # Garante que a vida não fique negativa visualmente
            print(f'{alvo.nome} recebeu {self.dano} de dano!')
            print(f'\033[31mO {alvo.nome} Morreu!\033[m')
        else:
            print(f'{alvo.nome} recebeu {self.dano} de dano!')
            print(f'\033[31mVida de {self.nome}: {self.vida}\nVida de {alvo.nome}: {alvo.vida}\033[m')

    def mostrar(self):
        # self.__class__.__name__ pega o nome da classe (Mago, Guerreiro, etc.) automaticamente
        print(f'O {self.__class__.__name__} possui:\nNome: {self.nome}\nVida: {self.vida}\nGolpes: {self.golpes}')

    @abstractmethod
    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome=nome, vida=vida)
        self.golpes.append('Golpe de poder supremo')
        self.cura = random.randint(1, vida)

    def curar(self):
        self.vida += self.cura
        print(f'\033[34mO Mago {self.nome}, lançou um feitiço de cura!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome=nome, vida=vida)
        self.golpes.append('Espadada Mortal')
        self.cura = random.randint(1, vida)

    def curar(self):
        self.vida += self.cura
        print(f'\033[34mO Guerreiro {self.nome}, colocou uma bandagem!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')


class Arqueiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome=nome, vida=vida)
        self.golpes.append('Lançou uma flecha de fogo')
        self.cura = random.randint(1, vida)

    def curar(self):
        self.vida += self.cura
        print(f'\033[34mO Arqueiro {self.nome}, usou suas ervas medicinais para se curar!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')


# ================= EXEMPLOS =================

personagem1 = Guerreiro('Björn', vida=2000)
personagem2 = Arqueiro('Artemis', vida=2000)
personagem3 = Mago('Aldous', vida=2000)

# Mostrar:
personagem1.mostrar()
sleep(3)
limpar_terminal()

personagem2.mostrar()
sleep(3)
limpar_terminal()

personagem3.mostrar()
sleep(3)
limpar_terminal()

# Primeiros ataques:
personagem1.atacar(alvo=personagem3, dano_maximo=2000)
sleep(3)
limpar_terminal()

personagem2.atacar(alvo=personagem1, dano_maximo=2000)
sleep(3)
limpar_terminal()

personagem3.atacar(alvo=personagem2, dano_maximo=2000)
sleep(3)
limpar_terminal()

# Mostrar Depois do Primeiro ataque!:
personagem1.mostrar()
sleep(3)
limpar_terminal()

personagem2.mostrar()
sleep(3)
limpar_terminal()

personagem3.mostrar()