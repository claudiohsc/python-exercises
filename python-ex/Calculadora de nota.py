nome = str(input('Qual é o seu nome? '))


print('Seja bem vindo(a), {}!'.format(nome))
print('----------------------------')
print('Vamos calcular sua média bimestral.')
av1 = float(input('Digite a primeira nota: '))
av2 = float(input('Digite a segunda nota: '))
an = float(input('Digite a nota do simulado: '))
media = (av1*0.4)+(av2*0.4)+(an*0.3)
print('A sua média bimestral è {}.'.format(media))

if media<=6.9:
    print('{}, se esforce mais, a sua média não está boa!'.format(nome))
else:
    print('{}, sua média está boa, parabéns!!'.format(nome))