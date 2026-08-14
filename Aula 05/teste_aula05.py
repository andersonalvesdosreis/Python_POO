class MinhaClasse:
    """
    Representa uma pessoa com nome e idade.

    Attributes:
        nome (str): O nome da pessoa. O valor padrão é uma string vazia.
        idade (int): A idade da pessoa em anos. O valor padrão é 0.
    """
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'O(a) {self.nome} tem {self.idade} anos!'

#Melhoria de codigo!

obj = MinhaClasse('Anderson',17)
print(obj)
