""" A module for generating a character sheet key_pairs. """
from src.character import Character
from src.text_printer import TextPrinter


class SheetGenerator:
    """ A class to generate a character sheet. """
    def __init__(self, character: Character) -> None:
        """ Initialize the SheetGenerator. """
        self.character = character
        self.key_pairs = {}

    def unused_key_pairs(self) -> dict:
        """ Generate key pairs for the character sheet. """
        return {
            "background": "Test",
            "playername": "Test",
            "alignment": "Test",
            "experiencepoints": "Test",
            "atkname1": "Test",
            "atkbonus1": "Test",
            "atkdamage1": "Test",
            "atkname2": "Test",
            "atkbonus2": "Test",
            "atkdamage2": "Test",
            "atkname3": "Test",
            "atkbonus3": "Test",
            "atkdamage3": "Test",
            "cp": "Test",
            "sp": "Test",
            "ep": "Test",
            "gp": "Test",
            "pp": "Test"
        }

    def generate_key_pairs(self) -> dict:
        """ Generate all key pairs for the character sheet. """
        self.key_pairs = self.generate_basic_key_pairs()
        self.key_pairs.update(self.generate_stat_key_pairs())
        self.key_pairs.update(self.generate_saving_throw_key_pairs())
        self.key_pairs.update(self.generate_skill_key_pairs())
        self.key_pairs.update(self.generate_skill_prof_key_pairs())

        return self.key_pairs

    def generate_basic_key_pairs(self) -> dict:
        """ Generate basic key pairs for the character sheet. """
        key_pairs = {
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
            "otherprofs": str(self.character.languages),
            "features": str(self.character.traits)
        }
        return key_pairs

    def generate_stat_key_pairs(self) -> dict:
        """ Generate stat key pairs for the character sheet. """
        text_printer = TextPrinter()
        key_pairs = {
            "Strengthscore": self.character.stats["Strength"],
            "Strengthmod": text_printer.print_modifiers(self.character.find_modifier_stat("Strength")),
            "Dexterityscore": self.character.stats["Dexterity"],
            "Dexteritymod": text_printer.print_modifiers(self.character.find_modifier_stat("Dexterity")),
            "Constitutionscore": self.character.stats["Constitution"],
            "Constitutionmod": text_printer.print_modifiers(self.character.find_modifier_stat("Constitution")),
            "Wisdomscore": self.character.stats["Wisdom"],
            "Wisdommod": text_printer.print_modifiers(self.character.find_modifier_stat("Wisdom")),
            "Intelligencescore": self.character.stats["Intelligence"],
            "Intelligencemod": text_printer.print_modifiers(self.character.find_modifier_stat("Intelligence")),
            "Charismascore": self.character.stats["Charisma"],
            "Charismamod": text_printer.print_modifiers(self.character.find_modifier_stat("Charisma"))
        }
        return key_pairs

    def generate_saving_throw_key_pairs(self) -> dict:
        """ Generate saving throw key pairs for the character sheet. """
        text_printer = TextPrinter()
        key_pairs = {
            "Strengthsave": text_printer.print_modifiers(self.character.saving_throws["Strength"]),
            "Dexteritysave": text_printer.print_modifiers(self.character.saving_throws["Dexterity"]),
            "Constitutionsave": text_printer.print_modifiers(self.character.saving_throws["Constitution"]),
            "Wisdomsave": text_printer.print_modifiers(self.character.saving_throws["Wisdom"]),
            "Intelligencesave": text_printer.print_modifiers(self.character.saving_throws["Intelligence"]),
            "Charismasave": text_printer.print_modifiers(self.character.saving_throws["Charisma"])
        }
        return key_pairs

    def generate_skill_key_pairs(self) -> dict:
        """ Generate skill key pairs for the character sheet. """
        text_printer = TextPrinter()
        key_pairs = {
            "Acrobatics": text_printer.print_modifiers(self.character.all_skills["Acrobatics"]),
            "AnimalHandling": text_printer.print_modifiers(self.character.all_skills["Animal Handling"]),
            "Arcana": text_printer.print_modifiers(self.character.all_skills["Arcana"]),
            "Athletics": text_printer.print_modifiers(self.character.all_skills["Athletics"]),
            "Deception": text_printer.print_modifiers(self.character.all_skills["Deception"]),
            "History": text_printer.print_modifiers(self.character.all_skills["History"]),
            "Insight": text_printer.print_modifiers(self.character.all_skills["Insight"]),
            "Intimidation": text_printer.print_modifiers(self.character.all_skills["Intimidation"]),
            "Investigation": text_printer.print_modifiers(self.character.all_skills["Investigation"]),
            "Medicine": text_printer.print_modifiers(self.character.all_skills["Medicine"]),
            "Nature": text_printer.print_modifiers(self.character.all_skills["Nature"]),
            "Perception": text_printer.print_modifiers(self.character.all_skills["Perception"]),
            "Performance": text_printer.print_modifiers(self.character.all_skills["Performance"]),
            "Persuasion": text_printer.print_modifiers(self.character.all_skills["Persuasion"]),
            "Religion": text_printer.print_modifiers(self.character.all_skills["Religion"]),
            "SleightofHand": text_printer.print_modifiers(self.character.all_skills["Sleight of Hand"]),
            "Stealth": text_printer.print_modifiers(self.character.all_skills["Stealth"]),
            "Survival": text_printer.print_modifiers(self.character.all_skills["Survival"])
        }
        return key_pairs

    def generate_skill_prof_key_pairs(self) -> dict:
        """ Generate key pairs for the character sheet. """
        key_pairs = {
            "Acrobaticsprof": self.check_proficiency("Acrobatics"),
            "AnimalHandlingprof": self.check_proficiency("Animal Handling"),
            "Arcanaprof": self.check_proficiency("Arcana"),
            "Athleticsprof": self.check_proficiency("Athletics"),
            "Deceptionprof": self.check_proficiency("Deception"),
            "Historyprof": self.check_proficiency("History"),
            "Insightprof": self.check_proficiency("Insight"),
            "Intimidationprof": self.check_proficiency("Intimidation"),
            "Investigationprof": self.check_proficiency("Investigation"),
            "Medicineprof": self.check_proficiency("Medicine"),
            "Natureprof": self.check_proficiency("Nature"),
            "Perceptionprof": self.check_proficiency("Perception"),
            "Performanceprof": self.check_proficiency("Performance"),
            "Persuasionprof": self.check_proficiency("Persuasion"),
            "Religionprof": self.check_proficiency("Religion"),
            "SleightofHandprof": self.check_proficiency("Sleight of Hand"),
            "Stealthprof": self.check_proficiency("Stealth"),
            "Survivalprof": self.check_proficiency("Survival")
        }

        return key_pairs

    def check_proficiency(self, skill: str) -> bool:
        """ Check if the character is proficient in the skill. """
        if skill in self.character.skill_proficiencies:
            return "checked"
        return ""
