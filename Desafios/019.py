from time import sleep
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Livro:
    def __init__(self,num,nome= ''):
        self.numero = num
        self.nome = nome
        self.pagina_atual = 1

    def avancar_pagina(self,num_avancar):
        print(f'Você mandou avançar {num_avancar} paginas!')
        sleep(3)
        limpar_terminal()
        for n in range(num_avancar+1):
            if self.pagina_atual >= self.numero:
                print('Chegou ao Limite, Não tem como avançar!')
                sleep(3)
                limpar_terminal()
                break
            else:
                self.pagina_atual += 1
                print(f'Você esta na pagina -> {self.pagina_atual}')
                print(f'Avançando para proxima pagina...')
                sleep(3)
                limpar_terminal()
                continue
        print(f'Pronto! Você chegou a pagina {self.pagina_atual}/{self.numero}')

    def __str__(self):
        return f'Olá Você abriu o livro {self.nome}\ne está na paigna {self.pagina_atual}\nO livro possui {self.numero} paginas'

#Exemplo:

nome = str(input('Qual o nome do Livro? '))
sleep(2)
limpar_terminal()
pergunta_principal = int(input(f'O livro {nome} possui quantas paginas? '))
sleep(2)
limpar_terminal()
l1 = Livro(num= pergunta_principal,nome= nome)
pergunta = int(input('Deseja avançar quantas paginas? '))
sleep(2)
limpar_terminal()
l1.avancar_pagina(pergunta)
sleep(2)
limpar_terminal()
print(l1)
