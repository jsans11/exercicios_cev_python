import moeda


#programa principal
p = float(input('Digite o preço: R$ '))
t = int(input('Digite a taxa (0 a 100): '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentar em {t}%, temos: R$ {moeda.aumentar(p, t)}')
print(f'Diminuir em {t}%, temos: R$ {moeda.diminuir(p, t)}')