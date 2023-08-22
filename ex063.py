n = int(input('Digite quantos termos da Sequência de Fibonacci você quer ver:'))
termo = 1
primeiro = 0
segundo = 1
proximo = 0
while termo <= n:
    if termo == 2:
        print('1 --> ', end='')
        termo = termo + 1
    else:
        print(f'{proximo} --> ', end='')
        proximo = primeiro + segundo
        primeiro = segundo
        segundo = proximo
        termo = termo + 1
print('FIM!')