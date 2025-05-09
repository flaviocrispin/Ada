import os
os.system('cls' if os.name == 'nt' else 'clear')


aluno['media'] = sum(aluno['notas'])/len(aluno['notas'])
aluno['aprovado'] = aluno['media'] >= 6.0 and aluno['presencas'] >= 0.7