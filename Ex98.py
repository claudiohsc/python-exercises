from time import sleep



def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-='*20)
    cont = i
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)
print()
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')

ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contagem(ini, fim, pas)







