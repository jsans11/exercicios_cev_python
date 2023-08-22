def leiaint(msg):
    """
    --> Função que lê uma mensagem do tipo: Digite um número, e transforma essa frase através do input para vc digitar um número inteiro, e da uma mensagem de erro se você não digitar corretamente.
    :param msg: mensagem que será usada para ler o número.
    :return: valor do número lido
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!! Digite um número válido: \033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')