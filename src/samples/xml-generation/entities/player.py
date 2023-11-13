import xml.etree.ElementTree as ET

from entities.college import College
from entities.country import Country


class Player:

    def __init__(self, name, age, height, weight, draft_year, draft_round, draft_number, college, country):
        Player.counter += 1
        self._id = Player.counter
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
        el = ET.Element("Player")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("age", self._age)
        el.set("height", self._height)
        el.set("weight", self._weight)
        el.set("draft_year", self._draft_year)
        el.set("draft_round", self._draft_round)
        el.set("draft_number", self._draft_number)
        el.set("college_ref", str(self._college.get_id()))
        el.set("country_ref", str(self._country.get_id()))

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._name}, age:{self._age}, college:{self._college}, country:{self._country}"


Player.counter = 0
