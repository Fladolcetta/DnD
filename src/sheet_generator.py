""" A module for generating a character sheet key_pairs. """
from src.character import Character
from src.text_printer import TextPrinter

class SheetGenerator:
    """ A class to generate a character sheet. """
    def __init__(self, character: Character):
        """ Initialize the SheetGenerator. """
        self.character = character
        self.key_pairs = {}

    def generate_key_pairs(self):
        """ Generate key pairs for the character sheet. """
        text_printer = TextPrinter()
        key_pairs = {
            "charname": self.character.name,
            "race": self.character.race,
            "classlevel": self.character.dnd_class + " " + str(self.character.level),
            "Strengthscore": self.character.stats["Strength"],
            "Strengthmod": text_printer.print_modifiers(self.character.find_modifier_stat("Strength")),
        }
        return key_pairs
