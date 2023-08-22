def aumentar(p=0, taxa=0, format=False):
    p_aumentado = p + (p * taxa / 100)
    return p_aumentado if format == False else moeda(p_aumentado)


def diminuir(p=0, taxa=0, format=False):
    p_diminuido = p - (p * taxa/100)
    return p_diminuido if format == False else moeda(p_diminuido)


def dobro(p=0, format=False):
    p_dobro = p * 2
    return p_dobro if format == False else moeda(p_dobro)


def metade(p=0, format=False):
    p_metade = p / 2
    return p_metade if format == False else moeda(p_metade)


def moeda(p=0, moeda = 'R$'):
    return f'{moeda}{p:>8.2f}'.replace('.',',')