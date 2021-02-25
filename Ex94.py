pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: ').strip())
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite um sexo válido. [M/F]')

    pessoa['idade'] = int(int(input('Digite a idade: ')))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input("Quer continuar? [S/N]: ")).strip().upper()
        if r in 'SN':
            break
        print('ERRO! Digite apenas [S/N]')
    if r == 'N':
        break
#Análise dos dados:
print('-='*30)
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('')
print(f'Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print('')
print('ENCERRADO')
