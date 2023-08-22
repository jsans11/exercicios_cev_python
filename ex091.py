from random import randint
from time import sleep
from operator import itemgetter # esse itemgetter nos ajuda a ordenar o dicionário, o parâmetro 1 dentro serve pra dizer que queremos ordenar pelo valor, se fosse pela chave seria 0


maiorvalor = menorvalor = 0
jogo = dict()
jogo_ordenado = list()
for p in range(1, 5):
    jogo[f'Jogador {p}'] = randint(1, 6)
for j, v in jogo.items():
    print(f'{j} tirou {v} no dado.')
    sleep(1)
jogo_ordenado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for j, v in enumerate(jogo_ordenado):
    print(f'{j + 1}º lugar: {v[0]} com {v[1]} no dado.')
    sleep(1)

