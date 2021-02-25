ano = int(input('Digite um ano e direi se é bissexto ou não: '))
bi = ano / 4
resultado = bi.is_integer()

if resultado == True:
    print('O ano de {} é um ano bissexto.'.format(ano))
else:
    print('O ano de {} não é um ano bissexto.'.format(ano))