n1 = 0
soma = 0
cont = 0

while n1 != 999:
    n1 = int(input('Digite um número [999 para parar]: '))
    soma += n1
    cont += 1
print(f'A soma total dos números foi de {(soma-999)} e'
      f'\nvocê digitou {cont-1} número(s).')
