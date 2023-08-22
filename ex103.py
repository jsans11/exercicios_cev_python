def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gols')


#programa principal
nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite o número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)