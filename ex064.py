cont = -1
total = 0
n = 0
while n != 999:
    cont = cont + 1
    total = n + total
    n = int(input('Digite um número inteiro (999 para sair): '))
print(f'Você digitou {cont} números e a soma desses números é igual a {total}')
