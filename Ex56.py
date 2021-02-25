somaidade = 0
mediaidade = 0
maioridade_homem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'----------{p}ª PESSOA----------')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'F' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {maioridade_homem}.')
print(f'Ao todo são {totmulher20} mulheres com mais de 20 anos.')