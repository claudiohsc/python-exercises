def leiaInt(txt=''):
    try:
        n = input('Digite um número: ')
        while not n.isnumeric():
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            n = input('Digite um número: ')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar um número')
        return 0
    return n


def leiaFloat(txt=''):
    try:
        n = input('Digite um número real: ').replace(',', '.')
        float(n)
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar um número')
        n = 0
    except ValueError:
        print('\033[0;31mErro! Digite um número real válido.\033[m')
        n = input('Digite um número real: ')
    finally:
        print('Volte sempre!!')
    return n

n1 = leiaInt()
n2 = leiaFloat()
print(f'Você digitou o número inteiro {n1} e o real {n2}.')