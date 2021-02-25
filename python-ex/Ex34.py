salario = float(input('Digite seu salário: R$'))
if salario<=1250:
    print(f'O novo salário será de R${salario+(salario*15/100)}')
else:
    print(f'O novo salário será de R${salario+(salario*10/100)}')