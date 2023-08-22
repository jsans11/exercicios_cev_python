def aumentar(p, taxa):
    p_aumentado = p + (p * taxa / 100)
    return p_aumentado


def diminuir(p, taxa):
    p_diminuido = p - (p * taxa/100)
    return p_diminuido


def dobro(p):
    p_dobro = p * 2
    return p_dobro


def metade(p):
    p_metade = p / 2
    return p_metade