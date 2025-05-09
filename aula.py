import os
os.system('cls' if os.name == 'nt' else 'clear')
"""
4.Dado o dicionário:
frutas = {"maçã": 3, "banana": 5, "laranja": 2}
Escreva um código que:
- Peça ao usuário o nome de uma fruta.
- Verifique se a fruta está no dicionário.
- Se estiver, mostre quantas unidades têm.
Caso contrário, diga que a fruta não está disponível.
"""

aluno = {'nome':'Mario', 'notas':[7, 9, 5, 6], 'presencas':0.8}

chaves = list(aluno.keys())
valores = list(aluno.values())

print('Chaves: ', chaves)
print('Valores:', valores)