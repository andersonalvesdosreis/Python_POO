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


