def notas(*num, sit=False):
    '''

    :param num: As notas que serão analisadas.
    :param sit: Valor opicional da situação da turma. True ou False
    :return: Dicionário contendo informações sobre a turma.
    '''
    turma = dict()
    turma["Qtd notas"] = len(num)
    turma["Maior nota"] = max(num)
    turma["Menor nota"] = min(num)
    turma["Media"] = sum(num) / len(num)
    if sit:
        if turma["Media"] > 7:
            turma["Situação"] = 'Boa'
        elif turma["Media"] == 7:
            turma["Situação"] = 'Na média'
        elif 6.5 < turma["Media"] < 7:
            turma["Situação"] = 'Ruim'
    return turma


resp = notas(9.5, 10, 6.5, sit=True)
print(resp)
help(notas)