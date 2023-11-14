import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class College:

    def __init__(self, name: str):
        self._id = str_to_ascii(name.strip())
        self._name = name

    def to_xml(self):
        college_element = ET.Element("college")
        college_element.set("id", str(self._id))

        ET.SubElement(college_element, "name").text = str(self._name)

        return college_element

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
