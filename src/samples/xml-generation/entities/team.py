import xml.etree.ElementTree as ET


class Team:

    def __init__(self, abbreviation: str):
        Team.counter += 1
        self._id = Team.counter
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


Team.counter = 0
