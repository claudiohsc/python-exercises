dezoito = homens = mulher = 0
while True:
    print('-' * 21)
    print('CADASTRE UMA PESSOA')
    print('-' * 21)
    idade = int(input('Idade: '))
    if idade >= 18:
        dezoito += 1
    sexo = escolha = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-' * 21)
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if escolha == 'N':
        print('====FIM DO PROGRAMA====')
        print(f'Total de pessoas com mais de 18 anos: {dezoito}')
        print(f'Ao todo temos {homens} homens cadastrados.')
        print(f'E temos {mulher} mulher(es) com menos de 20 anos.')
        break
