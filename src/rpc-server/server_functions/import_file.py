import base64
from io import StringIO
from xml_generation.csv_to_xml_converter import CSVtoXMLConverter
from xml_generation.functions.validator import validate_xml


def import_csv(encoded_file):
    try:
        decoded_file = base64.b64decode(encoded_file).decode('utf-8')

        csv_file = StringIO(decoded_file)

        converter = CSVtoXMLConverter(decoded_file)

        xml_str = converter.xml_to_str()

        with open("/data/output/NBA_all_seasons.xml", "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_str)

        return f"XML gerado e salvo."

    except Exception as e:
        return f"Error: {e}"
