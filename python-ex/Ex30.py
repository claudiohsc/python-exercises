numero = int(input('Digite um número para saber se é par ou ímpar: '))
resto = numero % 2

if resto == 0:
    print('O número escolhido é par.')
else:
    print('O número escolhido é ímpar.')
