# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
# Atribua valores fictícios e imprima cada valor individualmente.

""""
# Edvaldo
aluno = {
    'nome': 'Lucas',
    'idade': 25,
    'nota': 9.5
}
print(aluno['nome'])
print(aluno['idade'])
print(aluno['nota'])

print("----------------------")
"""
#Willian

aluno = {"nome": "Joao", 
        "idade": 20, 
        "nota": 8.5}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Nota:", aluno["nota"]) 


print("----------------------")

"""
#DAN
aluno = {
    "nome": "Danilo",
    "idade": 43,
    "nota": 8.5
}

print(aluno["nome"]) 
print(aluno["idade"]) 
print(aluno["nota"]) 


#Gabi 
aluno = {
    "nome": "Gabriela",
    "idade": 21,
    "nota": 9.5
}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Nota:", aluno["nota"])


# Alice 
aluno = {
    "nome": "Maria", 
    "idade": 16, 
    "nota": 8.2
}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Nota:", aluno["nota"])

# Mychelle
import os
os.system('cls' if os.name == 'nt' else 'clear')

aluno = {'nome': 'Ana', 'idade': 17, 'nota': 8.0}
print(f'Nome: {aluno['nome']}')
print(f'Idade: {aluno['idade']}')
print(f'Nota: {aluno['nota']}')


# Mirra

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


#Isabela

aluno = dict(zip(['nome', 'idade', 'nota'], ['isabela', 23, 5]))
print("\ndados do aluno:")
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")
"""