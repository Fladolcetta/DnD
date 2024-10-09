""" A module for printing text to the console. """
from src.dice import Dice
from src.character import Character
from src.race import Race
from src.character_class import CharacterClass

class TextPrinter:
    """ A class to print text to the console. """

    def __init__(self):
        self.text_to_print = ""

    def update_text_to_print(self, text):
        """ Print the text. """
        self.text_to_print += text + "\n"

    def split_string(self, string):
        """ Split the string. """
        string_array = string.split("\n")
        html_string = ""
        for string in string_array:
            html_string += f"<p>{string}</p>"
        return html_string

    def header(self, title):
        """ Print the header. """
        self.update_text_to_print(f"<h1>{title}</h1>")

    def subheader(self, title):
        """ Print the subheader. """
        self.update_text_to_print(f"<h2>{title}</h2>")

    def bolded(self, text):
        """ Print the text in bold. """
        self.update_text_to_print(f"<b>{text}</b>")

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
                self.update_text_to_print(f" - {value}")

    def print_links(self, links):
        """ Print the links. """
        for key, value in links.items():
            self.update_text_to_print(f"<a href='{value}'>{key}</a>")

    def print_single_value(self, value, title):
        """ Print a single value. """
        self.update_text_to_print(f"<b>{title}</b>: {value}")

    def print_dict_with_modifiers(self, data, title):
        """ Print the dictionary with modifiers. """
        if data:
            sorted_data = self.sort_dict(data)
            self.bolded(f"{title}:")
            for key, value in sorted_data.items():
                self.update_text_to_print(f" - {key}: {self.print_modifiers(value)}")

    def print_dict_with_data_and_modifiers(self, data, title):
        """ Print the dictionary with data and modifiers. """
        if data:
            sorted_data = self.sort_dict(data)

            self.bolded(f"{title}:")
            for key, value in sorted_data.items():
                self.update_text_to_print(f" - {key}: {value} ({self.print_modifiers(Character.find_modifier_value(value))})")

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
        self.subheader(f"Creating a new character: {character.name}")

        self.print_single_value(character.name, "Name")
        self.print_single_value(character.race, "Race")
        self.print_single_value(character.dnd_class, "Class")
        self.print_single_value(character.level, "Level")
        self.print_single_value(character.hp, "HP")
        self.print_single_value(character.ac, "AC")
        self.print_single_value(character.initiative, "Initiative")
        self.print_single_value(character.proficiency_bonus, "Proficiency Bonus")
        self.print_single_value(character.passive_perception, "Passive Perception")
        self.print_single_value(character.hit_die, "Hit Die")
        self.print_single_value(character.speed, "Speed")
        self.print_data(character.languages, "Languages")
        self.print_data(character.traits, "Traits")
        self.print_data(character.proficiencies, "Proficiencies")
        self.print_dict_with_data_and_modifiers(character.stats, "Stats")
        self.print_dict_with_modifiers(character.all_skills, "Skills")
        self.print_dict_with_modifiers(character.saving_throws, "Saving Throws")
        return self.split_string(self.text_to_print)

    def print_race_info(self, race_name):
        """ Print the list of races. """
        current_race = Race(race_name)
        self.subheader(f"{current_race.name}")
        self.print_dict_with_modifiers(current_race.stats, "Stats")
        self.print_data(current_race.traits, "Traits")
        self.print_data(current_race.languages, "Languages")
        self.print_single_value(current_race.speed, "Speed")
        return self.split_string(self.text_to_print)

    def print_class_info(self, class_name):
        """ Print the list of classes. """
        current_class = CharacterClass(class_name)
        self.subheader(f"{current_class.name}")
        self.print_data(current_class.primary_stat, "Primary Stat")
        #self.print_single_value(current_class.hit_die, "Hit Die")
        self.print_data(current_class.skill_proficiencies, "Skill Proficiencies")
        self.print_data(current_class.saving_throws_proficiencies, "Saving Throw Proficiencies")
        return self.split_string(self.text_to_print)

    def print_roll(self, num_dice, num_sides, modifier):
        """ Print the roll of the dice. """
        die = Dice(num_dice, num_sides, modifier)
        total_dice, rolls = die.roll()
        if modifier >= 0:
            modifier_string = f" + {modifier}"
        elif modifier < 0:
            modifier_string = f" - {abs(modifier)}"
        self.subheader(f"Rolling {num_dice}d{num_sides}{modifier_string}")
        self.print_single_value(total_dice, "Result")
        self.print_data(die.rolls, "Individual Rolls")
        if die.critical_success:
            self.update_text_to_print("Critical Success!")
        if die.critical_fail:
            self.update_text_to_print("Critical Fail!")
        return self.split_string(self.text_to_print)

    def print_home(self, links):
        """ Print the home page. """
        self.header("Frank's DnD Tool!")
        self.print_links(links)
        return self.split_string(self.text_to_print)