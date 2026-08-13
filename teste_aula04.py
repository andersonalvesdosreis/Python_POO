class MinhaClasse:
    def __init__(self):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'O(a) {self.nome} tem {self.idade} anos!'

#Teste com o primeiro objeto!

obj = MinhaClasse()
obj.nome = 'Anderson'
obj.idade = 16
if obj.nome == 15:
    obj.aniversario()
print(obj.mensagem())

#Teste com o segundo objeto!

obj2 = MinhaClasse()
obj2.nome = 'Maria'
obj2.idade = 20
print(obj2.mensagem())

