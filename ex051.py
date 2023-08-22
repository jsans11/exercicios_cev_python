p = int(input('Digite o 1º Termo da PA: '))
raz = int(input('Digite a razão da PA: '))
decimo = p + (10 - 1)* raz
for c in range (p, decimo + 1, raz):
    print(f'{c}', end = ' --> ')
print('FIM!!')