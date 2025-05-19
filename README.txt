Downloader, Organizer and File Utilities in Python

Simple and didactic scripts to download, organize, convert, unzip, rename and find duplicate files automatically using Python. Perfect for learning about automation, file manipulation, and web scraping!

---

About the project

This repository contains several independent automation scripts, including:

- **baixador_arquivos.py**: Downloads all files of a specific extension (.zip, .pdf, .jpg, etc.) from a web page, saving them in the desired folder.
  Execute: pip install requests beautifulsoup4 tqdm
- **organizador_arquivos.py**: Organizes files into subfolders, separating them by keywords found in the file name.
- **renomeador_em_massa.py**: Mass renames files, applying prefixes, suffixes, and sequential numbering.
- **descompactador_automatico.py**: Unzips all .zip files in the folder, each into its own subfolder.
- **conversor_png_jpg.py**: Converts all .png images in the folder to .jpg using Pillow.
  Execute: pip install pillow
- **buscador_duplicados.py**: Finds and lists duplicate files by content, using hash.

You can adapt these scripts for personal projects, learning, file organization, or as a foundation for more advanced automations!

---

How to use

1. Prerequisites

- Python 3.x installed
- Install the required libraries (example):
  pip install requests beautifulsoup4 tqdm pillow

---

2. Download files from a website

Edit the baixador_arquivos.py file with:
- The website URL you want to download files from
- The folder path where you want to save files
- The file extension you want to download

Example configuration at the top of the file:
URL_SITE = "https://google.com/"
PASTA_DESTINO = "E:\\"
EXTENSAO = ".zip"

Run:
python baixador_arquivos.py

---

3. Organize files by keyword

Edit the organizador_arquivos.py file with:
- The folder path where the downloaded files are
- The extension of files you want to organize
- The list of keywords to define subfolders

Example:
PASTA_ORIGEM = "E:\\"
EXTENSAO = ".zip"
PALAVRAS_CHAVE = [
    "Frontend", "Java", "Flutter", "BackEnd", "Python", "JavaScript", "React",
    "React Native", "Fullstack", "Logica de Programacao", "Programar do Zero",
    "Renda Extra", "TypeScript"
]

Run:
python organizador_arquivos.py

---

4. Mass rename files

Edit the renomeador_em_massa.py file to define prefix, suffix, and extension.
Run:
python renomeador_em_massa.py

---

5. Unzip all zips

Edit the folder path at the start of descompactador_automatico.py.
Run:
python descompactador_automatico.py

---

6. Convert PNG images to JPG

Edit the folder path at the start of conversor_png_jpg.py.
Run in the terminal:
pip install pillow
Then run:
python conversor_png_jpg.py

---

7. Find duplicate files

Edit the folder path at the start of buscador_duplicados.py.
Run:
python buscador_duplicados.py

---

Usage example

- Download all .zip files from a course website.
- Organize the zips into folders by keyword (Java, Python, Frontend, etc.).
- Rename files with a standard numbering.
- Unzip all zips into automatic subfolders.
- Convert .png images to .jpg in batch.
- Find duplicate files in your collection.

---

Author

Developed by Gustavo Dimas

- GitHub: https://github.com/gustadimas
- E-mail: gustavodimas.92@gmail.com
- Linktree: https://linktr.ee/gustavodimas

Feel free to get in touch, contribute, or suggest improvements!

---

License

This project is open-source for learning purposes and may be used or modified as you wish.
