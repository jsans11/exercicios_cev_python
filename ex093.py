dados = dict()
gols = []
total_gols = 0
dados['Nome'] = str(input('Nome: '))
partidas = int(input('Quantas partidas jogou? ')) + 1
for p in range(1, partidas):
    gols.append(int(input(f'Quantos gols na partida {p}: ')))
    total_gols += gols[p - 1]
dados['Gols'] = gols
dados['Soma de gols'] = total_gols
print('-='*45)
for i, j in dados.items():
    print(f'O campo {i} tem valor: {j}')
print('-='*45)
print(f'O jogador {dados["Nome"]} jogou {partidas - 1} partidas.')
for gol in range(0, len(gols)):
    print(f'Na partida {gol + 1}, fez {gols[gol]} gols.')
print(f'Um total de {total_gols} gols.')
