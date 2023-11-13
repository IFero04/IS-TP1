import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class Team:

    def __init__(self, abbreviation: str):
        self._id = str_to_ascii(abbreviation)
        self._abbreviation = abbreviation

    def to_xml(self):
        el = ET.Element("Team")
        el.set("id", str(self._id))
        el.set("abbreviation", self._abbreviation)

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._abbreviation} ({self._id})"
