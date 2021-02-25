from datetime import date

hj = date.today().year
totmaior = 0
totmenor = 0

for d in range(1, 8):
    data = int(input(f'Digite o ano de nascimento {d}:'))
    if hj - data >= 18:
        totmenor += 1
    else:
        totmaior += 1
print(f'Existem {totmaior} pessoas maiores e {totmenor} menores de idade.')

