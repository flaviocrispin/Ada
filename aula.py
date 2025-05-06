import os
os.system('cls' if os.name == 'nt' else 'clear')

lista1 = [1, 2, 3, 4, 5]
print (lista1)

aluno = {'nome':'Mario', 'notas':[7, 9, 5, 6], 'presencas':0.8, "endereço"}

print(f"Aluno: {aluno['nome']}") # Aluno: Mario
print(f"Notas: {aluno['notas'][0]}") # Notas: [7, 9, 5, 6]

notas = dict(Ana = "7", Brenda = 10, Carlos = 8, Diana = 9)
print(notas) # resultado: {'Ana': 7, 'Brenda': 10, 'Carlos': 8}

lista = [['Ana', 7], ['Brenda', 10], ['Carlos', 8]]
dicionario = dict(lista)
print(dicionario)

nomes = ['Ana', 'Brenda', 'Carlos', 'Diana']
notas = [7, 10, 8, 7]
endereco = ['Rua A', 'Rua B', 'Rua C', 'Rua D']
dicionario_notas = dict(zip(nomes, notas)
print(dicionario_notas)