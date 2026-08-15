class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f'Olá eu sou o(a) {self.nome}\ntrabalho no setor: {self.setor}\ne estou atualmente no cargo: {self.cargo}'

funcionario = Funcionario('Anderson','Vendas','Gerente')
print(funcionario)