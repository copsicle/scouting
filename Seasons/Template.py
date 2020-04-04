"""
This is a template for season specific info and classes module
Endgame time is supposed to be included in the teleop time
"""
year = 4590
autotime = 15
teleoptime = 135
endgametime = 30


class Event1:
    datatypes = {
        "didhetry": "text",
        "didhedo": "smallint"
    }

    def __init__(self, didhetry, didhedo):
        self.didhetry = didhetry
        self.didhedo = didhedo


class Itdobelikethat:
    datatypes = {
        "theysayitaint": "text",
        "butitdo": "smallint"
    }

    def __init__(self, theysayitaint, butitdo):
        self.theysayitaint = theysayitaint
        self.butitdo = butitdo
