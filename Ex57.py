v = 1
sexo = str(input('Digite o seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite o seu sexo [M/F]: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso.')