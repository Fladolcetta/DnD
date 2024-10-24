""" A module to load html pages. """
from flask import render_template
from src.character import Character
from src.sheet_generator import SheetGenerator
from src.db import DB
from src.text_printer import TextPrinter


class PageLoader:
    """ A class to load html pages. """
    def __init__(self) -> None:
        pass

    def load_left_right_page(self, left_content: str = "", right_content: str = "", subtitle: str = "") -> str:
        """ Load the page. """
        other_styles = "<link rel='stylesheet' type='text/css' href= '/static/left_right_split.css'>"
        content = render_template('left_right_split_body.html',
                                  left_content=left_content,
                                  right_content=right_content)
        return render_template('base.html',
                               subtitle=subtitle,
                               content=content,
                               other_styles=other_styles)

    def load_left_only_page(self, left_content: str = "", subtitle: str = "") -> str:
        """ Load the page. """
        other_styles = "<link rel='stylesheet' type='text/css' href= '/static/left_only.css'>"
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
        other_styles = "<link rel='stylesheet' type='text/css' href= '/static/sheet.css'>"
        other_scripts = "<script  type='text/javascript' src='/static/sheet.js'></script>"
        return render_template('base.html',
                               subtitle="Character Sheet",
                               content=content,
                               other_styles=other_styles,
                               other_scripts=other_scripts)
