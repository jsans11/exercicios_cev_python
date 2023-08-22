def leiaint(msg):
    """
    --> Função que lê uma mensagem do tipo: Digite um número, e transforma essa frase através do input para vc digitar um número inteiro, e da uma mensagem de erro se você não digitar corretamente.
    :param msg: mensagem que será usada para ler o número.
    :return: valor do número lido
    """
    while True:
        try:
            num = int(input(msg))
            break
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número válido: \033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário parou a execução do programa \033[m')
            return '(Nenhum valor foi digitado pelo usuário)'
    return num

def linha(tamanho = 42):
    return '-' * tamanho


def cabeçalho(texto, tamanho = 42):
    print(linha())
    print(texto.center(tamanho))
    print(linha())


def menu(dados):
    for indice, opçao in enumerate(dados):
        print(f'\033[33m{indice + 1}\033[m - \033[34m{opçao}\033[m')
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc