""" A module for representing a race in Dungeons and Dragons. """

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
            "Human": {
                "Strength": 1,
                "Dexterity": 1,
                "Constitution": 1,
                "Intelligence": 1,
                "Wisdom": 1,
                "Charisma": 1
            },
            "Elf": {
                "Dexterity": 2,
                "Intelligence": 1
            },
            "Dwarf": {
                "Constitution": 2,
                "Wisdom": 1
            },
            "Halfling": {
                "Dexterity": 2,
                "Charisma": 1
            },
            "Half-Orc": {
                "Strength": 2,
                "Constitution": 1
            },
            "Gnome": {
                "Intelligence": 2,
                "Constitution": 1
            },
            "Half-Elf": {
                "Charisma": 2,
                "Constitution": 1,
                "Wisdom": 1
            },
            "Dragonborn": {
                "Strength": 2,
                "Charisma": 1
            },
            "Tiefling": {
                "Intelligence": 1,
                "Charisma": 2
            }
        }
        return race_bonus_stat[self.name]

    def get_race_speed(self):
        """ Get the speed of the Race."""
        race_speed = {
            "Human": 30,
            "Elf": 30,
            "Dwarf": 25,
            "Halfling": 25,
            "Half-Orc": 30,
            "Gnome": 25,
            "Half-Elf": 30,
            "Dragonborn": 30,
            "Tiefling": 30
        }
        return race_speed[self.name]

    def get_race_languages(self):
        """ Get the languages of the Race."""
        race_languages = {
            "Human": ["Common"],
            "Elf": ["Common", "Elvish"],
            "Dwarf": ["Common", "Dwarvish"],
            "Halfling": ["Common", "Halfling"],
            "Half-Orc": ["Common", "Orc"],
            "Gnome": ["Common", "Gnomish"],
            "Half-Elf": ["Common", "Elvish"],
            "Dragonborn": ["Common", "Draconic"],
            "Tiefling": ["Common", "Infernal"]
        }

        return race_languages[self.name]

    def get_race_traits(self):
        """ Get the traits of the Race. """
        race_traits = {
            "Human": ["None"],
            "Elf": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
            "Dwarf": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning"],
            "Halfling": ["Lucky", "Brave", "Halfling Nimbleness"],
            "Half-Orc": ["Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"],
            "Gnome": ["Darkvision", "Gnome Cunning"],
            "Half-Elf": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
            "Dragonborn": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
            "Tiefling": ["Darkvision", "Hellish Resistance", "Infernal Legacy"]
        }

        return race_traits[self.name]

    @staticmethod
    def get_all_races():
        """ Get a list of all the Dungeons and Dragons races """
        return [
            "Human",
            "Elf",
            "Dwarf",
            "Halfling",
            "Half-Orc",
            "Gnome",
            "Half-Elf",
            "Dragonborn",
            "Tiefling"
            ]