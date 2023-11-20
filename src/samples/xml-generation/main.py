from csv_to_xml_converter import CSVtoXMLConverter
from functions.validator import validate_xml

if __name__ == "__main__":
    input_csv_file = "/data/input/NBA_all_seasons.csv"
    output_xml_file = "/data/output/NBA_all_seasons.xml"

    converter = CSVtoXMLConverter(input_csv_file)

    xml_str = converter.xml_to_str()

    try:
        validate_xml(xml_str)

        with open(output_xml_file, "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_str)

        print(f"XML gerado e salvo em '{output_xml_file}'.")
    except Exception as e:
        print(f"Validation failed: {e}")
