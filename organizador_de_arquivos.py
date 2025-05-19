import os
import shutil

def obter_subpasta_por_palavra(nome_arquivo, palavras_chave):
    """
    Retorna o nome da subpasta baseado na palavra-chave encontrada no nome do arquivo.
    Caso não encontre, retorna 'Outros'.
    """
    nome_arquivo_lower = nome_arquivo.lower()
    for palavra in palavras_chave:
        if palavra.lower() in nome_arquivo_lower:
            return palavra
    return "Outros"

def organizar_arquivos_por_palavra(pasta_origem, extensao=".zip", palavras_chave=None):
    """
    Move arquivos de uma extensão específica para subpastas baseadas em palavras-chave.
    """
    if palavras_chave is None:
        palavras_chave = []

    arquivos = [f for f in os.listdir(pasta_origem) if f.lower().endswith(extensao.lower())]
    if not arquivos:
        print(f"Nenhum arquivo '{extensao}' encontrado na pasta.")
        return
    for arquivo in arquivos:
        subpasta = obter_subpasta_por_palavra(arquivo, palavras_chave)
        destino_subpasta = os.path.join(pasta_origem, subpasta)
        os.makedirs(destino_subpasta, exist_ok=True)
        caminho_atual = os.path.join(pasta_origem, arquivo)
        caminho_novo = os.path.join(destino_subpasta, arquivo)
        if caminho_atual == caminho_novo:
            continue  # já está na subpasta
        print(f"Movendo {arquivo} para {destino_subpasta}")
        shutil.move(caminho_atual, caminho_novo)

if __name__ == "__main__":
    # ----------- CONFIGURAÇÕES -----------
    PASTA_ORIGEM = r"E:\downloads"  # Altere conforme sua necessidade
    EXTENSAO = ".zip"  # Qualquer extensão: ".zip", ".pdf", ".jpg" etc.
    PALAVRAS_CHAVE = [
        "Frontend", "Java", "Flutter", "BackEnd", "Python", "JavaScript", "React",
        "React Native", "Fullstack", "Logica de Programacao", "Programar do Zero",
        "Renda Extra", "TypeScript"
    ]
    # -------------------------------------
    organizar_arquivos_por_palavra(PASTA_ORIGEM, EXTENSAO, PALAVRAS_CHAVE)