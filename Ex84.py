pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(dados) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoa(s).')
print(f'O maior peso foi de {mai} kgs!', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} kgs!', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()