import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

def baixar_arquivo(url_arquivo, pasta_destino):
    """
    Baixa um arquivo de uma URL para a pasta de destino, mostrando barra de progresso.
    """
    nome_arquivo = url_arquivo.split("/")[-1]
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    resposta = requests.get(url_arquivo, stream=True)
    tamanho_total = int(resposta.headers.get('content-length', 0))
    with open(caminho_completo, "wb") as arquivo, tqdm(
        desc=nome_arquivo,
        total=tamanho_total,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as barra:
        for dado in resposta.iter_content(chunk_size=1024):
            if dado:
                arquivo.write(dado)
                barra.update(len(dado))

def encontrar_links_de_arquivos(url, extensao):
    """
    Busca e retorna todos os links de arquivos com a extensão especificada na página.
    """
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, "html.parser")
    links = set()
    for link in sopa.find_all("a", href=True):
        href = link["href"]
        if href.lower().endswith(extensao.lower()):
            links.add(urljoin(url, href))
    return links

def baixar_todos_arquivos(url, pasta_destino, extensao=".zip"):
    """
    Baixa todos os arquivos com a extensão escolhida da página principal para a pasta destino.
    """
    if not os.path.exists(pasta_destino):
        print(f"Pasta {pasta_destino} não existe. Criando...")
        os.makedirs(pasta_destino, exist_ok=True)

    print(f"Buscando arquivos '{extensao}' em {url} ...")
    links = encontrar_links_de_arquivos(url, extensao)
    if not links:
        print(f"Nenhum arquivo '{extensao}' encontrado na página.")
        return

    print(f"{len(links)} arquivos encontrados.")
    for link in links:
        try:
            print(f"Baixando: {link}")
            baixar_arquivo(link, pasta_destino)
        except Exception as e:
            print(f"Erro ao baixar {link}: {e}")

if __name__ == "__main__":
    # ---------- CONFIGURAÇÕES ----------
    URL_SITE = "https://google.com/" # Altere conforme sua necessidade
    PASTA_DESTINO = "E:\\"  # Altere conforme sua necessidade
    EXTENSAO = ".zip"  # Qualquer extensão: ".zip", ".pdf", ".jpg" etc.
    # -----------------------------------
    baixar_todos_arquivos(URL_SITE, PASTA_DESTINO, EXTENSAO)