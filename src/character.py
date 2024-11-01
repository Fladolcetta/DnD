""" A module to represent a character in Dungeons and Dragons. """
from src.dice import Dice
from src.race import Race
from src.db import DB
from src.character_class import CharacterClass


class Character:
    """ A class to represent a character in Dungeons and Dragons. """
    def __init__(self) -> None:
        self.name = "Unnamed"
        self.race = "Human"
        self.dnd_class = "Fighter"
        self.level = 1
        self.ac = 10
        self.initiative = 0
        self.hp = 0
        self.passive_perception = 10
        self.speed = 0
        self.proficiency_bonus = 2
        self.hit_die = "0d0"
        self.skill_proficiencies = {}
        self.save_proficiencies = {}
        self.saving_throws = {}
        self.all_skills = {}
        self.traits = []
        self.languages = []
        self.stats = {
            "Constitution": 0,
            "Dexterity": 0,
            "Strength": 0,
            "Wisdom": 0,
            "Intelligence": 0,
            "Charisma": 0
        }
        self.char_id = None

    def new_character(self, name: str, race: str, dnd_class: str, stats=None) -> None:
        """ Create a new character. """
        # Roll stats and update values
        self.name = name
        self.race = race
        self.dnd_class = dnd_class
        if stats is None:
            primary_stat = CharacterClass(self.dnd_class).get_primary_stat()
            worst_stat = CharacterClass(self.dnd_class).get_worst_stat()
            self.roll_stats(primary_stat, worst_stat)
        else:
            self.stats = stats
        self.update_race_details()
        self.update_skills()
        self.update_class_details()
        self.update_ac()
        self.update_initiative()
        self.update_hp()
        self.update_passive_perception()

    def store_character_in_db(self) -> None:
        """ Create the character in the database. """
        db = DB()
        self.char_id = db.insert_character(self.name, self.race, self.dnd_class, self.stats)

    def find_modifier_stat(self, stat: str) -> int:
        """ Find the modifier for a given stat. """
        return Character.find_modifier_value(self.stats[stat])

    @staticmethod
    def find_modifier_value(value: int) -> int:
        """ Find the modifier for a given value. """
        return (value - 10) // 2

    def update_race_details(self) -> None:
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
        self.stats = dict(sorted(self.stats.items()))

    def update_class_details(self) -> None:
        """ Update the character based on the class. """
        class_object = CharacterClass(self.dnd_class)
        self.hit_die = str(self.level) + "d" + str(class_object.hit_die)
        self.skill_proficiencies = class_object.get_skill_proficiencies()
        for skill in self.all_skills:
            if skill in self.skill_proficiencies:
                self.all_skills[skill] = self.all_skills[skill] + self.proficiency_bonus

        self.save_proficiencies = class_object.get_saving_throw_proficiencies()
        for stat, value in self.stats.items():
            modifier = Character.find_modifier_value(value)
            if stat in self.save_proficiencies:
                modifier = modifier + self.proficiency_bonus
            self.saving_throws[stat] = modifier

    def update_skills(self) -> None:
        """ Update the skills based on the stats. """
        strength_skills = ["Athletics"]
        dexterity_skills = ["Acrobatics", "Sleight of Hand", "Stealth"]
        intelligence_skills = ["Arcana", "History", "Investigation", "Nature", "Religion"]
        wisdom_skills = ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"]
        charisma_skills = ["Deception", "Intimidation", "Performance", "Persuasion"]
        self.update_skill_for_stat("Strength", strength_skills)
        self.update_skill_for_stat("Dexterity", dexterity_skills)
        self.update_skill_for_stat("Intelligence", intelligence_skills)
        self.update_skill_for_stat("Wisdom", wisdom_skills)
        self.update_skill_for_stat("Charisma", charisma_skills)
        self.all_skills = dict(sorted(self.all_skills.items()))

    def update_ac(self) -> None:
        """ Update the AC based on the stats. """
        self.ac = 10 + self.find_modifier_stat("Dexterity")

    def update_initiative(self) -> None:
        """ Update the initiative based on the stats. """
        self.initiative = self.find_modifier_stat("Dexterity")

    def update_hp(self) -> None:
        """ Update the HP based on the stats. """
        hit_die_array = self.hit_die.split("d")
        hit_die_count = int(hit_die_array[0])
        hit_die_sides = int(hit_die_array[1])
        die = Dice(hit_die_count, hit_die_sides, self.find_modifier_stat("Constitution"))
        die.roll()
        self.hp = die.total

    def update_passive_perception(self) -> None:
        """ Update the passive perception based on the stats. """
        base_perception = 10
        wisdom_modifier = self.find_modifier_stat("Wisdom")
        perception_proficiency = 0
        if "Perception" in self.skill_proficiencies:
            perception_proficiency = self.proficiency_bonus
        self.passive_perception = base_perception + wisdom_modifier + perception_proficiency

    def roll_stats(self, primary_stat: list, worst_stat: list) -> None:
        """ Roll the stats for the character. """
        die = Dice(4, 6, 0)
        stat_array = die.roll_stats()
        stat_array.sort(reverse=True)
        for stat in primary_stat:
            self.stats[stat] = stat_array.pop(0)
        for stat in worst_stat:
            self.stats[stat] = stat_array.pop()
        for key, value in self.stats.items():
            if value == 0:
                self.stats[key] = stat_array.pop(0)

    def update_skill_for_stat(self, stat: str, skill_list: list) -> None:
        """ Update the skill based on the stat. """
        for skill in skill_list:
            self.all_skills[skill] = self.find_modifier_stat(stat)

    def load_character_from_db(self, char_id: int) -> None:
        """ Load the character from the database. """
        db = DB()
        char_dict = db.load_character(char_id)
        name = char_dict["name"]
        dnd_class = char_dict["dnd_class"]
        race = char_dict["race"]
        stats = char_dict["stats"]
        self.new_character(name, race, dnd_class, stats)
        self.char_id = char_id

    def roll_check(self, check_type: str, check="") -> int:
        """ Roll a check based on type. """
        modifier = 0
        if check_type == "stat":
            modifier = self.find_modifier_stat(check)
        elif check_type == "skill":
            modifier = self.all_skills[check]
        elif check_type == "save":
            modifier = self.saving_throws[check]
        elif check_type == "death":
            modifier = 0
        die = Dice(1, 20, 0)
        die.roll()
        return die.total + modifier
