def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número o qual quer se calcular o fatorial
    :param show: se True mostra o cálculo detalhado do cálculo (opcional)
    :return: o valor do fatorial
    """
    print('-'*30)
    print('CÁLCULO DE FATORIAL')
    number = num
    fat = 1
    while num > 0:
        fat = fat * num
        num -= 1
    if number < 0:
        print('Não existe fatorial de número negativo.')
    if show and number > 1:
        for n in range(number, 0, -1):
            if n > 1:
                print(f'{n} x ', end='')
            else:
                print(f'{n} == {fat}')
    if not show:
        print(fat)


a = int(input('Digite um número inteiro para o cálculo de seu fatorial: '))
fatorial(a, True)
help(fatorial)