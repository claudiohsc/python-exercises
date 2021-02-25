soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o valor {c}:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número(s) par(es) e a soma entre eles é {soma}.')
