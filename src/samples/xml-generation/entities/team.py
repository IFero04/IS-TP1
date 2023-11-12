import xml.etree.ElementTree as ET

from entities.season import Season


class Team:

    def __init__(self, abbreviation: str):
        Team.counter += 1
        self._id = Team.counter
        self._abbreviation = abbreviation
        self._seasons = []

    def add_season(self, season: Season):
        self._seasons.append(season)

    def to_xml(self):
        el = ET.Element("Team")
        el.set("id", str(self._id))
        el.set("abbreviation", self._abbreviation)

        season_el = ET.Element("Players")
        for season in self._seasons:
            season_el.append(season.to_xml())

        el.append(season_el)

        return el

    def __str__(self):
        return f"{self._abbreviation} ({self._id})"


Team.counter = 0
