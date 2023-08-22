jogadores = list()
while True:
    dados = dict()
    gols = []
    total_gols = 0
    dados['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {p}: ')))
        total_gols += gols[p - 1]
    dados['Gols'] = gols
    dados['Soma de gols'] = total_gols
    jogadores.append(dados)
    while True:
        a = str(input('Quer adicionar mais alguém ? [S/N] '))
        if a not in 'sSnN':
            print('Ops. Dados inválidos!!', end=' ')
        else:
            break
    if a in 'nN':
        break
print('-'*45)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*45)
for indice in range(0, len(jogadores)):
    print(f'{indice:<4}', f'{jogadores[indice]["Nome"]:<15}', f'{jogadores[indice]["Gols"]}'.ljust(15), f'{jogadores[indice]["Soma de gols"]:<15}')
while True:
    print('-' * 45)
    c = int(input('Digite o número do jogador que você deseja ver [Digite 999 para finalizar]: '))
    if c == 999:
        break
    elif c < 0 or c >= len(jogadores):
        print('Ops. Dados inválidos!!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {jogadores[c]["Nome"]}:')
        for gol in jogadores[c]['Gols']:
            print(f'No jogo {p} fez {jogadores[c]["Gols"][gol]}')
print('-'*45)
print('PROGRAMA FINALIZADO')
