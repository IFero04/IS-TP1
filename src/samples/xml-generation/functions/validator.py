from xmlschema import XMLSchema


def validate_xml(xml_document):
    # Load XML Schema
    schema = XMLSchema('/data/validator.xsd')  # Use the file path directly

    try:
        schema.validate(xml_document)
    except Exception as e:
        raise Exception(e)
