""" A module for printing text to the console. """
import sys
from io import StringIO
from src.dice import Dice
from src.character import Character
from src.race import Race

sys.stdout = buffer = StringIO()
class TextPrinter:
    """ A class to print text to the console. """

    def split_string(self, string):
        """ Split the string. """
        string_array = string.split("\n")

        html_string = ""
        for string in string_array:
            html_string += f"{string}<br>"
        return html_string

    def header(self, title):
        """ Print the header. """
        print(f"<h1>{title}</h1>")

    def bolded(self, text):
        """ Print the text in bold. """
        print(f"<b>{text}</b>")

    def print_roll(self, num_dice, num_sides, modifier):
        """ Print the roll of the dice. """
        buffer.truncate(0)

        die = Dice(num_dice, num_sides, modifier)
        total_dice, rolls = die.roll()
        self.header("Dice Roller")
        self.bolded(f"Rolling {num_dice}d{num_sides} + {modifier}")
        self.bolded("Result:")
        print(f"- {total_dice}")
        self.bolded("Individual Rolls:")
        print(f"- {rolls}")
        if die.critical_success:
            print("Critical Success!")
        if die.critical_fail:
            print("Critical Fail!")

        return self.split_string(buffer.getvalue())

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

            self.bolded(f"{title}:")
            for _, value in sorted_data.items():
                print(f" - {value}")

    def print_dict_with_modifiers(self, data, title):
        """ Print the dictionary with modifiers. """
        if data:
            sorted_data = self.sort_dict(data)

            self.bolded(f"{title}:")
            for key, value in sorted_data.items():
                print(f" - {key}: {self.print_modifiers(value)}")

    def print_dict_with_data_and_modifiers(self, data, title):
        """ Print the dictionary with data and modifiers. """
        if data:
            sorted_data = self.sort_dict(data)

            self.bolded(f"{title}:")
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
        buffer.truncate(0)

        self.header(f"Character Generator")
        self.bolded("Name:")
        print(f"- {character.name}")
        self.bolded("Race:")
        print(f"- {character.race}")
        self.bolded("Class:")
        print(f"- {character.dnd_class}")
        self.bolded("Hit Die:")
        print(f"- {character.hit_die}")
        self.bolded("Speed:")
        print(f"- {character.speed}")
        self.print_data(character.languages, "Languages")
        self.print_data(character.traits, "Traist")
        self.print_data(character.proficiencies, "Proficiencies")
        self.print_dict_with_data_and_modifiers(character.stats, "Stats")
        self.print_dict_with_modifiers(character.all_skills, "Skills")
        self.print_dict_with_modifiers(character.saving_throws, "Saving Throws")
        return self.split_string(buffer.getvalue())

    def print_races(self):
        """ Print the list of races. """
        buffer.truncate(0)
        race_list = Race.get_all_races()

        self.bolded("Race List:")
        for race in race_list:
            print (f"- {race}")

        return self.split_string(buffer.getvalue())
