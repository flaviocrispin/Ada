import os
os.system('cls' if os.name == 'nt' else 'clear')

import csv

NOME_ARQUIVO_CSV = "Classificacao_2023.csv"

def csv_para_lista(nome_arquivo_csv):
    """
    Lê um arquivo CSV e retorna seus dados como uma lista.
    
    Args:
        nome_arquivo_csv (str): Caminho para o arquivo CSV a ser lido
    
    Retorno:
        tupla: (cabecalho, dados) onde:
            - cabecalho é uma lista com os nomes das colunas
            - dados é uma lista de listas com os dados do CSV
    """
    dados = []
    
    with open(NOME_ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        cabecalho = next(leitor_csv)  # Pega a primeira linha como cabeçalho
        
        for linha in leitor_csv:
            dados.append(linha)
    
    return cabecalho, dados


cabecalho, dados = csv_para_lista('seu_arquivo.csv')
print ("Cabeçalho:", cabecalho)
print("\nPrimeiras 5 linhas:")
for i, linha in enumerate(dados, 1):
    if i > 2:
        break
    print(f"Linha {i}: {linha}")

#Transforma (cabecalho, dados) em lista de dicionários
def lista_para_dicionarios(cabecalho, dados):
    """
    Converte dados estruturados em lista para lista de dicionários.
    
    Args:
        cabecalho (list): Nomes das colunas.
        dados (list): Lista de listas contendo os dados.
    
    Returns:
        list: Lista de dicionários (chave=coluna, valor=dado).
    """
    lista_dict = []
    
    for linha in dados:
        linha_dict = {}
        for coluna, valor in zip(cabecalho, linha):
            linha_dict[coluna] = valor
        lista_dict.append(linha_dict)
    
    return lista_dict

dados_dict = lista_para_dicionarios(cabecalho, dados)
print("\nDados como dicionários (5 primeiras linhas):")
for i, linha in enumerate(dados_dict[:5], 1):
    print(f"Linha {i}: {linha}")

def converter_para_int(dados: List[Dict], chaves: List[str]) -> List[Dict]:
    """
    Converte valores especificados para inteiro
    Args:
        dados: Lista de dicionários com os dados
        chaves: Lista de chaves para converter
    Returns:
        Lista de dicionários com valores convertidos
    """
    for registro in dados:
        for chave in chaves:
            if chave in registro and registro[chave].isdigit():
                registro[chave] = int(registro[chave])
    return dados

def padronizar_time(dados: List[Dict], chave: str) -> List[Dict]:
    """
    Padroniza strings para minúsculas
    Args:
        dados: Lista de dicionários
        chave: Chave contendo o nome do time
    Returns:
        Lista com os valores padronizados
    """
    for registro in dados:
        if chave in registro:
            registro[chave] = registro[chave].lower()
    return dados

def tratamento_limpeza(dados: List[Dict]) -> List[Dict]:
    """
    Executa todas as operações de limpeza e tratamento
    Args:
        dados: Lista de dicionários brutos
    Returns:
        Nova lista de dicionários tratados
    """
    # Criamos uma cópia profunda para não alterar o original
    dados_tratados = [dict(registro) for registro in dados]
    
    # Aplicamos as transformações
    dados_tratados = converter_para_int(dados_tratados, ["Rodada", "Pontos"])
    dados_tratados = padronizar_time(dados_tratados, "time")
    
    return dados_tratados

# Exemplo de uso
if __name__ == "__main__":
    # 2. Aplicar tratamento completo
    dados_tratados = tratamento_limpeza(dados_dict)
    
    # 3. Mostrar resultados
    print("\nDados brutos (amostra):")
    for i, linha in enumerate(dados_dict[:3], 1):
        print(f"Registro {i}: {linha}")
    
    print("\nDados tratados (amostra):")
    for i, linha in enumerate(dados_tratados[:3], 1):
        print(f"Registro {i}: {linha}")