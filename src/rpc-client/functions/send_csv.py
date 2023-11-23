import os
from functions.encoder_file import encoder_csv


def send_csv(server):
    print('O seu ficheiro deve estar na pasta /docker/volumes/data/input')

    csv_name = input('Digite o nome do ficheiro: ').strip() + '.csv'
    csv_path = os.path.join('/data/input', csv_name)

    encoded_string = encoder_csv(csv_path)

    print('*Nota: Caso ja exista esse nome na base de  dados será atualizado')
    db_file_name = input('Nome para guardar na base de dados: ').strip()

    try:
        response = server.import_csv(encoded_string, db_file_name)
        print(response)
    except Exception as e:
        print(f"An error occurred sending to server: {e}")
