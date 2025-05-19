Baixador, Organizador e Utilitários de Arquivos em Python

Scripts simples e didáticos para baixar, organizar, converter, descompactar, renomear e encontrar duplicados de arquivos automaticamente, usando Python. Ideal para aprender automação, manipulação de arquivos e web scraping!

---

Sobre o projeto

Este repositório contém vários scripts independentes de automação, incluindo:

- **baixador_arquivos.py**: Baixa todos os arquivos de uma extensão específica (.zip, .pdf, .jpg, etc) de uma página web, salvando na pasta desejada.
- **execute: pip install requests beautifulsoup4 tqdm
- **organizador_arquivos.py**: Organiza arquivos em subpastas, separando por palavras-chave no nome do arquivo.
- **renomeador_em_massa.py**: Renomeia arquivos em massa, aplicando prefixos, sufixos e numeração sequencial.
- **descompactador_automatico.py**: Descompacta todos os arquivos .zip da pasta, cada um em sua própria subpasta.
- **conversor_png_jpg.py: Converte todas as imagens .png da pasta para .jpg usando Pillow.
- **execute: pip install pillow
- **buscador_duplicados.py**: Procura e lista arquivos duplicados por conteúdo, usando hash.

Você pode adaptar esses scripts para projetos pessoais, estudos, organização de arquivos ou como base para automações mais avançadas!

---

Como usar

1. Pré-requisitos

- Python 3.x instalado
- Instalar as bibliotecas necessárias (exemplo):
  pip install requests beautifulsoup4 tqdm pillow

---

2. Baixar arquivos de um site

Edite o arquivo baixador_arquivos.py com:
- URL do site que deseja baixar arquivos
- Caminho da pasta onde deseja salvar
- Extensão do arquivo que deseja baixar

Exemplo de configuração no topo do arquivo:
URL_SITE = "https://google.com/"
PASTA_DESTINO = "E:\\"
EXTENSAO = ".zip"

Execute:
python baixador_arquivos.py

---

3. Organizar arquivos por palavras-chave

Edite o arquivo organizador_arquivos.py com:
- Caminho da pasta onde estão os arquivos baixados
- Extensão dos arquivos que deseja organizar
- Lista de palavras-chave que define as subpastas

Exemplo:
PASTA_ORIGEM = "E:\\"
EXTENSAO = ".zip"
PALAVRAS_CHAVE = [
    "Frontend", "Java", "Flutter", "BackEnd", "Python", "JavaScript", "React",
    "React Native", "Fullstack", "Logica de Programacao", "Programar do Zero",
    "Renda Extra", "TypeScript"
]

Execute:
python organizador_arquivos.py

---

4. Renomear arquivos em massa

Edite o arquivo renomeador_em_massa.py para definir o prefixo, sufixo e extensão.
Execute:
python renomeador_em_massa.py

---

5. Descompactar todos os zips

Edite o caminho da pasta no início do descompactador_automatico.py.
Execute:
python descompactador_automatico.py

---

6. Converter imagens PNG para JPG

Edite o caminho da pasta no início do conversor_png_jpg.py.
Execute no terminal:
pip install pillow
Execute:
python conversor_png_jpg.py

---

7. Encontrar arquivos duplicados

Edite o caminho da pasta no início do buscador_duplicados.py.
Execute:
python buscador_duplicados.py

---

Exemplo de uso

- Baixe todos os arquivos .zip de um site de cursos.
- Organize os zips em pastas por palavra-chave (Java, Python, Frontend, etc).
- Renomeie arquivos para uma numeração padrão.
- Descompacte todos os zips em subpastas automáticas.
- Converta imagens .png para .jpg em lote.
- Encontre arquivos duplicados na sua coleção.

---

Autor

Desenvolvido por Gustavo Dimas

- GitHub: https://github.com/gustadimas
- E-mail: gustavodimas.92@gmail.com
- Linktree: https://linktr.ee/gustavodimas

Fique à vontade para entrar em contato, contribuir ou sugerir melhorias!

---

Licença

Este projeto é open-source para fins de aprendizado e pode ser utilizado ou modificado à vontade.
