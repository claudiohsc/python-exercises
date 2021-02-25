print('Controle de Terrenos')
print('-' * 30)


def area(largura, comprimento):
    areat = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é {areat} m².')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
