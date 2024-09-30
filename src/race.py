""" A module for representing a race in Dungeons and Dragons. """

# pylint: disable=line-too-long
class Race:
    """ A class to represent a race in Dungeons and Dragons. """
    def __init__(self, name):
        self.name = name
        self.stats = self.get_race_bonus_stat()
        self.speed = self.get_race_speed()
        self.languages = self.get_race_languages()
        self.traits = self.get_race_traits()

    def get_race_bonus_stat(self):
        """ Get the bonus stats of the Race."""
        race_bonus_stat = {
            "Humans": {
                "Strength": 1,
                "Dexterity": 1,
                "Constitution": 1,
                "Intelligence": 1,
                "Wisdom": 1,
                "Charisma": 1
            },
            "Elves": {
                "Dexterity": 2,
                "Intelligence": 1
            },
            "Dwarves": {
                "Constitution": 2,
                "Wisdom": 1
            },
            "Halflings": {
                "Dexterity": 2,
                "Charisma": 1
            },
            "Half-Orcs": {
                "Strength": 2,
                "Constitution": 1
            },
            "Gnomes": {
                "Intelligence": 2,
                "Constitution": 1
            },
            "Half-Elves": {
                "Charisma": 2,
                "Two Other Stats": 1 #TODO Fix
            },
            "Dragonborn": {
                "Strength": 2,
                "Charisma": 1
            },
            "Tieflings": {
                "Intelligence": 1,
                "Charisma": 2
            }
        }
        return race_bonus_stat[self.name]

    def get_race_speed(self):
        """ Get the speed of the Race."""
        race_speed = {
            "Humans": 30,
            "Elves": 30,
            "Dwarves": 25,
            "Halflings": 25,
            "Half-Orcs": 30,
            "Gnomes": 25,
            "Half-Elves": 30,
            "Dragonborn": 30,
            "Tieflings": 30
        }
        return race_speed[self.name]

    def get_race_languages(self):
        """ Get the languages of the Race."""
        race_languages = {
            "Humans": ["Common"],
            "Elves": ["Common", "Elvish"],
            "Dwarves": ["Common", "Dwarvish"],
            "Halflings": ["Common", "Halfling"],
            "Half-Orcs": ["Common", "Orc"],
            "Gnomes": ["Common", "Gnomish"],
            "Half-Elves": ["Common", "Elvish"],
            "Dragonborn": ["Common", "Draconic"],
            "Tieflings": ["Common", "Infernal"]
        }

        return race_languages[self.name]

    def get_race_traits(self):
        """ Get the traits of the Race. """
        race_traits = {
            "Humans": ["None"],
            "Elves": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
            "Dwarves": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning"],
            "Halflings": ["Lucky", "Brave", "Halfling Nimbleness"],
            "Half-Orcs": ["Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"],
            "Gnomes": ["Darkvision", "Gnome Cunning"],
            "Half-Elves": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
            "Dragonborn": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
            "Tieflings": ["Darkvision", "Hellish Resistance", "Infernal Legacy"]
        }

        return race_traits[self.name]
