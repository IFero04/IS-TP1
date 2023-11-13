import xml.etree.ElementTree as ET
from entities.functions.str_to_ascii import str_to_ascii

class Player:

    def __init__(self, name, age, height, weight, draft_year, draft_round, draft_number, college, country):
        self._id = str_to_ascii(name)
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self._draft_year = draft_year
        self._draft_round = draft_round
        self._draft_number = draft_number
        self._college = college
        self._country = country

    def to_xml(self):
        player_element = ET.Element("Player")
        player_element.set("id", str(self._id))

        ET.SubElement(player_element, "Name").text = self._name
        ET.SubElement(player_element, "Age").text = str(self._age)
        ET.SubElement(player_element, "Height").text = str(self._height)
        ET.SubElement(player_element, "Weight").text = str(self._weight)
        ET.SubElement(player_element, "DraftYear").text = str(self._draft_year)
        ET.SubElement(player_element, "DraftRound").text = str(self._draft_round)
        ET.SubElement(player_element, "DraftNumber").text = str(self._draft_number)

        ET.SubElement(player_element, "College_ref").set("id", str(self._college.get_id()))
        ET.SubElement(player_element, "Country_ref").set("id", str(self._country.get_id()))

        return player_element

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._name}, age:{self._age}, college:{self._college}, country:{self._country}"
