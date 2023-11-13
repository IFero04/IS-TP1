import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class Team:

    def __init__(self, abbreviation: str):
        self._id = str_to_ascii(abbreviation)
        self._abbreviation = abbreviation

    def to_xml(self):
        team_element = ET.Element("Team")
        team_element.set("id", str(self._id))

        ET.SubElement(team_element, "Abbreviation").text = self._abbreviation

        return team_element

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._abbreviation} ({self._id})"
