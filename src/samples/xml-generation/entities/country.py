import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class Country:

    def __init__(self, name: str):
        self._id = str_to_ascii(name)
        self._name = name

    def to_xml(self):
        country_element = ET.Element("Country")
        country_element.set("id", str(self._id))

        ET.SubElement(country_element, "Name").text = self._name

        return country_element

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
