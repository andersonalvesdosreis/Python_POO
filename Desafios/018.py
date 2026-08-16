class Churrasco:
    def __init__(self,num_pessoas):
        self.num = int(num_pessoas)

    def analisar(self):
        kg = 82.40
        g = 400
        self.total_carne = self.num*0.4
        self.total_custo = self.total_carne*82.40
        self.custo_por_pessoa = self.total_custo/self.num
        print(f'O churrasco conta com {self.num} pessoas\nCada pessoa consome em media 0.4kg de carne\nRecomendado comprar {self.total_carne}Kg\nCusto total: R${self.total_custo}\nCusto por pessoa: R${self.custo_por_pessoa}')

#Exemplo:

obj = Churrasco(num_pessoas= 10)
obj.analisar()