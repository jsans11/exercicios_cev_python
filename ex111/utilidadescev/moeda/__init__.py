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

def resumo(p, taxa_aumento, taxa_desconto):
    print('-'*30)
    print('     RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}'.rjust(8))
    print(f'Dobro do preço: \t{moeda(dobro(p))}'.rjust(8))
    print(f'Metade do preço: \t{moeda(metade(p))}'.rjust(8))
    print(f'{taxa_aumento}% de aumento: \t{moeda(aumentar(p, taxa_aumento))}'.rjust(8))
    print(f'{taxa_desconto}% de desconto: \t{moeda(diminuir(p, taxa_desconto))}'.rjust(8))
    print('-' * 30)