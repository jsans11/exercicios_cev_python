s = 0
d = 0
for c in range(1, 7):
    a = int(input(f'Digite o {c}º número: '))
    if a % 2 == 0:
        s = s + a
        d = d + 1
print(f'A soma dos {d} números pares é: {s}')
print('FIM!!')
