dados = dict()
pessoas = []
mulheres = []
acima = []
cont = somaid = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: '))
        if dados['sexo'] in 'FfmM':
            break
        else:
            print('Ops. Dados inválidos!!', end=' ')
    dados['idade'] = int(input('Idade: '))
    somaid += dados['idade']
    pessoas.append(dados)
    dados = dict()
    cont += 1
    while True:
        a = str(input('Quer continuar ?[S/N] '))
        if a not in 'sSnN':
            print('Ops. Dados inválidos!!', end=' ')
        else:
            break
    if a in 'nN':
        break
print(pessoas)
print(f'Foram adicionadas {cont} pessoas.')
print(f'A média de idade das pessoas adicionadas é de {somaid/cont} anos.')
for p in pessoas:
    if p['sexo'] in 'fF':
        mulheres.append(p['nome'])
    if p['idade'] > somaid/cont:
        acima.append(p['nome'])
print(f'As mulheres cadastradas foram {mulheres}.')
print(f'As pessoas acima da média são {acima}')