cont = le = pe = 0
info = []
dados = []
pesados = []
leves = []
while True:
    info.append(str(input('Digite o nome: ')))
    info.append(float(input('Digite o peso da pessoa, em kg: ')))
    dados.append(info[:])
    info.clear()     # É necessário o clear para não criar um loop infinito com os dados que já estão na lista !!
    para = str(input('Deseja adicionar mais algum nome? [S/N]: '))
    cont += 1
    if para in 'nN':
        break
for dado in range(len(dados)):
    if dado == 0:
        le = dados[dado][1]
        pe = dados[dado][1]
        pesados.append(dados[dado])
        leves.append(dados[dado])
        #dados.pop(dado)
    else:
        if dados[dado][1] > pe:
            pesados.clear()
            pe = dados[dado][1]
            pesados.append(dados[dado])
            #dados.pop(dado)
        elif dados[dado][1] == pe:
            pesados.append(dados[dado])
            #dados.pop(dado)
        else:
            if dados[dado][1] < le:
                leves.clear()
                le = dados[dado][1]
                leves.append(dados[dado])
                #dados.pop(dado)
            elif dados[dado][1] == le:
                leves.append(dados[dado])
                #dados.pop(dado)
print(f'Foram adicionadas {cont} pessoa(s).')
if len(leves) > 1:
    print(f'Tivemos {len(leves)} pessoas entre as mais leves, pesando {le}kg. Sendo: ', end='')
    for p in leves:
        print(f'{p[0]}')
else:
    print(f'Tivemos apenas {leves[0]} sendo a pessoa mais leve pesando {le}kg.')
if len(pesados) > 1:
    print(f'Tivemos {len(pesados)} pessoas entre as mais pesadas, pesando {pe}kg. Sendo: ', end='')
    for p in pesados:
        print(f'{p[0]}')
else:
    print(f'Tivemos uma pessoa mais pesada que as outras, sendo: {pesados}')
