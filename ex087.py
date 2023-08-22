matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = colunatres = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da linha {linha},e da coluna {coluna}: '))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if coluna == 2:
            colunatres += matriz[linha][2]
print('-='*40)
print('A matriz solicitada é a seguinte: ')
print('-='*40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        #O método abaixo deixa o valor ocupando 5 casas e o acento circunflexo em cima serve para dizer que está no centro.
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*40)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da 3ª coluna é {colunatres}')
print(f'O maior valor da 2ª linha é {max(matriz[1])}')