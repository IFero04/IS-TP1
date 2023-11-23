import base64
from io import StringIO
from csv import DictReader


def import_csv(encoded_file):
    try:
        decoded_file = base64.b64decode(encoded_file).decode('utf-8')

        csv_file = StringIO(decoded_file)

    except Exception as e:
        print(f"Erro ao decodificar o csv: {e}")

    try:
        pass
    except Exception as e:
        print(f"Erro ao converter o csv para xml: {e}")
