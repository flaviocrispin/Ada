"""
1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
Atribua valores fictícios e imprima cada valor individualmente.
"""
aluno = {
    'nome': ('emile', 'janete', 'janio', 'mario'),
    'idade': (25, 35, 44, 20),
    'nota': (8.5, 10, 5.5, 7)
}

for i, (nome, idade, nota) in enumerate(zip(aluno['nome'], aluno['idade'], aluno['nota']), start=1):
    print(f'aluno {i}')
    print(f'nome: {nome}')
    print(f'idade: {idade}')
    print(f'nota: {nota}')
    print()

"""
2. Dado o dicionário abaixo:
dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
Altere o valor da chave "idade" para 31 e adicione uma nova chave "email" com qualquer e-mail fictício. 
"""



"""
3. Escreva um código que pergunte ao usuário o nome de um produto e seu preço. 
Guarde essas informações em um dicionário e exiba-o no final.
"""