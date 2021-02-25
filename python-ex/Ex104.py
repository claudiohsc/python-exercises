def leiaInt(txt=''):
    n = input('Digite um número: ')
    while not n.isnumeric():
        print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        n = input('Digite um número: ')
    print(f'Você digitou um número inteiro: {n}')


leiaInt()
