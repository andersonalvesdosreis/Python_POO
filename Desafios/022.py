from time import sleep
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class ControleRemoto:
    def __init__(self):
        canais = {
            1:'Notícias 📰',
            2:'Filmes & Séries 🎬',
            3:'Esportes ⚽',
            4:'Música & Shows 🎶'
        }
        self.canais = canais
        self.tv = False
        self.volume = 0
        self.canal = 1

    def vol(self, volume):
        volume_max = 5
        volume_min = 0
        if self.tv:
            if volume == '+':
                if self.volume < volume_max:
                    self.volume += 1
            elif volume == '-':
                if self.volume > volume_min:
                    self.volume -= 1

    def cnl(self,canal):
        canal_max = 4
        canal_min = 1
        if self.tv:
            if canal in '>':
                if self.canal < canal_max:
                    self.canal += 1
            elif canal in '<':
                if self.canal > canal_min:
                    self.canal -= 1
        


    def pergunta(self):
        pergunta = input(f'< CH{self.canal} >  - Vol{self.volume} +  @ On/Off: ')
        if pergunta in '+-':
            self.vol(volume=pergunta)
        elif pergunta == '@':
            self.tv = not self.tv
        elif pergunta in '<>':
            self.cnl(canal=pergunta)

    def exibir(self):
        while True:
            limpar_terminal() 
            
            print("┌" + "─" * 38 + "┐")
            print(f"│ {'Painel Da Tv':^36} │")
            print("├" + "─" * 38 + "┤")
            
            if self.tv:
                print(f"│ Canal de  : {self.canais[self.canal]:<23} │")
                print(f"│ Volume     : {self.volume:<23} │")
            else:
                print(f"│  TV -> \033[31mDESLIGADA\033[m                     │")
                
            print("├" + "─" * 38 + "┤")
            self.pergunta()


controle = ControleRemoto()
controle.exibir()