#recebe um dicionario com as notas e presenças de um aluno
aluno = {'nome':'Marios', 'notas':[7, 9, 5, 6], 'presencas':0.8}

#inserir um novo elemento no dicionario
aluno['idade'] = 20 #adiciona a idade do aluno
# mostra o resultado na tela
aluno['notas'].append(10) #adiciona a nota 10 na lista de notas do aluno

    # mostra o nome do aluno
print('Aluno:', aluno['nome'])
    # mostra a nota do aluno
print('Notas:', aluno['notas'])

print (f"os rotulos sao: {aluno.keys()}")
print (aluno.values())
print (aluno.items())
print (aluno['notas'][0])  #mostra a primeira nota do aluno
print (aluno['notas'][1])  #mostra a segunda nota do aluno
print (f"O tipo do rotulo notas é: {type(aluno['notas'])}") #mostra o tipo do dicionario

#ver o tamanho da lista
len(aluno['notas']) #mostra o tamanho da lista de notas
# o len vai funcionar para listas, dicionarios e strings
# não funciona para inteiros e floats
print('Quantidade de notas:', len(aluno['notas']))
print ('Quantidade de chaves:', len(aluno))

#uma lista com listas dentro
lista = [['Ana', 7], ['Brenda', 10], ['Carlos', 8]]
dicionario = dict(lista)
type(dicionario) #mostra o tipo do dicionario
print(dicionario)

#uma lista com os nomes e outra com as notas
nomes = ['Ana', 'Brenda', 'Carlos']
notas = [7, 10, 8]

#cria um dicionario com os nomes e notas com o metodo zip   
dicionario_notas = dict(zip(nomes, notas))
 #mostra o tipo do dicionario
print("---------aqui-----------")
print(dicionario_notas)
print("--------------------")

#cria um novo rotulo com a media e se o aluno foi aprovado ou reprovado
aluno['media'] = sum(aluno['notas'])/len(aluno['notas'])

aluno['aprovado'] = aluno['media'] >= 6.0 and aluno['presencas'] >= 0.7

#
for nome in nomes:
    aluno[nome] = dicionario_notas[nome]


print("--------------------")
print(aluno)

print("--------------------")
for valor in aluno:
    print(valor, '--->', aluno[valor])

dicionario = {'escola':"Ada", 'unidade':'Faria Lima'}


if 'cursos' in dicionario:
    dicionario['cursos'].append('Python')
else:
    dicionario['cursos'] = ['Python']

# Agora a chave já existe. 
# Portanto, será adicionado 'Data Science' à lista. 
if 'cursos' in dicionario:
    dicionario['cursos'].append('Data Science')
else:
    dicionario['cursos'] = ['Data Science']

print(dicionario)