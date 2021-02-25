preco = float(input('Digite o preço do produto: R$'))
from time import sleep
sleep(0.5)
print('''Condições de pagamento: 
[ 1 ] Á vista em dinheiro/Cheque: 10% de desconto;
[ 2 ] Á vista no cartão: 5% de desconto;
[ 3 ] Em até 2x no cartão; 
[ 4 ] 3x ou mais no cartão: 20% de juros.''')

cond = int(input('Qual a condição de pagamento: 1, 2, 3 ou 4?'))


if cond == 1:
    total = preco - (preco * 10/100)
elif cond == 2:
    total = preco - (preco * 5/100)
elif cond == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f}')
elif cond == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Em quantas parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela}')
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')