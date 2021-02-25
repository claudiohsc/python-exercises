distancia = float(input('Digite a distância da viagem desejada em km: '))

if distancia<=200:
    print('O valor da viagem será de R${}'.format((distancia*0.50)))
else:
    print('O valor da viagem será de R${}'.format((distancia*0.45)))