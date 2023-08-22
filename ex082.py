valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    continua = str(input('Quer adicionar mais algum valor [S/N]?: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if continua in 'Nn':
        break
valores.sort()
pares.sort()
impares.sort()
print(f'Os valores que você digitou foram: {valores}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
