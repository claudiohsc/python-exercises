from random import randint
from time import sleep
print('-=-'*20)
print('                 \033[32mPEDRA, PAPEL E TESOURA.\033[m')
print('-=-'*20)
#Apresentação do jogo.
print('Pedra = 1; Papel = 2; Tesoura = 3')
sleep(1)
pc = randint(1, 3)
print('Pedra')
sleep(0.6)
print('Papel')
sleep(0.6)
print('Tesoooura')
sleep(1)
escolha = int(input('Sua escolha:'))
#Escolha do pc.
if pc == 1:
    print('Eu escolhi Pedra.')
elif pc == 2:
    print('Eu escolhi Papel.')
elif pc == 3:
    print('Eu escolhi Tesoura.')
#Definindo quem ganhou.
if pc == escolha:
    print('Empate.')
elif (pc == 1 and escolha == 2) or (pc == 2 and escolha == 3) or (pc == 3 and escolha == 1):
    print('Parabéns, você GANHOU!')
else:
    print('Que pena, você PERDEU!')