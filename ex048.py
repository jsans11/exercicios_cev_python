a = 0
c = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        c = c + 1
        a = a + num
print(f'A soma dos {c} números ÍMPARES múltiplos de 3 entre 1 e 500 é {a}')
print('FIM!!')