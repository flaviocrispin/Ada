import os
os.system('cls' if os.name == 'nt' else 'clear')

gerador_impares = (x for x in range(20) if x % 2 == 1)

#lista_impares = list(gerador_impares)

print(gerador_impares)