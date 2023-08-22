from python_exercicios.ex115.lib.interface import *


def arquivo_existe(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {name} criado com sucesso!')
        cabeçalho('PESSOAS CADASTRADAS')


def ler_arquivo(name):
    try:
        a = open(name, 'rt')
    except:
        print(f'Erro ao ler o arquivo {name}!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()