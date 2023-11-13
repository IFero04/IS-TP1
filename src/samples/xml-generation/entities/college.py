import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class College:

    def __init__(self, name: str):
        self._id = str_to_ascii(name)
        self._name = name

    def to_xml(self):
        el = ET.Element("College")
        el.set("id", str(self._id))
        el.set("name", self._name)

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"
