#AULA 10 - EXERCÍCIOS

#EXERCÍCIO 28

from random import randint
from time import sleep

nome = str(input('Qual é o seu nome? '))
print('Olá {}.'.format(nome))
print('\033[36m-=-'*20)
print('\033[32mVou pensar em um número de 0 a 5, e você tentará adivinhar. Boa sorte!!')
print('\033[36m-=-'*20)
num = int(input('\033[31mDigite o  seu  palpite: '))
print('\033[33mPROCESSANDO...')
sleep(2)
r = int(randint(0,5))
if num == r:
    print('\033[32mAcertou, Parabéns!!')
else:
    print(f'Errouu, mais sorte na próxima vez. Eu pensei no número {r} e não no {num}.')
