import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii


class Team:

    def __init__(self, abbreviation: str):
        self._id = str_to_ascii(abbreviation.strip())
        self._abbreviation = abbreviation

    def to_xml(self):
        team_element = ET.Element("team")
        team_element.set("id", str(self._id))

        ET.SubElement(team_element, "abbreviation").text = str(self._abbreviation)

        return team_element

    def __str__(self):
        return f"{self._abbreviation} ({self._id})"
