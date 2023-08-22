from utilidadescev import moeda
from utilidadescev import dado

#programa principal
p = dado.leiadinheiro('Digite o preço: R$ ')
ta = int(input('Digite a taxa de aumento(0 a 100): '))
td = int(input('Digite a taxa de desconto(0 a 100): '))
moeda.resumo(p, ta, td)
