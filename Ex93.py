rendimento = {'Nome': str(input('Qual o nome do jogador? ')), 'Partidas': int(input('Número de partidas: ')),
              'Gols': []}

if rendimento['Partidas'] > 0:
    for n in range(0, rendimento['Partidas']):
        rendimento['Gols'].append(int(input(f'Número de gols na partida {n+1}: ')))
print(rendimento)
for k, v in rendimento.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'  O jogador {rendimento["Nome"]} jogou {rendimento["Partidas"]} partidas.')

for v in range(0, rendimento['Partidas']):
    print(f'    -Na partida {v+1}, fez {rendimento["Gols"][v]} gol(s).')
print(f'Total: {sum(rendimento["Gols"])} gols.')
