r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if (r1-r2) < r3 < (r1+r2) and (r1-r3) <r2 < (r1+r3) or (r2-r3) < r1 < (r2+r3):
    print('As semirretas podem formar um triângulo.')
else:
    print('As semirretas não podem formar um triângulo.')