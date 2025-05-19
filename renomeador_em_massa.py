"""
Renomeia em massa arquivos de uma pasta, aplicando prefixo, sufixo e numeração sequencial.
"""

import os

PASTA_ALVO = "E:\\"  # Altere para sua pasta
PREFIXO = "arquivo_"
SUFIXO = ""
EXTENSAO = ".zip"  # Só arquivos dessa extensão; deixe "" para todos

def renomear_em_massa(pasta, prefixo="", sufixo="", extensao=""):
    arquivos = sorted(f for f in os.listdir(pasta) if f.endswith(extensao))
    for i, arquivo in enumerate(arquivos, 1):
        nome_antigo = os.path.join(pasta, arquivo)
        base, ext = os.path.splitext(arquivo)
        novo_nome = f"{prefixo}{i:03d}{sufixo}{ext}"
        nome_novo = os.path.join(pasta, novo_nome)
        print(f"{arquivo} --> {novo_nome}")
        os.rename(nome_antigo, nome_novo)

if __name__ == "__main__":
    renomear_em_massa(PASTA_ALVO, PREFIXO, SUFIXO, EXTENSAO)