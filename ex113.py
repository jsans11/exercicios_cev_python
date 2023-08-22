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


def leiafloat(msg):
    """
    --> Função que lê uma mensagem do tipo: Digite um número, e transforma essa frase através do input para vc digitar um número real, e da uma mensagem de erro se você não digitar corretamente.
    :param msg: mensagem que será usada para ler o número.
    :return: valor do número lido
    """
    while True:
        try:
            num = float(input(msg))
            break
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número válido: \033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário parou a execução do programa \033[m')
            return '(Nenhum valor foi digitado pelo usuário)'
    return num


# Programa principal
n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
print()
n = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n}')