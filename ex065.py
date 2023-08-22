maiorvalor = menorvalor = valor = cont = total = a = 0
while a != 'N':
    cont = cont + 1
    n = int(input('Digite um número inteiro: '))
    a = str(input('Você quer continuar ? (S/N): ')).upper().strip()
    if a != 'S' and a != 'N':
        str(input('Opção Inválida!! Você quer continuar? (S/N): ')).upper().strip()
    valor = n + valor
    if cont == 1:
        maiorvalor = n
        menorvalor = n
    else:
        if n > maiorvalor:
            maiorvalor = n
        elif n < menorvalor:
            menorvalor = n
v = float(valor/cont)
print(f'A média entre todos os números calculados é {v:.2f}')
print(f'{maiorvalor} é o maior valor, e {menorvalor} é o menor valor.')
