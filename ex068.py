from random import randint
vitorias = 0
while True:
    comp = randint(0, 10)
    n = int(input('Digite um número (Entre 0 e 10): '))
    if n > 10 or n < 0:
        print('Comando inválido!!')
    else:
        valor = str(input('Par ou Ímpar (P/I): ')).upper().strip()[0]
        final = comp + n
        if final % 2 == 0:
            jogo = 'P'
        else:
            jogo = 'I'
        if jogo == valor:
            print(f'Parabéns você venceu, você pediu {valor} e você jogou {n} e eu joguei {comp} e deu {final}.')
            vitorias =+ 1
        else:
            break
print(f'GAME OVER!! Você pediu {valor} e você jogou {n} e eu joguei {comp} e deu {final}.')
print(f'Você ganhou {vitorias} vezes.')