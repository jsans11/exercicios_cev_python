def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade >= 60 or 16 <= idade < 18:
        print(f'VOTO OPCIONAL!! Pois a idade é de {idade} anos.')
    elif idade >= 18:
        print(f'VOTO OBRIGATÓRIO!! Pois a idade é de {idade} anos.')
    else:
        print(f'VOTO NEGADO!! Pois a idade é de {idade} anos.')


# programa principal
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
voto(2010)
voto(1997)
voto(1943)
voto(2007)
voto(2005)