a = resp = True
cont = 0
dados = [[], [], [], [], []]
while a == True:
    dados[0].append(str(input('Digite o nome da(o) aluna(o): ')))
    dados[1].append(float(input('Nota da P1: ')))
    dados[2].append(float(input('Nota da P2: ')))
    dados[4].append(cont)
    cont += 1
    b = str(input('Quer cadastrar mais alguém? [S/N] '))
    if b in 'Nn':
        a = False
for alunx in dados[4]:
    nota_um = dados[1][alunx]
    nota_dois = dados[2][alunx]
    dados[3].append((nota_um + nota_dois) / 2)
print('-'*10,'BOLETIM','-'*10)
print('-'*4,'NOME','-'*4,'MÉDIA')
for alunx in dados[4]:
    print(f'{dados[4][alunx]}','-'*4,f'{dados[0][alunx]}','-'*4,f'{dados[3][alunx]}')
while resp == True:
    c = int(input('Digite o número da(o) aluna(o) que você deseja ver [Digite 999 para finalizar]: '))
    if c in dados[4]:
        print(f'Nome: {dados[0][c]}, Notas:[{dados[1][c]}, {dados[2][c]}]')
    else:
        resp = False
print('-'*30)
print('PROGRAMA FINALIZADO')
