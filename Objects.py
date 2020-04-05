# Import of seasons
import os
import sys
import inspect
# from Database import check_database
direc = os.path.dirname(os.path.abspath(__file__))
sys.path.append(direc)
from Seasons import Seasons


class Match:
    def __init__(self, gameid, teams, match_type, year):
        self.gameid = gameid
        self.teams = teams
        self.match_type = match_type
        self.year = year


class Team:
    def __init__(self, color, number, events, year):
        self.color = color
        self.number = number
        self.events = events
        self.year = year


class EventWrapper:
    datatypes = {
        "timestamp": "timestamp",
        "displayname": "text",
        "starttime": "time",
        "endtime": "time",
        "gamephase": "text",
        "comment": "text",
        "eventid": "integer",
        "scouterid": "smallint"
    }
    """
    :param timestamp: When was this object created
    :param displayname: How this event will be named in the website
    :param starttime: When did the event begin
    :param event: The desired event from the classes in Seasons
    :param endtime: When did the event end
    :param gamephase: In what phase of the game did it happen? (auto,teleop,endgame)
    :param comment: Scouter comment on the event
    :param eventid: ID of the event (given automatically by the website probably)
    :param year: The year where the event occurs
    :param competition: The competition where the event occurs
    :param scouterid: ID of the scouter inputting the event (probably will be assigned by the web server)
    """
    def __init__(self, timestamp, displayname, starttime, gamephase, comment,
                 endtime, event, eventid, year, competition, scouterid):
        self.timestamp = timestamp
        self.displayname = displayname
        self.starttime = starttime
        self.gamephase = gamephase
        self.comment = comment
        self.endtime = endtime
        self.event = event
        self.eventid = eventid
        self.year = year
        self.competition = competition
        self.scouterid = scouterid


def print_classes(cls):
    print([m[0] for m in inspect.getmembers(Seasons, inspect.isclass) if m[1].__module__ == str(cls)])


"""
if __name__ == "__main__":
    with check_database("scouting", "gonen") as db, db.cursor() as cur:
        pass
"""