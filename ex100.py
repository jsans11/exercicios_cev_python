from random import randint


def sorteia(valores):
    for i in range(1, 6):
        n = randint(1, 10)
        while n in valores:
            n = randint(1, 10)
        if n not in valores:
            valores.append(n)


def somapar(valores):
    soma = 0
    for i in range(0, len(valores)):
        if valores[i] % 2 == 0:
            soma += valores[i]
    print(f'A soma dos números pares de {valores} é igual {soma}')


valores = list()
sorteia(valores)
somapar(valores)



