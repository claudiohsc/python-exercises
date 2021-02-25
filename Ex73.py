print('-='*20)
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Lista de times do Brasileirão: ', tabela)
print('-='*20)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-='*20)
print(f'Os 4 últimos são {tabela[20:15:-1]}') #OU [-4:]
print('-='*20)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('-='*20)
pos = tabela.index('Chapecoense')
print(f'O Chapecoense está na {pos + 1}ª posição.')
