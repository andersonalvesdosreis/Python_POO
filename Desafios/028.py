from rich import inspect,print
class Temperatura:
    def __init__(self,temperatura=24):
        self.__temperatura = float(temperatura)
        self.temp_inicial = 24 #Temperatura inicial

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,nova_temperatura):
        if 16 <= nova_temperatura <= 30 and nova_temperatura % 0.5 == 0:
            self.__temperatura = nova_temperatura
        else:
            print(f'{nova_temperatura}°C se encontra fora dos parametros exigidos\nParametros -> valor inteiro (entre 16 a 30) ou com 0,5')

temp1 = Temperatura()
temp1.temperatura = 3000
temp1.temperatura = 21
inspect(temp1)
