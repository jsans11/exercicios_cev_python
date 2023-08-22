while True:
    n = int(input('Digite um número que você queira ver a tabuada: '))
    if n < 0:
        break
    for a in range (1,11):
        print(f'{n} x {a} = {n * a}')
print('FIM')