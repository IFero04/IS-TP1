from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    input_csv_file = "/data/NBA_all_seasons.csv"
    output_xml_file = "/data/NBA_all_seasons.xml"

    converter = CSVtoXMLConverter(input_csv_file)

    xml_str = converter.to_xml_str()

    with open(output_xml_file, "w", encoding="utf-8") as xml_file:
        xml_file.write(xml_str)

    print(f"XML gerado e salvo em '{output_xml_file}'.")