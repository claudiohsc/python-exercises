def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num:  O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: Retorna o valor do fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(f'x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f


print(fatorial(7, show=True))
help(fatorial)