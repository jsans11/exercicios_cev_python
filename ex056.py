velho = 0
novo = 0
i = 0
m = 0
homemv = ''
for p in range(1, 5):
    print(f'--- {p}ª PESSOA ---')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo (F ou M):')).upper()
    i = idade + i
    if sexo == 'M':
        if p == 1:
            velho = idade
            novo = idade
            homemv = nome
        else:
            if idade > velho:
                velho = idade
                homemv = nome
            elif idade < novo:
                novo = idade
    elif sexo == 'F' and idade < 20:
        m = m + 1
id = float(i / 4)
print(f'A média de idade do grupo é de {id} anos')
print(f'Tem {m} mulheres com menos de 20 anos.')
print(f'{homemv.capitalize()} é o homem mais velho com {velho} anos de idade.')
