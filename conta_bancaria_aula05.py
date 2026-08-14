import classe_aula05
print('=-'*20)

pergunta = str(input('Qual seu nome? '))
pergunta2 = int(input('Qual seu saldo? '))
cliente2 = ContaBancaria(nome= pergunta,saldo= pergunta2)
print(cliente2)

print('=-'*20)

pergunta3 = str(input('Deseja depositar algum valor? (S= para sim)')).upper()
if pergunta3 == 'S':
    pergunta_valor = int(input('Quanto? '))
    cliente2.deposito_no_saldo(deposito=pergunta_valor)
    print(cliente2)
pergunta4 = str(input('Deseja saquar algum valor? (S= para sim)')).upper()
if pergunta4 == 'S':
    pergunta_valor = int(input('Quanto? '))
    cliente2.saque_no_saldo(saque=pergunta_valor)
    print(cliente2)
