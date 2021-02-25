from time import sleep


def maior(* lst):
    cont = maior = 0
    print('-='*40)
    print('\nAnalisando os valores passados... ')
    for valor in lst:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} valor(es) ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(1, 5, 8, 12)
maior(58, 5, 664, -25)
maior(1, 2)
maior(5)