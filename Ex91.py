from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = list()
for k, v in jogadores.items():
    print(f'{k} tirou no dado ', end='')
    print(f'{v}')
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
