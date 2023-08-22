listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 10.12,
            'transferidor', 3.98,
            'compasso', 9.99,
            'mochila', 119.99,
            'caneta', 1.00,
            'livro', 35.99)
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')