"""
Descompacta todos os arquivos .zip da pasta, cada um em uma subpasta com o nome do arquivo.
"""

import os
import zipfile

PASTA_ZIPS = "E:\\"  # Altere para sua pasta

def descompactar_todos(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".zip")]
    for arquivo in arquivos:
        caminho_zip = os.path.join(pasta, arquivo)
        pasta_destino = os.path.join(pasta, os.path.splitext(arquivo)[0])
        os.makedirs(pasta_destino, exist_ok=True)
        print(f"Descompactando {arquivo} em {pasta_destino}")
        try:
            with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
        except Exception as e:
            print(f"Erro ao descompactar {arquivo}: {e}")

if __name__ == "__main__":
    descompactar_todos(PASTA_ZIPS)
