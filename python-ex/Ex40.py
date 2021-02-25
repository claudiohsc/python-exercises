nota1 = float(input('Qual foi sua primeira nota?'))
nota2 = float(input('Qual foi a sua segunda nota?'))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print('Você está REPROVADO.')
elif media == 6.0 or media <= 6.9:
    print('Você está de RECUPERAÇÃO.')
else:
    print('Parabéns!!! Você está APROVADO!')