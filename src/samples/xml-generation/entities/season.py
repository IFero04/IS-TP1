import xml.etree.ElementTree as ET

import entities.player
import entities.team


class Season:

    def __init__(self, season_year, gp, pts, reb, ast, net_rating, oreb_pct
                 , dreb_pct, usg_pct, ts_pct, ast_pct, player, team):
        Season.counter += 1
        self._id = Season.counter
        self._season_year = season_year
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
        self._player = player
        self._team = team

    def to_xml(self):
        el = ET.Element("Season")
        el.set("id", str(self._id))
        el.set("season_year", self._season_year)
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
        el.set("player_ref", str(self._player.get_id()))
        el.set("team_ref", str(self._team.get_id()))
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._season_year} ({self._id}"


Season.counter = 0
