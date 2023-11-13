import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.team import Team
from entities.player import Player
from entities.college import College
from entities.season import Season


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

        colleges = self._reader.read_entities(
            attr="college",
            builder=lambda row: College(row["college"])
        )

        def after_creating_season(season, row):
            players[row["player_name"]].add_season(season)
            teams[row["team_abbreviation"]].add_season(season)

        self._reader.read_entities(
            attr="season",
            builder=lambda row: Season(
                season=row["season"],
                gp=row["gp"],
                pts=row["pts"],
                reb=row["reb"],
                ast=row["ast"],
                net_rating=row["net_rating"],
                oreb_pct=row["oreb_pct"],
                dreb_pct=row["dreb_pct"],
                usg_pct=row["usg_pct"],
                ts_pct=row["ts_pct"],
                ast_pct=row["ast_pct"],
                team=teams[row["team_abbreviation"]],
                player=players[row["player_name"]])
            ,

            after_create=after_creating_season
        )

        # read players

        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["team_abbreviation"]].add_player(player)
            countries[row['country']].add_player(player)
            colleges[row['college']].add_player(player)

        players = self._reader.read_entities(
            attr="player_name",
            builder=lambda row: Player(
                name=row["player_name"],
                age=row["age"],
                height=row["height"],
                weight=row["weight"],
                draft_year=row["draft_year"],
                draft_round=row["draft_round"],
                draft_number=row["draft_number"],
                country=countries[row["country"]],
                team=teams[row["team_abbreviation"]],
                college=colleges[row["college"]]

            ),
            after_create=after_creating_player
        )

        # generate the final xml
        root_el = ET.Element("NBAData")

        teams_el = ET.Element("teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        colleges_el = ET.Element("colleges")
        for college in colleges.values():
            colleges_el.append(college.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)
        root_el.append(colleges_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
