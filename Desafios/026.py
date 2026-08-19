from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calc_sal(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qnt_hora, num_dias_uteis=22, num_domingos=4, num_feriados=0):
        super().__init__(nome=nome)
        self.valor_h = valor_hora
        self.qnt_h = qnt_hora
        
        valor_total_horas = self.valor_h * self.qnt_h
        self.dsr = (valor_total_horas / num_dias_uteis) * (num_domingos + num_feriados)
        self.sal_bruto = 0

    def calc_sal(self):
        self.sal_bruto = (self.valor_h * self.qnt_h) + self.dsr

    def __str__(self):
        return f'{self.nome} trabalha como horista!\nSalario Bruto -> R$ {self.sal_bruto:.2f}\nValor ganho por hora -> R$ {self.valor_h:.2f}\nQuantidade de horas -> {self.qnt_h}'

class Mensalista(Funcionario):
    def __init__(self, nome, salario_base, hrs_extras_valor=0, inss=7.5, faltas_valor=0):
        super().__init__(nome=nome)
        self.salario_base = salario_base
        self.salario_b = 0
        self.salario_l = 0
        self.hrs = hrs_extras_valor
        self.inss = inss
        self.flts = faltas_valor

    def calc_sal(self):
        self.salario_b = self.salario_base + self.hrs - self.flts
        
        desconto_inss = self.salario_b * (self.inss / 100)
        
        self.salario_l = self.salario_b - desconto_inss

    def __str__(self):
        return f'{self.nome} trabalha como mensalista!\nSalario Bruto -> R$ {self.salario_b:.2f}\nSalario Líquido (após INSS) -> R$ {self.salario_l:.2f}'

#Teste:

print("-" * 30)
func1 = Horista("João", valor_hora=15, qnt_hora=160)
func1.calc_sal()
print(func1)
    
print("-" * 30)
func2 = Mensalista("Maria", salario_base=3000, inss=9.0)
func2.calc_sal()
print(func2)
print("-" * 30)
