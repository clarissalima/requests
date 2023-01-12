import os
import requests

saida_dir = ("C:\\Users\\clari\\Desktop\\LASER\\python-pdf")

urls = [
    "https://edisciplinas.usp.br/pluginfile.php/3257195/mod_resource/content/0/As_dez_mulheres_mais_importantes_da_hist%C3%B3ria_da_tecnologia_-_Personalidades.pdf"
    
    # "4222d5e0-4feb-4a4b-9675-d67569c1f7ef.pdf"

    ]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        arquivo_path = os.path.join(saida_dir, os.path.basename(url))
        with open(arquivo_path, 'wb') as f:
            f.write(response.content)