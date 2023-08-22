valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {c}: ')))
print(f'A sua lista tem os seguintes valores: {valores}')
print(f'O maior valor é {max(valores)}, e está nas posições: ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}...', end= '')
print(f'\nO menor valor é {min(valores)}, e está nas posições: ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}...', end='')
