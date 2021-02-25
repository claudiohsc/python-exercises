from time import sleep

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
y = -1
while y == -1:
    print('O que você deseja fazer com esses valores?'
          '\n '
          '\n[1] SOMAR'
          '\n[2] MULTIPLICAR'
          '\n[3] MAIOR'
          '\n[4] NOVOS NÚMEROS'
          '\n[5] SAIR DO PROGRAMA'
          '\n ')
    opcao = int(input('Opção: '))
    if opcao == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        y = -1
    elif opcao == 1:
        print(f'A soma dos números é {v1 + v2}')
        y = -1
    elif opcao == 2:
        print(f'O produto dos números é {v1 * v2}')
        y = -1
    elif opcao == 3:
        if v1 > v2:
            print('O maior número é ', v1)
            y = -1
        else:
            print('O maior número é ', v2)
            y = -1
    elif opcao == 5:
        print('Saindo...')
        sleep(2)
        y = 0
    else:
        print('Opção inválida, tente novamente.')
        y = -1
    sleep(2)
print('FIM')
