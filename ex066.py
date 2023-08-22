n = total = cont = 0
while True:
    n = int(input('Digite um número: (999 Para parar): '))
    if n == 999:
        break
    cont += 1
    total += n
print(f'Você digitou {cont} números, e a soma entre eles é igual a {total}')
