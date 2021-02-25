from time import sleep
from random import randint

lista = list()
numeros = lista[:]


def sorteio(lst):

    for i in range(0, 5):
        numeros.append(randint(1, 10))
    print('Foram sorteados os números: ', end='')
    for num in numeros:
        print(f'{num} ', end='')
        sleep(0.2)
    print('  PRONTO!')
    print()


def somaPar(nums):
    soma = 0
    for num in nums:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos valores pares da lista {nums} é: {soma}')


sorteio(lista)
somaPar(numeros)