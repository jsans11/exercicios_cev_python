palavra = ('aprender', 'programar', 'linguagem',
           'python', 'gratis', 'estudar', 'praticar',
           'curso', 'trabalhar', 'mercado', 'futuro',
           'programador')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')