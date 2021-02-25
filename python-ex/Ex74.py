from random import randint
menor = maior = -1
nums = (randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in nums:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(nums)}')
print(f'O menor valor sorteado foi {min(nums)}')






