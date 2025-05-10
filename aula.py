import os
os.system('cls' if os.name == 'nt' else 'clear')

5. Você faz parte do time de dados da Globo, e está recebendo uma 
lista com os nomes dos programas e suas respectivas audiências em pontos de ibope, de uma semana.
Seu objetivo é gerar um dicionário onde:

A chave seja o nome do programa.
O valor seja uma classificação textual baseada na audiência:
'Alta' se audiência ≥ 25
'Média' se audiência entre 15 e 24
'Baixa' se audiência < 15

audiencia = [
    ("Jornal Nacional", 30),
    ("Big Brother Brasil", 28),
    ("Altas Horas", 18),
    ("Sessão da Tarde", 12),
    ("É de Casa", 14),
    ("Fantástico", 26)
]