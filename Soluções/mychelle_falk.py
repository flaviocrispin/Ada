# Módulo 01 - Aula 01 - Dicionários - 05/05/2025 

'''
1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
Atribua valores fictícios e imprima cada valor individualmente.
'''

# aluno = {'nome': 'Ana', 'idade': 17, 'nota': 8.0}
# print(f'Nome: {aluno['nome']}')
# print(f'Idade: {aluno['idade']}')
# print(f'Nota: {aluno['nota']}')



'''
2. Dado o dicionário abaixo:

dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
Altere o valor da chave "idade" para 31 e adicione uma nova chave "email" com qualquer e-mail fictício.
'''

# dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
# dados['idade'] = 31
# dados['email'] = 'email@email.com'
# print(dados)



'''
3. Escreva um código que pergunte ao usuário o nome de um produto e seu preço. 
Guarde essas informações em um dicionário e exiba-o no final.
'''

# nome = input('Digite o nome do produto: ')
# preco = float(input('Digite o preço do produto: '))

# info_produto = {nome: preco}

# print(info_produto)



# -----------------------------------------------------------------------------




# Módulo 01 - Aula 02 - Dicionários - 07/05/2025 

'''
4.Dado o dicionário:
frutas = {"maçã": 3, "banana": 5, "laranja": 2}
Escreva um código que:
- Peça ao usuário o nome de uma fruta.
- Verifique se a fruta está no dicionário.
- Se estiver, mostre quantas unidades têm.
Caso contrário, diga que a fruta não está disponível.
'''

# frutas = {"maçã": 3, "banana": 5, "laranja": 2}

# fruta = input('Digite o nome da fruta: ')

# if fruta in frutas:
#   print(f'Há {frutas[fruta]} {fruta} disponíveis')
# else:
#   print(f'A fruta {fruta} não está disponível')



'''
5. Crie um dicionário chamado notas_alunos, onde a chave é o nome do aluno e o valor é a média final.
Depois, mostre apenas os alunos com média maior ou igual a 7.
'''

# notas_alunos = {"Ana": 6.0, "Brenda": 10.0, "Carla": 8.5, "Duda": 9.0}

# for chave in notas_alunos:
#   if notas_alunos[chave] >= 7:
#     print(f'{chave}: {notas_alunos[chave]}')
