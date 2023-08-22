expressao = list(input('Digite uma expressão: '))
if '(' or ')' in expressao:
    if expressao.count('(') == expressao.count(')'):
        print('A expresão digitada é válida!!')
    else:
        print('A expressão digitada é inválida!!')
else:
    print('A expresão digitada não contém parenteses ().')