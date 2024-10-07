""" A module to represent a class in Dungeons and Dragons. """

class CharacterClass:
    """ A class to represent a class in Dungeons and Dragons. """
    def __init__(self, name):
        self.name = name
        self.hit_die = self.get_hit_die()
        self.primary_stat = self.get_primary_stat()
        self.saving_throws_proficiencies = self.get_saving_throw_proficiencies()
        self.skill_proficiencies = self.get_skill_proficiencies()

    def get_hit_die(self):
        """ Get the hit die of the class. """
        hit_die = {
            "Barbarian": 12,
            "Bard": 8,
            "Cleric": 8,
            "Druid": 8,
            "Fighter": 10,
            "Monk": 8,
            "Paladin": 10,
            "Ranger": 10,
            "Rogue": 8,
            "Sorcerer": 6,
            "Warlock": 8,
            "Wizard": 6
        }
        return hit_die[self.name]

    def get_primary_stat(self):
        """ Get the primary stat of the class. """
        primary_stat = {
            "Barbarian": ["Strength"],
            "Bard": ["Charisma"],
            "Cleric": ["Wisdom"],
            "Druid": ["Wisdom"],
            "Fighter": ["Strength", "Dexterity"],
            "Monk": ["Dexterity", "Wisdom"],
            "Paladin": ["Strength", "Charisma"],
            "Ranger": ["Dexterity", "Wisdom"],
            "Rogue": ["Dexterity"],
            "Sorcerer": ["Charisma"],
            "Warlock": ["Charisma"],
            "Wizard": ["Intelligence"]
        }
        return primary_stat[self.name]

    def get_worst_stat(self):
        """ Get the worst stat of the class. """
        worst_stat = {
            "Barbarian": ["Intelligence"],
            "Bard": ["Strength"],
            "Cleric": ["Strength"],
            "Druid": ["Strength"],
            "Fighter": ["Intelligence"],
            "Monk": ["Intelligence"],
            "Paladin": ["Intelligence"],
            "Ranger": ["Intelligence"],
            "Rogue": ["Strength"],
            "Sorcerer": ["Strength"],
            "Warlock": ["Strength"],
            "Wizard": ["Strength"]
        }

        return worst_stat[self.name]

    def get_saving_throw_proficiencies(self):
        """ Get the saving throws of the class. """
        saving_throws = {
            "Barbarian": ["Strength", "Constitution"],
            "Bard": ["Dexterity", "Charisma"],
            "Cleric": ["Wisdom", "Charisma"],
            "Druid": ["Intelligence", "Wisdom"],
            "Fighter": ["Strength", "Constitution"],
            "Monk": ["Strength", "Dexterity"],
            "Paladin": ["Wisdom", "Charisma"],
            "Ranger": ["Strength", "Dexterity"],
            "Rogue": ["Dexterity", "Intelligence"],
            "Sorcerer": ["Constitution", "Charisma"],
            "Warlock": ["Wisdom", "Charisma"],
            "Wizard": ["Intelligence", "Wisdom"]
        }
        return saving_throws[self.name]

    def get_skill_proficiencies(self):
        """ Get the skills of the class. """
        skills = {
            "Barbarian": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
            "Bard": ["Acrobatics", "Performance", "Persuasion"],
            "Cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
            "Druid": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
            "Fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
            "Monk": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
            "Paladin": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
            "Ranger": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
            "Rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
            "Sorcerer": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
            "Warlock": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
            "Wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        }
        return skills[self.name]

    @staticmethod
    def get_all_classes():
        """ Get all classes. """
        return [
            "Barbarian",
            "Bard",
            "Cleric",
            "Druid",
            "Fighter",
            "Monk",
            "Paladin",
            "Ranger",
            "Rogue",
            "Sorcerer",
            "Warlock",
            "Wizard"
        ]
