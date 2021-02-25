n1 = int(input('Digite o primeiro termo termo de uma PA:'))
r = int(input('Digite a razão dessa PA:'))

termo = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')  #Mostra os termos na tela
        termo += r  #Fórmula rapida pra PA
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {cont-1} termos mostrados.')
