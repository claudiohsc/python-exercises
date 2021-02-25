valores = list()
while True:
    num = int(input('Digite um número: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    opcao = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
