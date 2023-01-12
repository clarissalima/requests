import os
import requests


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    BASE_URL = 'https://app.ekodevices.com/patient/a9a196f8-0473-4a16-a72e-38fa77e41435/recording/4222d5e0-4feb-4a4b-9675-d67569c1f7ef'
    OUTPUT_DIR = 'output'
#    for i in range(1, 26):
#        nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
#        baixar_arquivo(BASE_URL.format(i), nome_arquivo) 