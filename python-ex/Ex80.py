valores = list()
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > valores[-1]:# o -1 mostra que é o ultimo elemento da lista
        valores.append(num)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break

            pos += 1
print(f'A lista gerada foi {valores}')


