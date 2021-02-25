from random import randint
from time import sleep

palpites = []
print('-='*15)
print('     JOGOS DA MEGA SENA     ')
print('-='*15)
n = int(input('Quantos jogos você quer gerar? '))
print(f'Gerando {n} jogo(s)...')
print('-='*15)
sleep(1)
for i in range(0, n):
    while True:
        chute = randint(1, 60)
        if chute not in palpites:
            palpites.append(chute)
        if len(palpites) == 6:
            break
    print(f'Jogo {i +1}: {palpites}')
    palpites.clear()
    sleep(1)
print('-='*5, "Boa sorte!!!", '-='*5)