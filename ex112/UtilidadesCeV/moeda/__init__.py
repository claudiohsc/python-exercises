def metade(p, f=False):
    p /= 2
    if f:
        return f'R$' + f'{p:.2f}'
    else:
        return p


def dobro(p, f=False):
    p *= 2
    if f:
        return f'R$' + f'{p:.2f}'
    else:
        return p


def aumentar(p, dec, f=False):
    p += (dec/100) * p
    if f:
        return f'R$' + f'{p:.2f}'
    else:
        return p


def diminuir(p, dec, f=False):
    p -= (dec/100) * p
    if f:
        return f'R$' + f'{p:.2f}'
    else:
        return p


def moeda(p):
    return f'R$' + f'{p:.2f}'


def resumo(p, aum=10, dim=5):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')

    print(f'Dobro do preço: \t{dobro(p, True)}')

    print(f'Metade do preço: \t{metade(p, True)}')

    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')

    print(f'{dim}% de redução: \t{diminuir(p, dim, True)}')

    print('-' * 30)

