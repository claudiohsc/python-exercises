while True:
    n = int(input('Quer ver a tabuada de qual valor? [-n para parar] '))
    if n < 0:
        break
    print('-'*40)
    for m in range(0,11):
        print(f'{n} x {m} = {n*m}')
    print('-'*40)
print('PROGRAMA DA TABUADA ENCERRADO')
print('Volte Sempre!!!')