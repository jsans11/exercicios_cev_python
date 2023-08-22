p = int(input('Qual o primeiro termo da sua PA:'))
r = int(input('Qual a razão da sua PA: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} -->', end='')
    termo = termo + r
    cont = cont + 1
print('FIM!!')