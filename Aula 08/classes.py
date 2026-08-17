from abc import ABC , abstractmethod

class Cadastro(ABC):
    def __init__(self,nome= '',idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Cadastro):
    def __init__(self,nome,idade,curso,matri):
        super().__init__(nome,idade)
        self.curso = curso
        self.matri = matri

    def fzr_matricula(self):
        pass

    def estudar(self):
        return super().estudar()


class Professor(Cadastro):
    def __init__(self,nome,idade,especializacao,nivel):
        super().__init__(nome,idade)
        self.especializacao = especializacao
        self.nivel = nivel

    def dar_aula(self):
        pass

    def estudar(self):
        return super().estudar()


class Funcionario(Cadastro):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass

    def estudar(self):
        return super().estudar()
