def ficha(jogador='<desconhecido>', gols=0):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

#Programa Principal
nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)
