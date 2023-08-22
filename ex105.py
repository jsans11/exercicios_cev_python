def notas(*valores, sit=False):
    """
    --> Função que exibe dicionário quantidade de notas adicionadas, maior nota, menor nota, média, e a situação(opcional)
    :param valores: recebe cada nota, podendo ser qualquer quantidade.
    :param sit: retorna a situação de acordo com a média.
    :return: retorna o dicionário adicionado.
    """
    dados = dict()
    c = soma = maior = menor = 0
    for nota in valores:
        soma += float(nota)
        if c == 0:
            menor = float(nota)
            maior = float(nota)
        else:
            if nota < menor:
                menor = float(nota)
            elif nota > maior:
                maior = float(nota)
        c += 1
    dados['Notas'] = c
    dados['Maior nota'] = maior
    dados['Menor nota'] = menor
    dados['Média'] = soma / c
    if sit:
        if dados['Média'] >= 7:
            dados['Situação'] = 'BOA'
        elif dados['Média'] >= 5:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados


resp = notas(5, 10, 10, sit=True)
print(resp)
help(notas)