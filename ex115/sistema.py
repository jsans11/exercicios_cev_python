from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemviedo.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

cabeçalho('MENU PRINCIPAL')
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas','Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo !
        ler_arquivo(arquivo)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        cabeçalho('Opção 3: Saindo do sistema... Até breve!')
        break
    else:
        print('\033[0;31mERRO!! Digite uma opção válida!! \033[m')
        print(linha())
    sleep(2)