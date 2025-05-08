"""
1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
Atribua valores fictícios e imprima cada valor individualmente.
"""

aluno = {
    "nome": "Maria", 
    "idade": 16, 
    "nota": 8.2
}

print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Nota:", aluno["nota"])


"""
2. Dado o dicionário abaixo:
dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
Altere o valor da chave "idade" para 31 e adicione uma nova chave "email" com qualquer e-mail fictício. 
"""

dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}

dados["idade"] = 31

dados["email"] = "carlos@mail.com"

print("[Dados Atualizados:]\n")
for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")


"""
3. Escreva um código que pergunte ao usuário o nome de um produto e seu preço. 
Guarde essas informações em um dicionário e exiba-o no final.
"""

produto = {}

produto["nome"] = input("Digite o nome do produto: ")
produto["preco"] = float(input("Digite o preço do produto: R$"))

print("\nProduto Cadastrado:")
for chave, valor in produto.items():
    if chave == "preco":
        print(f"{chave.capitalize()}: R${valor:.2f}")
    else:
        print(f"{chave.capitalize()}: {valor}")


"""
4.Dado o dicionário:
frutas = {"maçã": 3, "banana": 5, "laranja": 2}
Escreva um código que:
- Peça ao usuário o nome de uma fruta.
- Verifique se a fruta está no dicionário.
- Se estiver, mostre quantas unidades têm.
Caso contrário, diga que a fruta não está disponível.
"""

frutas = {"maçã": 3, "banana": 5, "laranja": 2}

fruta = input("Digite o nome da fruta: ").strip().lower()

if fruta in frutas:
    print(f"Temos {frutas[fruta]} unidades de {fruta}.")
else:
    print("Desculpe, essa fruta não está disponível.")


"""
5. Crie um dicionário chamado notas_alunos, onde a chave é o nome do aluno e o valor é a média final.
 Depois, mostre apenas os alunos com média maior ou igual a 7.
"""

notas_alunos = {
    "Luiz": 8.5,
    "Maria": 6.0,
    "João": 7.2,
    "Pedro": 5.5,
    "Julia": 9.0
}

print("Alunos com média maior ou igual a 7:\n")

for aluno, media in notas_alunos.items():
    if media >= 7:
        print(f"{aluno}: {media}")
