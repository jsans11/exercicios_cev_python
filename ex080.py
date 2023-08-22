valores = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
    else:
        position = 0
        while position < len(valores):
            if n <= valores[position]:
                valores.insert(position, n)
                break
            position += 1
print('´', '-' * 50, '`')
print(f'Os valores digitados em ordem foram: {valores}')