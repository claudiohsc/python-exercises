n1 = int(input('Digite o primeiro termo termo de uma PA:'))
r = int(input('Digite a razão dessa PA:'))
termo = n1
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
print('FIM')

