from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for a in n:
    print(f'{a}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}, e o menor valor sorteado foi {min(n)}')
