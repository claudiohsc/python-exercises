valores = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1
    valores.append(num)
    opcao = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('=-'*20)
print(f'Foram digitados {cont} números')
valores.sort(reverse=True)
print(f'Ordem decrescente da lista: {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado na lista. Posição {valores.index(5)}')
else:
    print('O valor 5 não foi digitado!')