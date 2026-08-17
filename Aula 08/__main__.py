from classes import Aluno, Professor , Funcionario

#Exemplo:

aluno1 = Aluno(nome= 'Anderson',idade= 16,curso= 'TI',matri= '2026')
print(aluno1.__dict__)

prof = Professor(nome= 'Jose',idade= 40,especializacao= 'Biologia',nivel= 'Mestrado')
print(prof.__dict__)

func = Funcionario(nome='Maria', idade=20, cargo='Gerente',setor='ADM')
print(func.__dict__)

