from rich.panel import Panel
from rich import print
class Mensagem:
    def __init__(self,msg:str):
        self._mensagem = msg
        self.tabela = Panel(self._mensagem,title='Mensagem')

    def mostrar(self):
        print(self.tabela)

class Erro(Mensagem):
    def __init__(self,txt:str):
        super().__init__(msg=txt)
        self.tabela = Panel(self._mensagem,title='Erro',style="red")

class Alerta(Mensagem):
    def __init__(self,txt:str):
        super().__init__(msg=txt)
        self.tabela = Panel(self._mensagem,title='Alerta',style="yellow")

#Testando

Erro('Ola Mundo').mostrar()
Alerta('Ola Mundo').mostrar()
Mensagem('Ola Mundo').mostrar()
