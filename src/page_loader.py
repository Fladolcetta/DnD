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
        other_styles = self.build_styles_string(['container', 'left_and_right', 'inputs'])
        content = render_template('left_right_split_body.html',
                                  left_content=left_content,
                                  right_content=right_content)
        return render_template('base.html',
                               subtitle=subtitle,
                               content=content,
                               other_styles=other_styles)

    def load_left_only_page(self, left_content: str = "", subtitle: str = "", styles: list = None, scripts: list = None) -> str:
        """ Load the page. """
        if styles is None:
            styles = []
        if scripts is None:
            scripts = []
        other_styles = self.build_styles_string(['container', 'inputs'] + styles)
        other_scripts = self.build_script_string(scripts)
        content = render_template('left_only_body.html',
                                  left_content=left_content)
        return render_template('base.html',
                               subtitle=subtitle,
                               content=content,
                               other_styles=other_styles,
                               other_scripts=other_scripts)

    def display_char(self, char: Character) -> str:
        """ Display the character sheet. """
        text_printer = TextPrinter()
        key_pairs = SheetGenerator(char).generate_key_pairs()
        details = text_printer.print_character(char)
        basic_info = text_printer.print_basic_stats(char)
        char_id = char.char_id
        content = render_template('character_sheet.html',
                                  subtitle="Character Sheet",
                                  char_id=char_id,
                                  key_pairs=key_pairs,
                                  details=details,
                                  basic_info=basic_info)
        other_styles = self.build_styles_string(['sheet'])
        other_scripts = self.build_script_string(['sheet', 'roll_check'])
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

    def load_table(self) -> str:
        """ Load the table page. """
        db = DB()
        char_list = db.load_character_list()
        left_content = render_template('character_table.html', char_list=char_list)
        content = render_template('left_only_body.html',
                                  left_content=left_content)
        other_styles = self.build_styles_string(['container', 'table'])
        other_scripts = ""
        return render_template('base.html',
                               subtitle="Character Table",
                               content=content,
                               other_styles=other_styles,
                               other_scripts=other_scripts)

    def left_right_dance(self, submit: Union[None, str], left_content: str, right_content: str, subtitle: str) -> str:
        """ Load the left right page. """
        try:
            if "submit" in submit:
                pass
        except TypeError:
            right_content = ""
        return self.load_left_right_page(left_content, right_content, subtitle)

    def load_create_character(self, args: dict) -> str:
        """ Load the sheet page. """
        race_list = Race.get_all_races()
        class_list = CharacterClass.get_all_classes()
        left_content = render_template('create.html',
                                       subtitle="Character Generator",
                                       race_list=race_list,
                                       class_list=class_list)
        try:
            if "submit" in args.get("submit"):
                name = str(args.get("name"))
                race = str(args.get("race"))
                character_class = str(args.get("character_class"))
                new_char = Character()
                new_char.new_character(name, race, character_class)
                new_char.store_character_in_db()

                return self.display_char(new_char)
        except TypeError:
            pass
        return self.load_left_only_page(left_content, "Character Generator", scripts=['create'])

    def load_old_character(self, char_id: int) -> Character:
        """ Load the sheet page. """
        char = Character()
        char.load_character_from_db(char_id)
        return char

    def load_old_character_sheet(self, args: dict) -> str:
        """ Load the sheet page. """
        char_id = int(args.get("char_id") or 1)
        char = self.load_old_character(char_id)
        return self.display_char(char)

    def build_script_string(self, script_list: list) -> str:
        """ Build a string of script tags. """
        script_string = "\n".join(
            f"        <script type='text/javascript' src='/static/{script}.js'></script>"
            for script in script_list
        )
        return script_string + "\n" if script_list else ""

    def build_styles_string(self, styles_list: list) -> str:
        """ Build a string of style tags. """
        styles_string = "\n".join(
            f"    <link rel='stylesheet' type='text/css' href='/static/{style}.css'>"
            for style in styles_list
        )
        return styles_string + "\n" if styles_list else ""
