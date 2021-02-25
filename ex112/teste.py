from ex112.UtilidadesCeV import moeda
from ex112.UtilidadesCeV import dado

preço = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preço, 80, 35)