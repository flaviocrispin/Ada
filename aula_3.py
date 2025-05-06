import os
os.system('cls' if os.name == 'nt' else 'clear')

#criar variável em branco
quadrados = []

#fazer um loop de 1 a 10 e adicionar o quadrado de cada número na variável "quadrados"
for x in range(1, 11):
    quadrados.append(x**2)

print(quadrados)
print(x)

quadrados_compreensao = [num**2 for num in range(1, 11)]

print(quadrados_compreensao)

numeros = [1, 9, 4, 7, 6, 2]

metades = [n/2 for n in numeros]

print(metades)

metades_pares = [n/2 for n in numeros if n % 2 == 0]
print(metades_pares)


metades_tipo = [n//2 if n % 2 == 0 else n/2 for n in numeros]

print(metades_tipo)

nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
sobrenomes = ['Silva', 'Oliveira']

combinacoes = [nome + ' ' + sobrenome for nome in nomes for sobrenome in sobrenomes]
print(combinacoes)

numeros = [1, 2, 3, 4, 5]
quadrados = [n**2 for n in numeros]

combinacoes = sorted([num + quadrado for num in numeros for quadrado in quadrados])
print (f"Os numeros são: {numeros}")   
print (f"Os quadrados são: {quadrados}")
print (f"As combinações são: {combinacoes}")

[print(f"{num} + {quadrado} = {num + quadrado}") for num in numeros for quadrado in quadrados]

# times = ['Atlético Python', 'JavaScript United', 'C Seniors', 'Javeiros do Norte']
# entradas = ['V', 'E', 'D']
# tabela = [[int(input(f'Digite a quantidade de {tipo} do time {time}: ')) for tipo in entradas] for time in times]
# print(tabela)

alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

cadastro = {alunos[i]:medias[i] for i in range(len(alunos))}

print(cadastro)

alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

#percorre a lista de alunos e medias e especifica quem sera a chave e quem sera o valor usando o zip
cadastro = {aluno:media for aluno, media in zip(alunos, medias)}

print(cadastro)
type (cadastro)

gerador_quadrados = (x**2 for x in range(10))

for quadrado in gerador_quadrados:
    print(quadrado)

lista_quadrados = list(gerador_quadrados)
print(lista_quadrados) # imprime uma lista vazia

# gerador = (x for x in range(5))
# print (gerador)
# print(next(gerador))
# print(next(gerador))
# print(next(gerador))
# print(next(gerador))
# print(next(gerador))
# print(next(gerador))
 # imprime o gerador

# def gerador_de_sequencia(limite:int):
#     contador = 0
#     while contador < limite:
#         yield contador
#     contador += 1

# iterador_sequencia = gerador_de_sequencia(10)

# for x in iterador_sequencia:
#     print(x)