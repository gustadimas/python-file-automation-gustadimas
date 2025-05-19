"""
Procura e lista arquivos duplicados em uma pasta (por conteúdo, usando hash MD5).
"""

import os
import hashlib

PASTA_BUSCA = "E:\\"  # Altere para sua pasta

def hash_arquivo(caminho):
    hash_md5 = hashlib.md5()
    with open(caminho, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def encontrar_duplicados(pasta):
    hashes = {}
    duplicados = []
    for root, dirs, files in os.walk(pasta):
        for nome_arquivo in files:
            caminho = os.path.join(root, nome_arquivo)
            try:
                hash_val = hash_arquivo(caminho)
                if hash_val in hashes:
                    duplicados.append((caminho, hashes[hash_val]))
                else:
                    hashes[hash_val] = caminho
            except Exception as e:
                print(f"Erro ao processar {caminho}: {e}")
    if duplicados:
        print("\nArquivos duplicados encontrados:")
        for dup, original in duplicados:
            print(f"- {dup}\n  duplicado de: {original}\n")
    else:
        print("Nenhum arquivo duplicado encontrado.")

if __name__ == "__main__":
    encontrar_duplicados(PASTA_BUSCA)