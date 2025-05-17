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


# -----------------------------------------------------------------------------

# Módulo 01 - Aula 03 - Compreensão de Listas - 09/05/2025 

'''
6. Crie uma lista com os quadrados dos números de 0 a 9.
'''

# quadrados = [num**2 for num in range(10)]
# print(quadrados)



'''
7. A partir da lista 'nums = list(range(20))', crie uma nova lista apenas com os números pares.
'''

# nums = list(range(20))

# numeros_pares = [num for num in nums if num % 2 == 0]

# print(numeros_pares)



'''
8. Dada a lista palavras = ["python", "é", "legal"], crie uma nova lista com todas as palavras em maiúsculas.
'''

# palavras = ["python", "é", "legal"]

# maiusculo = [letra.upper() for letra in palavras]

# print(maiusculo)



'''
9. Você faz parte do time de dados da Globo, e está recebendo uma lista com os nomes dos programas e suas respectivas audiências em 
pontos de ibope, de uma semana. Seu objetivo é gerar um dicionário onde:

A chave seja o nome do programa.
O valor seja uma classificação textual baseada na audiência:
'Alta' se audiência ≥ 25
'Média' se audiência entre 15 e 24
'Baixa' se audiência < 15
'''

# audiencia = [
#   ("Jornal Nacional", 30),
#   ("Big Brother Brasil", 28),
#   ("Altas Horas", 18),
#   ("Sessão da Tarde", 12),
#   ("É de Casa", 14),
#   ("Fantástico", 26)
# ]

# dict_audiencia = {chave: ('Alta' if valor >= 25 else ('Média' if valor > 15 else 'Baixa')) for chave, valor in audiencia}

# print(dict_audiencia)


# -----------------------------------------------------------------------------

# Módulo 01 - Aula 04 - Parâmetros de Funções - 12/05/2025 

'''
10. Você trabalha com análise de audiência na Rede Globo e precisa retornar
os valores máximo e mínimo de uma lista de índices de audiência.

Implemente a função audiencia_extremos() e atribua os 
valores máximo e mínimo às variáveis maximo e minimo via desempacotamento. 
Imprima os dois valores, um por linha.
'''

# def audiencia_extremos(audiencias):
#   maior = max(audiencias)
#   menor = min(audiencias)
  
#   print(f'Maior: {maior}')
#   print(f'Menor: {menor}')

# lista_audiencias = [20, 14, 16, 28, 10, 30]
# audiencia_extremos(lista_audiencias)



'''
11. Padronização de nomes de arquivos do jornalismo com valor padrão upper=False. Implemente padroniza_titulo() e teste.
'''

# def padroniza_titulo(texto, upper=False):
#   if upper:
#     return texto.upper()
#   else:
#     return texto.lower()
  
# frase = 'Ada é top'
# print(padroniza_titulo(frase))
# print(padroniza_titulo(frase, upper=False))
# print(padroniza_titulo(frase, upper=True))



'''
12. Você trabalha com um sistema interno da Globo Educação. 
Precisa criar uma função que receba o nome de um aluno e retorne suas informações formatadas (curso, média e status).

Dicionário com dados de 4 alunos
alunos = {
  'Ana Clara': {'curso': 'Jornalismo', 'media': 8.5, 'status': 'Aprovada'},
  'Bruno Silva': {'curso': 'Engenharia de Dados', 'media': 6.8, 'status': 'Aprovado'},
  'Carlos Lima': {'curso': 'Publicidade', 'media': 4.2, 'status': 'Reprovado'},
  'Débora Souza': {'curso': 'Design Gráfico', 'media': 9.3, 'status': 'Aprovada'}
}
'''

alunos = {
  'Ana Clara': {'curso': 'Jornalismo', 'media': 8.5, 'status': 'Aprovada'},
  'Bruno Silva': {'curso': 'Engenharia de Dados', 'media': 6.8, 'status': 'Aprovado'},
  'Carlos Lima': {'curso': 'Publicidade', 'media': 4.2, 'status': 'Reprovado'},
  'Débora Souza': {'curso': 'Design Gráfico', 'media': 9.3, 'status': 'Aprovada'}
}

def informacoes(nome):
  if nome in alunos:
    return (f'Aluno: {nome}\nCurso: {alunos[nome]['curso']}\nMédia: {alunos[nome]['media']}\nStatus: {alunos[nome]['status']}')
  
  return 'Este aluno não está cadastro na base de dados.'
  
nome = input('Digite o nome do aluno: ')
print(informacoes(nome))