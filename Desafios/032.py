from rich import print
import hashlib
#Exercicio semelhante ao: 10
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

    def __init__(self,nome, senha, saldo = 0):
        self.__nome = nome
        self.__saldo = saldo
        mensagem_em_bytes = senha.encode('utf-8')
        hash_objeto = hashlib.sha256(mensagem_em_bytes)
        resultado = hash_objeto.hexdigest()
        self.__senha_cript = resultado

    def pedir_senha(self):
        tentativa = str(input('Digite sua senha para confirmar: '))
        mensagem_em_bytes = tentativa.encode('utf-8')
        hash_objeto = hashlib.sha256(mensagem_em_bytes)
        resultado = hash_objeto.hexdigest()
        self._tentativa = resultado
        if self._tentativa == self.__senha_cript:
            return True
        else:
            return False

    def deposito_no_saldo(self, deposito = 0):
        if self.pedir_senha() == True:
            self.__saldo += deposito
        else:
            return None

    def saque_no_saldo(self, saque = 0):
        if self.pedir_senha() == True:
            if saque <= self.__saldo:
                self.__saldo -= saque
        else:
             return None

    def __str__(self):
        return f"{'=-'*20} \n{'Nome:':<20} | {'Saldo:':<12} \n{self.__nome:<20} | R$ {self.__saldo:>9.2f}"

print('=-'*20)

pergunta = str(input('Qual seu nome? '))
pergunta_senha = str(input('Digite sua senha: '))
pergunta2 = float(input('Qual seu saldo? '))
cliente2 = ContaBancaria(nome= pergunta,senha= pergunta_senha,saldo= pergunta2)
print(cliente2)

print('=-'*20)

pergunta3 = str(input('Deseja depositar algum valor? (S= para sim)')).upper()
if pergunta3 == 'S':
    pergunta_valor = float(input('Quanto? '))
    cliente2.deposito_no_saldo(deposito=pergunta_valor)
    print(cliente2)
pergunta4 = str(input('Deseja saquar algum valor? (S= para sim)')).upper()
if pergunta4 == 'S':
    pergunta_valor = float(input('Quanto? '))
    cliente2.saque_no_saldo(saque=pergunta_valor)
    print(cliente2)
pergunta5 = str(input('Deseja ver estrutura do codigo? (S= para sim)')).upper()
if pergunta4 == 'S':
    print(ContaBancaria.__doc__)

print('=-'*20)