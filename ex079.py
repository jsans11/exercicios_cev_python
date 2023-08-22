lista = []
while True:
    a = int(input('Digite um número inteiro: '))
    if a in lista:
        while True:
            a = int(input('Opa! Esse número já foi adicionado, por favor digite outro número: '))
            if a not in lista:
                lista.append(a)
                break
        b = str(input('Número adicionado. Você quer continuar ? [S/N] ')).strip().upper()
        if b != 'S' and b != 'N':
            while True:
                b = str(input('Resposta Errada. Você quer continuar ? [S/N] ')).strip().upper()
                if b == 'S' or b == 'N':
                    break
        if b == 'N':
            break
    else:
        lista.append(a)
        b = str(input('Número adicionado. Você quer continuar ? [S/N] ')).strip().upper()
        if b != 'S' and b != 'N':
            while True:
                b = str(input('Resposta Errada. Você quer continuar ? [S/N] ')).strip().upper()
                if b == 'S' or b == 'N':
                    break
        if b == 'N':
            break
lista.sort()
print(f'A sua lista tem os seguintes valores: {lista}')
