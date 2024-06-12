import os
# import opendatasets as od
import requests


def download_dataset(dataset_url, dataset_path, csv_file_path):
    if os.path.exists(csv_file_path):
        print(f'O conjunto de dados já foi baixado em {dataset_path}')
        print('Pulando o download...')
    else:
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
        # od.download(dataset_url, dataset_path)
        response = requests.get(dataset_url)
        if response.status_code == 200:
            with open(csv_file_path, 'wb') as file:
                file.write(response.content)
            print(
                f'O conjunto de dados foi baixado com sucesso em {dataset_path}')
        else:
            print(f'Falha ao baixar o conjunto de dados de {dataset_url}')
            print(f'Código de status: {response.status_code}')


def delete_dataset(csv_file_path):
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
        print(
            f'O conjunto de dados foi removido com sucesso de {csv_file_path}')
    else:
        print(f'O conjunto de dados não existe em {csv_file_path}')
