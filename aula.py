import os
os.system('cls' if os.name == 'nt' else 'clear')
import csv

NOME_ARQUIVO_CSV = "Classificacao_2023.csv"

def csv_para_lista(nome_arquivo_csv):
    dados = []
    
    with open(NOME_ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        cabecalho = next(leitor_csv)  # Pega a primeira linha como cabeçalho
        
        for linha in leitor_csv:
            dados.append(linha)
    
    return cabecalho, dados
cabecalho, dados = csv_para_lista(NOME_ARQUIVO_CSV)

{time[0]: int(time[8]) for time in dados}
times_com_mais_de_2_gols = {time[0]: int(time[8]) for time in dados}
times_com_mais_de_2_gols = [(time, gols) for time, gols in times_com_mais_de_2_gols.items() if gols > 2]
print(times_com_mais_de_2_gols)