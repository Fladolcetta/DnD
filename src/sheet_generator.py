""" A module for generating a character sheet key_pairs. """
from src.character import Character
from src.text_printer import TextPrinter


class SheetGenerator:
    """ A class to generate a character sheet. """
    def __init__(self, character: Character) -> None:
        """ Initialize the SheetGenerator. """
        self.character = character
        self.key_pairs = {}

    def generate_key_pairs(self) -> dict:
        """ Generate all key pairs for the character sheet. """
        self.key_pairs = self.generate_basic_key_pairs()
        self.key_pairs.update(self.generate_stat_key_pairs())
        self.key_pairs.update(self.generate_saving_throw_key_pairs())
        self.key_pairs.update(self.generate_skill_key_pairs())
        self.key_pairs.update(self.generate_skill_prof_key_pairs())
        self.key_pairs.update(self.generate_saving_throw_prof_key_pairs())
        return self.key_pairs

    def generate_basic_key_pairs(self) -> dict:
        """ Generate basic key pairs for the character sheet. """
        return {
            "charname": self.character.name,
            "race": self.character.race,
            "classlevel": self.character.dnd_class + " " + str(self.character.level),
            "proficiencybonus": self.character.proficiency_bonus,
            "passiveperception": self.character.passive_perception,
            "ac": self.character.ac,
            "initiative": self.character.initiative,
            "speed": self.character.speed,
            "maxhp": self.character.hp,
            "currenthp": self.character.hp,
            "temphp": 0,
            "totalhd": self.character.hit_die,
            "remaininghd": self.character.hit_die.split("d")[0],
            "otherprofs": self.list_to_textarea_string(self.character.languages),
            "features": self.list_to_textarea_string(self.character.traits)
        }

    def generate_stat_key_pairs(self) -> dict:
        """ Generate stat key pairs for the character sheet. """
        return {
            "Strengthscore": self.character.stats["Strength"],
            "Dexterityscore": self.character.stats["Dexterity"],
            "Constitutionscore": self.character.stats["Constitution"],
            "Wisdomscore": self.character.stats["Wisdom"],
            "Intelligencescore": self.character.stats["Intelligence"],
            "Charismascore": self.character.stats["Charisma"],
            "Strengthmod": self.get_stat_modifier("Strength"),
            "Dexteritymod": self.get_stat_modifier("Dexterity"),
            "Constitutionmod": self.get_stat_modifier("Constitution"),
            "Wisdommod": self.get_stat_modifier("Wisdom"),
            "Intelligencemod": self.get_stat_modifier("Intelligence"),
            "Charismamod": self.get_stat_modifier("Charisma")
        }

    def generate_saving_throw_key_pairs(self) -> dict:
        """ Generate saving throw key pairs for the character sheet. """
        return {
            "Strengthsave": self.get_saving_throw_modifier("Strength"),
            "Dexteritysave": self.get_saving_throw_modifier("Dexterity"),
            "Constitutionsave": self.get_saving_throw_modifier("Constitution"),
            "Wisdomsave": self.get_saving_throw_modifier("Wisdom"),
            "Intelligencesave": self.get_saving_throw_modifier("Intelligence"),
            "Charismasave": self.get_saving_throw_modifier("Charisma")
        }

    def generate_skill_key_pairs(self) -> dict:
        """ Generate skill key pairs for the character sheet. """
        return {
            "Acrobatics": self.get_skill_modifier("Acrobatics"),
            "AnimalHandling": self.get_skill_modifier("Animal Handling"),
            "Arcana": self.get_skill_modifier("Arcana"),
            "Athletics": self.get_skill_modifier("Athletics"),
            "Deception": self.get_skill_modifier("Deception"),
            "History": self.get_skill_modifier("History"),
            "Insight": self.get_skill_modifier("Insight"),
            "Intimidation": self.get_skill_modifier("Intimidation"),
            "Investigation": self.get_skill_modifier("Investigation"),
            "Medicine": self.get_skill_modifier("Medicine"),
            "Nature": self.get_skill_modifier("Nature"),
            "Perception": self.get_skill_modifier("Perception"),
            "Performance": self.get_skill_modifier("Performance"),
            "Persuasion": self.get_skill_modifier("Persuasion"),
            "Religion": self.get_skill_modifier("Religion"),
            "SleightofHand": self.get_skill_modifier("Sleight of Hand"),
            "Stealth": self.get_skill_modifier("Stealth"),
            "Survival": self.get_skill_modifier("Survival")
        }

    def generate_skill_prof_key_pairs(self) -> dict:
        """ Generate key pairs for the character sheet. """
        return {
            "Acrobaticsprof": self.check_skill_proficiency("Acrobatics"),
            "AnimalHandlingprof": self.check_skill_proficiency("Animal Handling"),
            "Arcanaprof": self.check_skill_proficiency("Arcana"),
            "Athleticsprof": self.check_skill_proficiency("Athletics"),
            "Deceptionprof": self.check_skill_proficiency("Deception"),
            "Historyprof": self.check_skill_proficiency("History"),
            "Insightprof": self.check_skill_proficiency("Insight"),
            "Intimidationprof": self.check_skill_proficiency("Intimidation"),
            "Investigationprof": self.check_skill_proficiency("Investigation"),
            "Medicineprof": self.check_skill_proficiency("Medicine"),
            "Natureprof": self.check_skill_proficiency("Nature"),
            "Perceptionprof": self.check_skill_proficiency("Perception"),
            "Performanceprof": self.check_skill_proficiency("Performance"),
            "Persuasionprof": self.check_skill_proficiency("Persuasion"),
            "Religionprof": self.check_skill_proficiency("Religion"),
            "SleightofHandprof": self.check_skill_proficiency("Sleight of Hand"),
            "Stealthprof": self.check_skill_proficiency("Stealth"),
            "Survivalprof": self.check_skill_proficiency("Survival")
        }

    def generate_saving_throw_prof_key_pairs(self) -> dict:
        """ Generate key pairs for the character sheet. """
        return {
            "Strengthsaveprof": self.check_save_proficiency("Strength"),
            "Dexteritysaveprof": self.check_save_proficiency("Dexterity"),
            "Constitutionsaveprof": self.check_save_proficiency("Constitution"),
            "Wisdomsaveprof": self.check_save_proficiency("Wisdom"),
            "Intelligencesaveprof": self.check_save_proficiency("Intelligence"),
            "Charismasaveprof": self.check_save_proficiency("Charisma")
        }

    def get_stat_modifier(self, stat: str) -> int:
        """ Get the modifier of the stat. """
        return TextPrinter().print_modifiers(self.character.find_modifier_stat(stat))

    def get_skill_modifier(self, skill: str) -> int:
        """ Get the modifier of the skill. """
        return TextPrinter().print_modifiers(self.character.all_skills[skill])

    def get_saving_throw_modifier(self, save: str) -> int:
        """ Get the modifier of the saving throw. """
        return TextPrinter().print_modifiers(self.character.saving_throws[save])

    def check_skill_proficiency(self, skill: str) -> bool:
        """ Check if the character is proficient in the skill. """
        if skill in self.character.skill_proficiencies:
            return "checked"
        return ""

    def check_save_proficiency(self, save: str) -> bool:
        """ Check if the character is proficient in the save. """
        if save in self.character.save_proficiencies:
            return "checked"
        return ""

    def list_to_textarea_string(self, data: list) -> str:
        """ Convert a list to a string. """
        if not data:
            return ""
        return "- " + "\n- ".join(data)
