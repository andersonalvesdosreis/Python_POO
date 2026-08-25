import hashlib

class Credencial:
    def __init__(self):
        self.__senha = 'Texto Padrão'
        self.__mostrar = '' 

    @property
    def senha(self):
        return self.__mostrar

    @senha.setter
    def senha(self, msg):
        self.__senha = msg
        byts = self.__senha.encode('utf-8') 
        obj = hashlib.sha256(byts)
        self.__mostrar = obj.hexdigest() 

    def __str__(self):
        return f'{self.__mostrar}'

# Testando o código
c = Credencial()
c.senha = str(input('Digite sua senha: '))
print(f'O hash da senha digitada é: {c.senha}')