time = list()
partidas = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Qual o nome do jogador? '))
    tot = int(input(f'Número de partidas do {jogador["Nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Número de gols na partida {c+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break

#Analise dos dados
print('-'*30)
#cabeçalho
print('cod', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
#começo da lista
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe o jogador com código {busca}')
    else:
        print(f'--  LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')