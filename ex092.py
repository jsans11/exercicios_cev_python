from time import sleep
from datetime import datetime
info = {}
info['Nome'] = str(input('Nome: '))
info['Idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
carteira = int(input('Nº da CTPS (0 se não houver): '))
if carteira != 0:
    info['Ano de contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = float(input('Digite o salário: '))
    info['Aposentadoria'] = 'com ' + str(info['Ano de contratação'] + 30 - datetime.now().year + info['Idade']) + ' anos.'
print('-=' * 45)
for i, j in info.items():
     print(f'{i} é {j}')
     sleep(1)
print('-=' * 45)