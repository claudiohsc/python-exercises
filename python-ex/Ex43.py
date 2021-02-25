print('Vamos calcular seu IMC')

altura = float(input('Qual é a sua altura em metros?'))
peso = float(input('Qual é o seu peso?'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Atenção! Você está abaixo do peso.')
elif 18.5 < imc < 25:
    print('Seu peso está ideal.')
elif 25 < imc < 30:
    print('Você está em sobrepeso!')
elif 30 < imc < 40:
    print('Você está obeso! Cuidado!')
else:
    print('Você está com obesidade mórbida! Tenha cuidado e procure um médico.')

print('Tenha um bom dia!')