numeros = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um valor entre 0 e 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Erro. Digite um valor entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {numeros[n]}')