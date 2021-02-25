nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num1 = -1

while True:
    num1 = int(input('Digite um número entre 0 e 20: '))
    if 0<= num1 <= 20:
        print(f'Você digitou o número {nums[num1]}')
    v = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if v == 'S':
        num1 = -1
    else:
        break
print('FIM')