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


def list_files():
    try:
        query = '''
            SELECT file_name
            FROM imported_xml
            WHERE deleted_on IS NULL
        '''

        db = PostgresDB()
        response = db.execute_query(query)
        db.close_connection()

        file_data = []
        for item in response:
            file_name = item[0]

            file_data.append(file_name)

        return file_data

    except Exception as e:
        return f"Error: {e}"


def remove_file(file_name):
    try:
        query = '''
            UPDATE imported_xml
            SET deleted_on = CURRENT_TIMESTAMP
            WHERE 
                file_name = %s 
                AND deleted_on IS NULL 
            RETURNING deleted_on
        '''
        parameters = (file_name, )

        db = PostgresDB()
        response = db.execute_query(query, parameters)
        db.close_connection()
        if response:
            return 'Ficheiro Removido'
        return 'Ficheiro Não Existe'

    except Exception as e:
        return f"Error: {e}"

