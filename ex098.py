from time import sleep


def contador(inicio, fim, passo):
    print('-='*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11, 1):
        print(f'{i} ', end='')
        sleep(0.5)
    print()
    print('-=' * 30)
    print('Contagem de 10 até 0 de 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i} ', end='')
        sleep(0.5)
    print()
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim and passo > 0:
        passo = - passo
        fim -= 1
    elif inicio > fim and passo == 0:
        passo = - 1
        inicio -= 1
    elif inicio > fim:
        fim -= 1
    elif passo == 0:
        passo = 1
        fim += 1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
        sleep(0.5)
    print()
    print('-=' * 30)
    print('PROGRAMA FINALIZADO')


contador(2,15,0)
contador(40,3,-6)