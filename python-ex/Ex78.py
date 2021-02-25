valores = list()
menor = maior = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-'*20)

print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {menor} na posição ', end='')
for c, j in enumerate(valores):
    if j == menor:
        print(f'{c}...', end='')
print()

