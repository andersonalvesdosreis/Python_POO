class ContaBancaria:
    """
    Classe Para Definir conta bancaria:

    -> deposito no saldo: soma o valor depositado ao saldo
    -> saque no saldo: retira o valor sacado do saldo
    
    >> Deve informar os dados: nome = para o nome(str) e saldo = para seu saldo(int)
    >> deposito_no_saldo = para o deposito a ser realizado(int)
    >> saque_no_saldo = para a quantidade a ser retirada no saldo(int) 

    Estrutura montada:

    def __init__(self,nome, saldo = 0):               Inicializa
        self.__nome = nome    (-)Encapsulamento Privado
        self.__saldo = saldo  (-)Encapsulamento Privado

    def deposito_no_saldo(self, deposito = 0):        Deposita no Saldo
        self.saldo += deposito  Soma    (-)Encapsulamento Privado

    def saque_no_saldo(self, saque = 0):              Retira do Saldo
        if saque >= self.saldo:   Subtrai
            self.saldo -= saque      (-)Encapsulamento Privado

    def __str__(self):                                Mostra em Forma de Tabela o Resultado
        return f"{'=-'*20} {'Nome:':<20} | {'Saldo:':<12} {self.nome:<20} | R$ {self.saldo:>9.2f}"


    Codigo exemplo a ser seguido: 
    

    # cliente = ContaBancaria(nome = 'Anderson', saldo = 1000)         Parametros para serem seguidos na Classe
    # cliente.deposito_no_saldo(deposito=1000)                         Valor a ser depositado (opcional)
    # cliente.saque_no_saldo(saque=200)                                valor a ser sacado (opcional)
    # print(cliente)                                                   Mostrar no Terminal o resultado
    
    
    Autor: Anderson Alves
    """

    def __init__(self,nome, saldo = 0):
        self.__nome = nome
        self.__saldo = saldo

    def deposito_no_saldo(self, deposito = 0):
        self.__saldo += deposito

    def saque_no_saldo(self, saque = 0):
        if saque <= self.__saldo:
            self.__saldo -= saque

    def __str__(self):
        return f"{'=-'*20} \n{'Nome:':<20} | {'Saldo:':<12} \n{self.__nome:<20} | R$ {self.__saldo:>9.2f}"

