class Caneta:
    def __init__(self, cor):
        self.tabela_cores = {
            'vermelho': '\033[31m',
            'verde': '\033[32m',
            'amarelo': '\033[33m',
            'azul': '\033[34m',
            'roxo': '\033[35m',
            'ciano': '\033[36m',
            'branco': '\033[37m',
            'parar': '\033[0m'
        }
        self.cor = cor.lower()
        self.destampada = False

    def destampar(self):
        self.destampada = True

    def tampar(self):
        self.destampada = False

    def escrever(self, text):
        final = self.tabela_cores["parar"]
        
        if not self.destampada:
            print('A caneta está tampada!')
            return

        pintando = self.tabela_cores.get(self.cor)
        if pintando:
            print(f'{pintando}{text}{final}')
        else:
            print(f'A cor "{self.cor}" não está cadastrada na caneta!')

    def quebrar_linha(self, num_de_linhas=1):
        print('\n' * num_de_linhas, end='')
#Exemplo:

c1 = Caneta("Azul")
c2 = Caneta("Vermelho")
c3 = Caneta("Verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Ola mundo')
c1.quebrar_linha(2)
c2.escrever('Isso é um teste!')
c3.escrever('Que legal!')
