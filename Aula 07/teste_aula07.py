class Cadastro:
    def __init__(self,nome= '',idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

class Aluno(Cadastro):
    def __init__(self,nome,idade,curso,matri):
        super().__init__(nome,idade)
        self.curso = curso
        self.matri = matri

    def fzr_matricula(self):
        pass


class Professor(Cadastro):
    def __init__(self,nome,idade,especializacao,nivel):
        super().__init__(nome,idade)
        self.especializacao = especializacao
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Cadastro):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

#Exemplo:

aluno1 = Aluno(nome= 'Anderson',idade= 16,curso= 'TI',matri= '2026')
print(aluno1.__dict__)

prof = Professor(nome= 'Jose',idade= 40,especializacao= 'Biologia',nivel= 'Mestrado')
print(prof.__dict__)

func = Funcionario(nome='Maria', idade=20, cargo='Gerente',setor='ADM')
print(func.__dict__)

