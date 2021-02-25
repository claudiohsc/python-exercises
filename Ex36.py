print('Seja bem vindo(a).')

valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar a casa?'))

meses = anos * 12
valor_parcelas = valor_casa / meses
limite = salario * (30.001/100)

if valor_parcelas > limite:
    print('Seu pedido de empréstimo foi negado, pois excede o limite de 30% do seu salário.')
else:
    print(f'O valor da parcela da sua casa será de R${valor_parcelas}.')
print('Espero ter ajudado!')
print('Tenha um bom dia!!')