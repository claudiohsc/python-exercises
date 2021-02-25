from datetime import date

dados = {'nome': str(input('Digite o seu nome: ')),
       'idade': int(input('Digite seu ano de nascimento: ')),
        'ctps': int(input('Carteira de Trabalho [0 não tem]: '))
}
data = date.today()
ano = data.year
dados['idade'] = ano - dados['idade']

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Qual o ano de contratação? '))
    dados['salario'] = float(input('Digite o seu salário: '))
    dados['aposentadoria'] = 65 - dados['idade']
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'    -{k} tem o valor {v}.')