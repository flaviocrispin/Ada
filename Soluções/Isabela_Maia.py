#solucao exercicio da aula 1 com valor estatico usando for
aluno = dict(zip(['nome', 'idade', 'nota'], ['isabela', 23, 5]))
print("\ndados do aluno:")
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")