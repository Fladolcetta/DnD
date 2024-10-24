""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, render_template, request
from src.text_printer import TextPrinter
from src.race import Race
from src.character_class import CharacterClass
from src.page_loader import PageLoader

app = Flask(__name__)


@app.route('/')
def main() -> str:
    """ Main function. """
    return roll()


@app.route('/roll')
def roll() -> str:
    """ Roll function. """
    text_printer = TextPrinter()
    page_loader = PageLoader()
    num_sides = 6
    num_dice = 1
    modifier = 0
    left_content = render_template('roll.html',
                                   num_sides=num_sides,
                                   num_dice=num_dice,
                                   modifier=modifier)
    right_content = ""
    try:
        if "submit" in request.args.get("submit"):
            num_dice = int(request.args.get("num_dice"))
            num_sides = int(request.args.get("num_sides"))
            modifier = int(request.args.get("modifier"))
            right_content = text_printer.print_roll(num_dice, num_sides, modifier)
            return page_loader.load_left_right_page(left_content, right_content, "Dice Roller")
    except TypeError:
        pass
    return page_loader.load_left_only_page(left_content, "Dice Roller")


@app.route('/character')
def character() -> str:
    """ Character function. """
    page_loader = PageLoader()
    race_list = Race.get_all_races()
    class_list = CharacterClass.get_all_classes()
    left_content = render_template('character.html',
                                   subtitle="Character Generator",
                                   race_list=race_list,
                                   class_list=class_list)
    try:
        if "submit" in request.args.get("submit"):
            name = str(request.args.get("name"))
            race = str(request.args.get("race"))
            character_class = str(request.args.get("character_class"))
            return page_loader.load_sheet(name, race, character_class)
    except TypeError:
        pass
    return page_loader.load_left_only_page(left_content, "Character Generator")


@app.route('/races')
def races() -> str:
    """ List Races """
    page_loader = PageLoader()
    text_printer = TextPrinter()
    race_list = Race.get_all_races()
    left_content = render_template('race.html',
                                   race_list=race_list)
    right_content = ""
    try:
        if "submit" in request.args.get("submit"):
            right_content = text_printer.print_race_info(request.args.get("race"))
            return page_loader.load_left_right_page(left_content, right_content, "Race Info")
    except TypeError:
        pass
    return page_loader.load_left_only_page(left_content, "Race Info")


@app.route('/classes')
def classes() -> str:
    """ List Classes """
    page_loader = PageLoader()
    text_printer = TextPrinter()
    class_list = CharacterClass.get_all_classes()
    left_content = render_template('class.html',
                                   class_list=class_list)
    right_content = ""
    try:
        if "submit" in request.args.get("submit"):
            right_content = text_printer.print_class_info(request.args.get("character_class"))
            return page_loader.load_left_right_page(left_content, right_content, "Class Info")
    except TypeError:
        pass
    return page_loader.load_left_only_page(left_content, "Class Info")


if __name__ == '__main__':
    app.run(debug=True)
