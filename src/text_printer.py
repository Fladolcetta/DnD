""" A module for printing text to the console. """
from src.dice import Dice
from src.character import Character

# pylint: disable=line-too-long
class TextPrinter:
    """ A class to print text to the console. """
    def print_roll(self, num_dice, num_sides, modifier):
        """ Print the roll of the dice. """

        die = Dice(num_dice, num_sides, modifier)
        total_dice, rolls = die.roll()
        print(f"Total Dice: {total_dice}")
        print(f"Rolls: {rolls}")
        if die.critical_success:
            print("Critical Success!")
        if die.critical_fail:
            print("Critical Fail!")

    def list_to_dict(self, list_object):
        """ Convert a list to a dictionary. """
        dict_object = {}
        for i, value in enumerate(list_object):
            dict_object[i] = value

        return dict_object

    def sort_dict(self, dict_object):
        """ Sort the dictionary. """
        return dict(sorted(dict_object.items()))

    def print_data(self, data, title):
        """ Print the dictionary. """

        if data:
            if isinstance(data, list):
                data = self.list_to_dict(data)

            sorted_data = self.sort_dict(data)

            print(f"{title}:")
            for _, value in sorted_data.items():
                print(f" - {value}")

    def print_dict_with_modifiers(self, data, title):
        """ Print the dictionary with modifiers. """
        if data:
            sorted_data = self.sort_dict(data)

            print(f"{title}:")
            for key, value in sorted_data.items():
                print(f" - {key}: {self.print_modifiers(value)}")

    def print_dict_with_data_and_modifiers(self, data, title):
        """ Print the dictionary with data and modifiers. """
        if data:
            sorted_data = self.sort_dict(data)

            print(f"{title}:")
            for key, value in sorted_data.items():
                print(f" - {key}: {value} ({self.print_modifiers(Character.find_modifier_value(value))})")

    def print_modifiers(self, value):
        """ Print the modifiers of the value. """
        printed_value = ""
        if value >= 0:
            printed_value = f"+{value}"
        else:
            printed_value = f"{value}"
        return printed_value

    def print_character(self, character):
        """ Print the character. """
        print(f"Name: {character.name}")
        print(f"Race: {character.race}")
        print(f"Class: {character.dnd_class}")
        print(f"Hit Die: {character.hit_die}")
        print(f"Speed: {character.speed}")
        self.print_data(character.languages, "Languages")
        self.print_data(character.traits, "Traist")
        self.print_data(character.proficiencies, "Proficiencies")
        self.print_dict_with_data_and_modifiers(character.stats, "Stats")
        self.print_dict_with_modifiers(character.all_skills, "Skills")
        self.print_dict_with_modifiers(character.saving_throws, "Saving Throws")
