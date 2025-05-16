import os
os.system('cls' if os.name == 'nt' else 'clear')

tupla_str = (1, 3, 5)
tupla_float = tuple(map(str, tupla_str)) # função: float; coleção: tupla_str
print(tupla_str, tupla_float)