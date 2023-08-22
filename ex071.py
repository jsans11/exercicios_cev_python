while True:
    valor = int(input('Qual valor você quer sacar: R$ '))
    not50 = valor // 50
    if valor % 50 != 0:
        r1 = valor % 50
        not20 = r1 // 20
        if r1 % 20 != 0:
            r2 = r1 % 20
            not10 = r2 // 10
            if r2 % 10 != 0:
                r3 = r2 % 10
                not1 = r3 // 1
    print(f'Você sacou {valor} no total, foram {not50} notas de 50, {not20} notas de 20, {not10} notas de 10, e {not1} notas de 1.')
    a = str(input('Você quer sacar mais algum valor? (S/N) ')).upper().strip()[0]
    if a == 'N':
        break
    if a != 'S':
        a = str(input('Valor Inválido!! Você quer sacar mais algum valor? (S/N) ')).upper().strip()[0]