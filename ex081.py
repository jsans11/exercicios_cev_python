valores = []
maior = menor = 0
while True:
    n = int(input('Digite um número: '))
    if n in valores:
        while True:
            n = int(input('Opa! Esse número já foi adicionado, por favor digite outro número: '))
            if n not in valores:
                valores.append(n)
                break
        a = str(input('Número adicionado. Você quer continuar ? [S/N] ')).strip().upper()
        if a != 'S' and a != 'N':
            while True:
                a = str(input('Resposta Errada. Você quer continuar ? [S/N] ')).strip().upper()
                if a == 'S' or a == 'N':
                    break
        if a == 'N':
            break
    else:
        valores.append(n)
        a = str(input('Número adicionado. Você quer continuar ? [S/N] ')).strip().upper()
        if a != 'S' and a != 'N':
            while True:
                a = str(input('Resposta Errada. Você quer continuar ? [S/N] ')).strip().upper()
                if a == 'S' or a == 'N':
                    break
        if a == 'N':
            break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} números')
print(f'A sua lista tem os seguintes valores: {valores}')
if 5 not in valores:
    print('O número 5 não está na lista')
else:
    print('O número 5 está na lista')