import moeda


#programa principal
p = float(input('Digite o preço: '))
t = int(input('Digite a taxa (0 a 100): '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar em {t}%, temos: {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Diminuir em {t}%, temos: {moeda.moeda(moeda.diminuir(p, t))}')