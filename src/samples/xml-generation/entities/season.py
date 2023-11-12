import xml.etree.ElementTree as ET

import entities.player
import entities.team


class Season:

    def __init__(self, season, gp, pts, reb, ast, net_rating, oreb_pct, dreb_pct, usg_pct, ts_pct, ast_pct):
        Season.counter += 1
        self._id = Season.counter
        self._season = season
        self._gp = gp
        self._pts = pts
        self._reb = reb
        self._ast = ast
        self._net_rating = net_rating
        self._oreb_pct = oreb_pct
        self._dreb_pct = dreb_pct
        self._usg_pct = usg_pct
        self._ts_pct = ts_pct
        self._ast_pct = ast_pct
        self._players = []
        self._teams = []

    def add_player(self, player: Player):
        self._players.append(player)

    def add_team(self, team: Team):
        self._teams.append(team)

    def to_xml(self):
        el = ET.Element("Season")
        el.set("id", str(self._id))
        el.set("season", self._season)
        el.set("gp", self._gp)
        el.set("pts", self._pts)
        el.set("reb", self._reb)
        el.set("ast", self._ast)
        el.set("net_rating", self._net_rating)
        el.set("oreb_pct", self._oreb_pct)
        el.set("dreb_pct", self._dreb_pct)
        el.set("usg_pct", self._usg_pct)
        el.set("ts_pct", self._ts_pct)
        el.set("ast_pct", self._ast_pct)

        players_el = ET.Element("players")
        for player in self._players:
            player_el = ET.Element("player_ref")
            player_el.set("id", str(player.get_id()))
            players_el.append(player_el)

        el.append(players_el)

        teams_el = ET.Element('teams')
        for team in self._teams:
            team_el = ET.Element("team_ref")
            team_el.set("id", str(team.get_id()))
            teams_el.append(team_el)

        el.append(teams_el)

        return el

    def __str__(self):
        return f"{self._season} ({self._id}"


Season.counter = 0
