class Avaliacao:
    def __init__(self,nome,disciplina,nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_nota(self,valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('ERRO')

class AvaliacaoComPropety:
    def __init__(self,nome,disciplina,nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self,valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('ERRO')