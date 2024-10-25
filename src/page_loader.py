""" A module to load html pages. """
from typing import Union
from flask import render_template
from src.db import DB
from src.race import Race
from src.character import Character
from src.text_printer import TextPrinter
from src.sheet_generator import SheetGenerator
from src.character_class import CharacterClass


class PageLoader:
    """ A class to load html pages. """
    def __init__(self) -> None:
        pass

    def load_left_right_page(self, left_content: str = "", right_content: str = "", subtitle: str = "") -> str:
        """ Load the page. """
        other_styles = self.build_styles_string(['left_and_container', 'right_only', 'inputs'])
        content = render_template('left_right_split_body.html',
                                  left_content=left_content,
                                  right_content=right_content)
        return render_template('base.html',
                               subtitle=subtitle,
                               content=content,
                               other_styles=other_styles)

    def load_left_only_page(self, left_content: str = "", subtitle: str = "") -> str:
        """ Load the page. """
        other_styles = self.build_styles_string(['left_and_container', 'inputs'])
        content = render_template('left_only_body.html',
                                  left_content=left_content)
        return render_template('base.html',
                               subtitle=subtitle,
                               content=content,
                               other_styles=other_styles)

    def load_sheet(self, name: str, race: str, character_class: str) -> str:
        """ Load the character sheet. """
        text_printer = TextPrinter()
        new_char = Character(name, race, character_class)
        db = DB()
        char_id = db.insert_character(new_char)
        key_pairs = SheetGenerator(new_char).generate_key_pairs()
        details = text_printer.print_character(new_char)
        basic_info = text_printer.print_basic_stats(new_char)
        content = render_template('character_sheet.html',
                                  subtitle="Character Sheet",
                                  char_id=char_id,
                                  key_pairs=key_pairs,
                                  details=details,
                                  basic_info=basic_info)
        other_styles = self.build_styles_string(['sheet'])
        other_scripts = self.build_script_string(['sheet'])
        return render_template('base.html',
                               subtitle="Character Sheet",
                               content=content,
                               other_styles=other_styles,
                               other_scripts=other_scripts)

    def load_roll(self, args: dict) -> str:
        """ Load the roll page. """
        text_printer = TextPrinter()
        num_sides = int(args.get("num_sides") or 6)
        num_dice = int(args.get("num_dice") or 1)
        modifier = int(args.get("modifier") or 0)
        left_content = render_template('roll.html',
                                       num_sides=num_sides,
                                       num_dice=num_dice,
                                       modifier=modifier)
        right_content = text_printer.print_roll(num_dice, num_sides, modifier)
        submit = args.get("submit")
        return self.left_right_dance(submit, left_content, right_content, "Dice Roller")

    def load_races(self, args: dict) -> str:
        """ Load the races page. """
        text_printer = TextPrinter()
        race_list = Race.get_all_races()
        race = args.get("race") or "Human"
        left_content = render_template('race.html',
                                       race_list=race_list)
        right_content = text_printer.print_race_info(race)
        submit = args.get("submit")
        return self.left_right_dance(submit, left_content, right_content, "Race Info")

    def load_classes(self, args: dict) -> str:
        """ Load the classes page. """
        text_printer = TextPrinter()
        class_list = CharacterClass.get_all_classes()
        character_class = args.get("character_class") or "Barbarian"
        left_content = render_template('class.html',
                                       class_list=class_list)
        right_content = text_printer.print_class_info(character_class)
        submit = args.get("submit")
        return self.left_right_dance(submit, left_content, right_content, "Class Info")

    def left_right_dance(self, submit: Union[None, str], left_content: str, right_content: str, subtitle: str) -> str:
        """ Load the left right page. """
        try:
            if "submit" in submit:
                return self.load_left_right_page(left_content, right_content, subtitle)
        except TypeError:
            pass
        return self.load_left_only_page(left_content, subtitle)

    def load_character(self, args: dict) -> str:
        """ Load the sheet page. """
        race_list = Race.get_all_races()
        class_list = CharacterClass.get_all_classes()
        left_content = render_template('character.html',
                                       subtitle="Character Generator",
                                       race_list=race_list,
                                       class_list=class_list)
        try:
            if "submit" in args.get("submit"):
                name = str(args.get("name"))
                race = str(args.get("race"))
                character_class = str(args.get("character_class"))
                return self.load_sheet(name, race, character_class)
        except TypeError:
            pass
        return self.load_left_only_page(left_content, "Character Generator")

    def build_script_string(self, script_list: list) -> str:
        """ Build a string of script tags. """
        script_string = ""
        for script in script_list:
            script_string += f"        <script  type='text/javascript' src='/static/{script}.js'></script>\n"
        return script_string

    def build_styles_string(self, styles_list: list) -> str:
        """ Build a string of style tags. """
        styles_string = ""
        for style in styles_list:
            styles_string += f"        <link rel='stylesheet' type='text/css' href='/static/{style}.css'>\n"
        return styles_string
