dados = dict()
dados['nome'] = str(input('Nome da(o) aluna(o): '))
dados['media'] = float(input('Digite a média de notas: '))
if dados['media'] < 4:
    dados['situação'] = 'Reprovada(o)'
elif 4 <= dados['media'] < 6:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Aprovada(o)'
print(f'A(O) aluna(o) {dados["nome"]} teve média {dados["media"]} e tem a situação: {dados["situação"]}.')