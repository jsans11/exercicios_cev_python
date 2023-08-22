import moeda


#programa principal
p = float(input('Digite o preço: '))
t = int(input('Digite a taxa (0 a 100): '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentar em {t}%, temos: {moeda.aumentar(p, t, True)}')
print(f'Diminuir em {t}%, temos: {moeda.diminuir(p, t, True)}')