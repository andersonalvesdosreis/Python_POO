class MinhaClasse:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'O(a) {self.nome} tem {self.idade} anos!'

#Melhoria de codigo!

obj = MinhaClasse('Anderson',17)
if obj.nome == 15:
    obj.aniversario()
print(obj.mensagem())

obj2 = MinhaClasse('Maria',20)
print(obj2.mensagem())
