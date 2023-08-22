print('GERADOR DE PA!!!!')
print('-*'* 10)
p = int(input('Qual o primeiro termo da sua PA:'))
r = int(input('Qual a razão da sua PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} --> ', end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')