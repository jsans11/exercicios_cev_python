homem = menina = maioridade = 0
print('CADASTRO')
print('-'*25)
while True:
    n = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo (F ou M): ')).upper().strip()[0]
    print('-'*25)
    if n >= 18:
        maioridade += 1
    if sexo == 'F' and n < 20:
        menina += 1
    if sexo == 'M':
        homem += 1
    alfa = str(input('Você quer cadastrar mais alguém (S ou N) ?')).upper().strip()[0]
    if alfa == 'N':
        break
    print('-'*25)
print(f'Você cadastrou {maioridade} pessoas maiores de idade')
print(f'Você cadastrou {homem} homens no total')
print(f'Você cadastrou {menina} mulheres com idade inferior a 20.')