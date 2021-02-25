nome = str(input('Digite seu nome: '))
speed = int(input('Digite a velocidade do seu carro em km/h: '))
print('Atenção! Velocidade limite é 80 km/h.')
ult = int((speed-80))
multa = float((7*ult))
if speed<=80:
    print('Está tudo ok. Dirija com segurança.')
else:
    print('Você ultrapassou o limite de velocidade!!')
    print('O valor da multa é de R${}'.format(multa))

