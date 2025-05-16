import csv


def carregar_dados_de_arquivo_csv(nome_arquivo):
    dados_com_cabecalho = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            # Adiciona todas as linhas (incluindo o cabeçalho) à lista
            for linha in leitor_csv:
                dados_com_cabecalho.append(linha)
        
        if not dados_com_cabecalho:
            print(f"Aviso: O arquivo CSV '{nome_arquivo}' está vazio.")
            return None
        return dados_com_cabecalho
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado. Certifique-se de que ele está na mesma pasta do script.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV '{nome_arquivo}': {e}")
        return None