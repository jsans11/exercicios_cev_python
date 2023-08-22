import moeda


#programa principal
p = float(input('Digite o preço: R$ '))
ta = int(input('Digite a taxa de aumento(0 a 100): '))
td = int(input('Digite a taxa de desconto(0 a 100): '))
moeda.resumo(p, ta, td)
