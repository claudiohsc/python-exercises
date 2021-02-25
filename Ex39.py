ano = int(input('Qual é o ano do seu nascimento?'))
idade = 2020 - ano
tempo = 18 - idade
tempo_ult = (-1) * (tempo)
if idade == 18:
    print('Você tem que se alistar agora.')
elif idade <= 17:
    print('Você ainda precisa se alistar.')
    print(f'Está faltando {tempo} ano(s) para o seu alistamento.')
else:
    print('Você já ultrapassou o tempo de alistamento.')
    print(f'Você ultrapassou {tempo_ult} ano(s).')