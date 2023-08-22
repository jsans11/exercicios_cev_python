d = 0
n = int(input('Digite um número: '))
for a in range(1, n + 1):
    if n % a == 0:
        d = d + 1
        print('\033[34m', end=' ')
    else:
        print('\033[33m', end=' ')
    print(f'{a}', end=' ')
print('\033[m \n')
if d > 2:
    print(f'O número {n} \033[1;31mnão é primo\033[m, pois tem {d} divisores.')
else:
    print(f'O número {n} é \033[1;31mprimo\033[m, pois tem {d} divisores, ele mesmo e o número 1.')
