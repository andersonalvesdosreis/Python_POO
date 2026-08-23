from abc import ABC, abstractmethod
from rich import print,inspect
from datetime import datetime


class Pessoa(ABC):
    ano_atual = datetime.today().year
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def idade(self):
        return (self.ano_atual - self._nascimento)


    @nascimento.setter
    def nascimento(self, valor:int):
        if (self.ano_atual-100) <= valor <= (self.ano_atual-7):
            self._nascimento = valor
        else:
            raise ValueError(f"Ano {valor} é inválido!")

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")
    
class Aluno(Pessoa):
    cursos_oficiais = ['Administração', 'Analise e Desenvolvimento de Sistemas',
                       'Inglês', 'Espanhol', 'Francês', 'Italiano',
                       'Culinária', 'Artes Cenicas', 'Arquitetura',
                       'Dança', 'Balé', 'Pintura', 'Empreendedorismo']
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor:str):
        if valor in self.cursos_oficiais:
            self._curso = valor
        else:
            raise ValueError(f"O curso {valor} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        self.cursos_oficiais.append(curso)


aluno1 = Aluno('Pedro', 2002, 'Culinária')

aluno1.add_curso('Moda')
aluno1.curso = 'Moda'
aluno1.nascimento = 2003
inspect(aluno1, private=True, methods=True)