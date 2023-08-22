matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da linha {linha},e da coluna {coluna}: '))
        # Utilizando esse método abaixo não deu certo, acredito que o método de insert ou append não funcione bem dessa forma
        # num = int(input(f'Digite o valor [{linha},{coluna}]: '))
        # matriz.insert([linha][coluna], num)
print('A matriz solicitada é a seguinte: ')
for linha in range(0, 3):
    for coluna in range(0, 3):
        #O método abaixo deixa o valor ocupando 5 casas e o acento circunflexo em cima serve para dizer que está no centro.
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
