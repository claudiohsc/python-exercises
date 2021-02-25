n1 = int(input('Digite o primeiro termo termo de uma PA:'))
r = int(input('Digite a razão dessa PA:'))
t = n1 + ((10 - 1) * r)
for pa in range(n1, t + r, r):
    print('{}'.format(pa), end = ' ')