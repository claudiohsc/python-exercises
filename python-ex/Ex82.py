lista1 = list()
lista2 = list()
lista3 = list()
while True:
    num = int(input('Digite um número: '))
    lista1.append(num)
    opcao = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
for c, i in enumerate(lista1):
    if lista1[c] % 2 == 0:
        lista2.append(lista1[c])
    else:
        lista3.append(lista1[c])
print(f'Lista de números inseridos: {lista1}')
print(f'Lista de números pares: {lista2,}')
print(f'Lista de números ímpares: {lista3}')