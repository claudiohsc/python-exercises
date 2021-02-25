from random import randint

num = int(randint(0, 10))
acertou = False
tentativas = 0

print('Pensei em um número entre 0 e 10, tente descobrí-lo!!')

while not acertou:
    num2 = int(input('Seu palpite entre 0 e 10: '))
    if num2 == num:
        acertou = True
        tentativas += 1
        print('Você acertou!!!')
        print(f'Você precisou de {tentativas} tentativa(s) para acertar.')
    elif num2 > num:
        print('Menos... digite outro.')
        acertou = False
        tentativas += 1
    else:
        print('Mais... digite outro.')
        acertou = False
        tentativas += 1

