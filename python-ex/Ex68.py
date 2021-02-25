from random import randint
cont = 0
print("=-"*30)
print('VAMOS JOGAR PAR OU ÍMPAR.')
print("=-"*30)
escolha = ' '
while True:
    jogador = int(input('Digite um valor: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    pc = randint(0, 10)
    soma = jogador + pc
    result = 'I ou P'
    if soma % 2 == 0: #Descobrir se o total é par ou ímpar
        result = 'P'
    else:
        result = 'I'
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}.')
    print('Deu PAR' if result == 'P' else 'Deu Ímpar')
    print('-'*30)
    if result == escolha:
        cont += 1
        print('Você VENCEU!'
              '\nVamos jogar novamente...')
        print('-' * 30)
        escolha = ' '
    else:
        print('Você PERDEU!')
        print('-=' * 20)
        print(f'GAME OVER! Você venceu {cont} vez(es).')
        break

