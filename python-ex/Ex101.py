def voto(ano):
    idade = 2020 - ano
    if 65 > idade >= 18:
        return f'Você tem {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Você tem {idade} anos: NÃO VOTA'
    elif 16 >= idade > 65 or 16 <= idade < 18:
        return f'Você tem {idade} anos: VOTO OPCIONAL'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))