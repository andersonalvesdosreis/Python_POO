class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = 0
        self._altura = 0
        self._area = None
        self.base = base
        self.altura = altura
        
    @property
    def base(self):
        return self._base
   
    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor
            self._area = self.area
        else:
            raise ValueError('Valor inválido para a Base!')
        
    @property
    def altura(self):
        return self._altura
        
    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
            self._area = self.area
        else:
            raise ValueError('Valor inválido para a Altura!')
        
    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nArea = {self.area}'
        
    @medidas.setter
    def medidas(self, valor):
        self.base = valor[0]
        self.altura = valor[1]
        
    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area
    