c = 0
m = 0
for a in range(1, 8):
    b = int(input(f'Digite o ano de nascimento da {a}ª pessoa: '))
    if (2022 - b) >= 18:
        c = c + 1
    else:
        m = m + 1
print(f'Temos {c} pessoas que são maior de idade e {m} pessoas que são menor de idade')