class ContaBancaria:
    """
    Classe Para Definir conta bancaria:

    -> deposito no saldo: soma o valor depositado ao saldo
    -> saque no saldo: retira o valor sacado do saldo
    
    >> Deve informar os dados: nome = para o nome(str) e saldo = para seu saldo(int)
    >> deposito_no_saldo = para o deposito a ser realizado(int)
    >>saque_no_saldo = para a quantidade a ser retirada no saldo(int)
    """

    def __init__(self,nome = ' ', saldo = 0):
        self.nome = nome
        self.saldo = saldo

    def deposito_no_saldo(self, deposito = 0):
        self.saldo += deposito

    def saque_no_saldo(self, saque = 0):
        self.saldo -= saque

    def __str__(self):
        return f"{self.nome:<20} | R$ {self.saldo:>9.2f}"

