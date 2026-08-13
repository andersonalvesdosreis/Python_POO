#Estrutura Exemplo de Objeto!
# 
# Cliente:
# 
# Atributos:
# 
# Nome: CPF: Valor_da_compra: Metodo_de_pagamento: Data: Hora:
#
# Metodos:
#
# Entregar_o_produto_comprado() Devolução() Reembolso() Desconto()
#
def pergunta(text):
    pergunta = str(input(f'Deseja {text}? S/N '))
    return pergunta


class Cliente:
    def __init__(self):
        self.nome = ''
        self.cpf = 0
        self.valor_da_compra = 0
        self.metodo_de_pagamento = ''
        self.data = '00/00/00'
        self.hora = '00:00'


    def condicional(self):
        #Condicional:
     p1 = pergunta('devolução')
     if p1 in 'S':
         return f'a compra efetuada por {self.nome} no valor de {self.valor_da_compra} foi devolvida!'
     p2 = pergunta('reembolso')
     if p2 in 'S':
         return f'a compra efetuada por {self.nome} no valor de {self.valor_da_compra} foi reembolsada'
     p3 = pergunta('Desconto')
     if p3 in 'S':
         self.valor_da_compra = self.valor_da_compra - (self.valor_da_compra*0.10)

    def mensagem(self):
        return f'O Cliente {self.nome} com o cpf {self.cpf} realizou uma compra de R${self.valor_da_compra} no dia {self.data} no metodo de pagamento {self.metodo_de_pagamento}'

#Instanciamento:

cliente = Cliente()
cliente.nome = 'Anderson'
cliente.cpf = 12345678910
cliente.valor_da_compra = 100
cliente.metodo_de_pagamento = 'Pix'
cliente.data = '10/03/26'
cliente.hora = '13:09'

#Mostrar o Codigo:

print(cliente.condicional())
print(cliente.mensagem())
