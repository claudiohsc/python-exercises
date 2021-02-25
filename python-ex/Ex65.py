media = cont = soma = maior = menor = 0
v = 'S'

while v == 'S':
    n1 = int(input('Digite um número: '))
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    v = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

media = soma / cont
print(f'A média dos números foi de {media}, o maior número é {maior} e o menor {menor}.')
