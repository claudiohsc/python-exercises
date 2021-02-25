from ex115.lib.Interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExite(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #Opção de cadastrar uma nova  pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo...')
        break
    else:
        print('\033[31mErro! Opção inválida!\033[m')
    sleep(1)