""" A module to represent a character in Dungeons and Dragons. """
from src.dice import Dice
from src.race import Race
from src.character_class import CharacterClass


class Character:
    """ A class to represent a character in Dungeons and Dragons. """
    def __init__(self, name, desired_race="Human", desired_class="Fighter") -> None:
        self.name = name
        self.race = desired_race
        self.dnd_class = desired_class
        self.level = 1
        self.ac = 10
        self.initiative = 0
        self.hp = 0
        self.passive_perception = 10
        self.primary_stat = []
        self.worst_stat = []
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

        # Roll stats and update values
        self.primary_stat = CharacterClass(self.dnd_class).get_primary_stat()
        self.worst_stat = CharacterClass(self.dnd_class).get_worst_stat()
        self.roll_stats()
        self.update_race_details()
        self.update_skills()
        self.update_class_details()
        self.update_ac()
        self.update_initiative()
        self.update_hp()
        self.update_passive_perception()

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

        saving_throws_stats = self.stats.copy()
        for stat in saving_throws_stats:
            modifier = Character.find_modifier_value(saving_throws_stats[stat])
            self.saving_throws[stat] = modifier
        self.save_proficiencies = class_object.get_saving_throw_proficiencies()
        for saving_throw in self.save_proficiencies:
            self.saving_throws[saving_throw] = self.saving_throws[saving_throw] + self.proficiency_bonus

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
        self.hp = die.total

    def update_passive_perception(self) -> None:
        """ Update the passive perception based on the stats. """
        base_perception = 10
        wisdom_modifier = self.find_modifier_stat("Wisdom")
        perception_proficiency = 0
        if "Perception" in self.skill_proficiencies:
            perception_proficiency = self.proficiency_bonus
        self.passive_perception = base_perception + wisdom_modifier + perception_proficiency

    def roll_stats(self) -> None:
        """ Roll the stats for the character. """
        stat_array = []
        for _ in self.stats:
            die = Dice(4, 6, 0)
            stat_array.append(die.total - min(die.rolls))
        stat_array.sort(reverse=True)
        for primary_stat in self.primary_stat:
            self.stats[primary_stat] = stat_array.pop(0)
        for worst_stat in self.worst_stat:
            self.stats[worst_stat] = stat_array.pop()
        for key, value in self.stats.items():
            if value == 0:
                self.stats[key] = stat_array.pop(0)

    def update_skill_for_stat(self, stat: str, skill_list: list) -> None:
        """ Update the skill based on the stat. """
        for skill in skill_list:
            self.all_skills[skill] = self.find_modifier_stat(stat)
