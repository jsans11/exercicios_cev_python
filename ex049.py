from time import sleep
n = int(input('Digite um número: '))
for a in range (1, 11):
    b = n * a
    print(f'{n} x {a} = {b}')
    sleep(0.5)
print('FIM!!')
