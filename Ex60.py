num = int(input('Digite um número: '))
c = num
f = 1
print(f'Calculando {num}!')
while c > 0:
    print(f'{c} ', end='')
    print('x ' if c > 1 else f' = {f}', end='')
    f *= c
    c -= 1

