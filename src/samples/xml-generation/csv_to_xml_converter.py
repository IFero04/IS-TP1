import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.team import Team
from entities.player import Player
from entities.college import College
from entities.entry import Entry


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="country",
            builder=lambda row: Country(row["country"])
        )

        # read teams
        teams = self._reader.read_entities(
            attr="team_abbreviation",
            builder=lambda row: Team(row["team_abbreviation"])
        )

        # read college
        colleges = self._reader.read_entities(
            attr="college",
            builder=lambda row: College(row["college"])
        )

        # read players
        players = self._reader.read_entities(
            attr="player_name",
            builder=lambda row: Player(
                name=row["player_name"],
                age=row["age"],
                height=row["player_height"],
                weight=row["player_weight"],
                draft_year=row["draft_year"],
                draft_round=row["draft_round"],
                draft_number=row["draft_number"],
                country=countries[row["country"]],
                college=colleges[row["college"]]
            )
        )

        # generate the final xml
        root_el = ET.Element("NBAData")

        players_el = ET.Element("players")
        for player in players.values():
            players_el.append(player.to_xml())

        teams_el = ET.Element("teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        colleges_el = ET.Element("colleges")
        for college in colleges.values():
            colleges_el.append(college.to_xml())

        root_el.append(players_el)
        root_el.append(teams_el)
        root_el.append(countries_el)
        root_el.append(colleges_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
