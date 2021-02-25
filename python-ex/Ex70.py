print('-='*20)
print('{:-^40}'.format("LOJAS TEND TUDO"))
print('-='*20)
mil = soma = menor = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    soma += preco
    if preco >= 1000:
        mil += 1
    if preco <= preco:
        menor = preco
        nomemenor = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        print('======FIM DO PROGRAMA======')
        print(f'O total da compra foi de R${soma}')
        print(f'Temos {mil} produto(s) custando mais de R$1000.00')
        print(f'O produto mais barato foi {nomemenor} que custa R${menor}')
        break
