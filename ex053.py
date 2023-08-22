frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.split()
f = ''.join(p)
i = ''
for l in range(len(f) - 1, -1, -1):
    i = i + f[l]
if i == f:
    print(f'A frase {f} é igual ao seu inverso {i}, e por isso é um PALÍNDROMO')
else:
    print(f'A frase {f} é diferente do seu inverso {i}, então não é um palíndromo.')