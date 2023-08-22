a = maisde = menosde = soma = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    a += 1
    valor = int(input('Preço do produto: R$ '))
    soma += valor
    if valor > 1000:
        maisde += 1
    if a == 1:
        barato = produto
        menosde = valor
    else:
        if valor < menosde:
            barato = produto
            menosde = valor
    cont = str(input('Você quer continuar ?(S/N): ')).strip().upper()[0]
    if cont == 'N':
        break
    if cont != 'S':
        cont = str(input('Comando Inválido. Você quer continuar ? (S/N): ')).strip().upper()[0]
print(f'O total gasto na compra foi de {soma} reais.')
print(f'Temos {maisde} produtos com valor acima de 1000 reais.')
print(f'{barato.capitalize()} é o produto mais barato e custa {menosde} reais.')
