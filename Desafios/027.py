import random
from abc import *
class Personagem(ABC):
    def __init__(self,nome='',vida=0):
        golpes = ["soco", "chute", "voadora", "ataque por trás"]
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
        self.dano = 0
        self.nova_vida = 0
        self.cura = random.randint(1,vida)

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

class Mago(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Golpe de poder supremo'
        self.golpes.append(novo_golpe)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Mago {self.nome}, lançou um feitiço de cura!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')

class Guerreiro(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Espadada Mortal'
        self.golpes.append(novo_golpe)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Guerreiro {self.nome}, colocou uma bandagem!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')

class Arqueiro(Personagem):
    def __init__(self,nome,vida):
        super().__init__(nome=nome,vida=vida)
        novo_golpe = 'Lançou uma flecha de fogo'
        self.golpes.append(novo_golpe)

    def curar(self):
        self.vida = self.vida + self.cura
        print(f'\033[34mO Arqueiro {self.nome}, usou suas ervas medicinais para se curar!\033[m\nE recuperou {self.cura} de vida\nVida de {self.nome}: {self.vida}')
