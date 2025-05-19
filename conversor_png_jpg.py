"""
Converte todas as imagens .png da pasta para .jpg usando Pillow.
"""

import os
from PIL import Image

PASTA_IMAGENS = "E:\\"  # Altere para sua pasta

def converter_png_para_jpg(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".png")]
    for arquivo in arquivos:
        caminho_png = os.path.join(pasta, arquivo)
        caminho_jpg = os.path.join(pasta, os.path.splitext(arquivo)[0] + ".jpg")
        try:
            with Image.open(caminho_png) as img:
                rgb = img.convert('RGB')
                rgb.save(caminho_jpg, quality=95)
            print(f"{arquivo} --> {os.path.basename(caminho_jpg)}")
        except Exception as e:
            print(f"Erro ao converter {arquivo}: {e}")

if __name__ == "__main__":
    converter_png_para_jpg(PASTA_IMAGENS)
