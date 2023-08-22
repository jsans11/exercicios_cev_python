from random import randint
from time import sleep
a = 0
megasena = [0, 0, 0, 0, 0, 0]
jogos = int(input('Quantos jogos da MEGA SENA você quer? '))
for jogo in range(0, jogos):
    for n in range(0, 6):
        while a in megasena:
            a = randint(1, 60)
        if a not in megasena:
            megasena[n] = a
    megasena.sort()
    print(f'Aqui está o {jogo + 1}º jogo: ')
    sleep(1)
    print(f'{megasena}')