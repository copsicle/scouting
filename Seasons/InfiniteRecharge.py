year = 2020
autotime = 15
teleoptime = 135
endgametime = 30


class PickUpPowerCell:
    datatypes = {
        "place": "text",
        "numtried": "smallint",
        "numsucceeded": "smallint"
    }

    def __init__(self, place, numtried, numsucceeded):
        """
        Pick up of power cells
        :param place: Where did the pickup happen
        :param numtried: How much did the robot try to pick up
        :param numsucceeded: How much did the robot actually pick up
        """
        self.place = place
        self.numtried = numtried
        self.numsucceeded = numsucceeded


class ShootPowerCell:
    datatypes = {
        "place": "text",
        "target": "text",
        "numtried": "smallint",
        "numsucceeded": "smallint",
        "pickedup": "boolean"
    }

    def __init__(self, place, target, numtried, numsucceeded, pickedup):
        """
        Pick up of power cells
        :param place: Where was the robot when it shot
        :param target: What level did it aim for
        :param numtried: How much did the robot try to shoot
        :param numsucceeded: How much did the robot actually score
        :param pickedup: Did the robot start with the power cells or did it pick them up
        """
        self.place = place
        self.target = target
        self.numtried = numtried
        self.numsucceeded = numsucceeded
        self.pickedup = pickedup


class StoppedWorking:
    datatypes = {}

    def __init__(self):
        """
        Robot has stopped functioning
        """
        pass


class PlayedDefense:
    datatypes = {
        "target": "text"
    }

    def __init__(self, target):
        """
        Robot played defense on another robot
        :param target: The team that got defended
        """
        self.target = target


class ControlPanel:
    datatypes = {
        "controllevel": "text"
    }

    def __init__(self, controllevel):
        """
        Robot spun the control panel
        :param controllevel: What level does it spin to?
        """
        self.controllevel = controllevel


class Climbing:
    datatypes = {
        "didclimb": "boolean",
        "selflevelable": "boolean",
        "lifted": "smallint",
        "waslifted": "boolean"
    }

    def __init__(self, didclimb, selflevelable, lifted, waslifted):
        """
        Robot climb attempt
        :param didclimb: Did the robot climb
        :param selflevelable: Can the robot level itself on the scale
        :param lifted: How much robots did the robot lift with him
        :param waslifted: Was the robot lifted by another robot
        """
        self.didclimb = didclimb
        self.selflevelable = selflevelable
        self.lifted = lifted
        self.waslifted = waslifted


class Attacked:
    datatypes = {}

    def __init__(self):
        """
        The robot got attacked
        """
        pass
