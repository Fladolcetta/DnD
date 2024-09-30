""" A module to represent a character in Dungeons and Dragons. """
from src.dice import Dice
from src.race import Race
from src.character_class import CharacterClass

class Character:
    """ A class to represent a character in Dungeons and Dragons. """
    def __init__(self, name, desired_race=None, desired_class=None):
        self.name = name
        self.race = desired_race
        self.dnd_class = desired_class
        self.speed = 0
        self.traits = []
        self.languages = []
        self.stats = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }
        self.strength_skills = {
            "Athletics": 0
        }
        self.dexterity_skills = {
            "Acrobatics": 0,
            "Sleight of Hand": 0,
            "Stealth": 0
        }
        self.constitution_skills = {}
        self.intelligence_skills = {
            "Arcana": 0,
            "History": 0,
            "Investigation": 0,
            "Nature": 0,
            "Religion": 0
        }
        self.wisdom_skills = {
            "Animal Handling": 0,
            "Insight": 0,
            "Medicine": 0,
            "Perception": 0,
            "Survival": 0
        }
        self.charisma_skills = {
            "Deception": 0,
            "Intimidation": 0,
            "Performance": 0,
            "Persuasion": 0
        }
        self.all_skills = dict()

        # Roll stats and update values
        self.roll_stats()
        self.update_race_details()
        self.update_skills()

    def find_modifier(self, stat):
        """ Find the modifier for a given stat. """
        return (self.stats[stat] - 10) // 2

    def update_race_details(self):
        """ Update the character based on the race. """
        race_object = Race(self.race)
        self.speed = race_object.speed
        self.languages = race_object.languages
        self.traits = race_object.traits
        for stat in self.stats:
            try:
                self.stats[stat] = self.stats[stat] + race_object.stats[stat]
            except KeyError:
                pass

    def update_skills(self):
        """ Update the skills based on the stats. """
        for stat in self.stats:
            if stat == "Strength":
                for skill in self.strength_skills:
                    self.strength_skills[skill] = self.find_modifier(stat)
            if stat == "Dexterity":
                for skill in self.dexterity_skills:
                    self.dexterity_skills[skill] = self.find_modifier(stat)
            if stat == "Constitution":
                for skill in self.constitution_skills:
                    self.constitution_skills[skill] = self.find_modifier(stat)
            if stat == "Intelligence":
                for skill in self.intelligence_skills:
                    self.intelligence_skills[skill] = self.find_modifier(stat)
            if stat == "Wisdom":
                for skill in self.wisdom_skills:
                    self.wisdom_skills[skill] = self.find_modifier(stat)
            if stat == "Charisma":
                for skill in self.charisma_skills:
                    self.charisma_skills[skill] = self.find_modifier(stat)

        self.all_skills.update(self.strength_skills)
        self.all_skills.update(self.dexterity_skills)
        self.all_skills.update(self.constitution_skills)
        self.all_skills.update(self.intelligence_skills)
        self.all_skills.update(self.wisdom_skills)
        self.all_skills.update(self.charisma_skills)
        self.all_skills = dict(sorted(self.all_skills.items()))


    def roll_stats(self, primary_stat=None, secondary_stat=None):
        """ Roll the stats for the character. """
        for stat in self.stats:
            die = Dice(4, 6, 0)
            total, rolls = die.roll()
            self.stats[stat] = total - min(rolls)
