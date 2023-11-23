import base64
from io import StringIO
from xml_generation.csv_to_xml_converter import CSVtoXMLConverter
from db.main import PostgresDB


def import_csv(encoded_string, db_file_name):
    try:
        decoded_string = base64.b64decode(encoded_string).decode('utf-8')

        csv_file = StringIO(decoded_string)

        converter = CSVtoXMLConverter(csv_file)

        xml_str = converter.xml_to_str()

        db = PostgresDB()
        db_response = db.store_xml(xml_str, db_file_name)
        db.close_connection()

        return f"XML gerado e {db_response}."

    except Exception as e:
        return f"Error: {e}"
