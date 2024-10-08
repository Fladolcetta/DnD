""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, render_template, request
from src.character import Character
from src.text_printer import TextPrinter
from src.race import Race
from src.character_class import CharacterClass
from src.sheet_generator import SheetGenerator

app = Flask(__name__)


@app.route('/')
def main() -> str:
    """ Main function. """
    text_printer = TextPrinter()
    links = {
        "Roll": "/roll",
        "Character": "/character",
        "Race List": "/races",
        "Class List": "/classes",
        "Character Sheet": "/sheet"
    }

    content = text_printer.print_home(links)
    return render_template('blank.html', subtitle="Home", content=content)


@app.route('/roll')
def roll() -> str:
    """ Roll function. """
    text_printer = TextPrinter()

    content = ""
    num_sides = 6
    num_dice = 1
    modifier = 0

    try:
        if "Roll" in request.args.get("roll"):
            num_dice = int(request.args.get("num_dice"))
            num_sides = int(request.args.get("num_sides"))
            modifier = int(request.args.get("modifier"))
            content = text_printer.print_roll(num_dice, num_sides, modifier)
    except TypeError:
        pass

    return render_template('roll.html',
                           subtitle="Dice Roller",
                           num_sides=num_sides,
                           num_dice=num_dice,
                           modifier=modifier,
                           content=content)


@app.route('/character')
def character() -> str:
    """ Character function. """
    text_printer = TextPrinter()

    race_list = Race.get_all_races()
    class_list = CharacterClass.get_all_classes()

    try:
        if "Create" in request.args.get("create"):
            name = str(request.args.get("name"))
            race = str(request.args.get("race"))
            character_class = str(request.args.get("character_class"))
            new_char = Character(name, race, character_class)

            key_pairs = SheetGenerator(new_char).generate_key_pairs()
            details = text_printer.print_character(new_char)
            basic_info = text_printer.print_basic_stats(new_char)
            return render_template('character_sheet.html',
                                   subtitle="Character Sheet",
                                   key_pairs=key_pairs,
                                   details=details,
                                   basic_info=basic_info)
    except TypeError:
        pass
    return render_template('character.html',
                           subtitle="Character Generator",
                           race_list=race_list,
                           class_list=class_list)


@app.route('/races')
def races() -> str:
    """ List Races """
    text_printer = TextPrinter()
    race_list = Race.get_all_races()
    content = ""
    try:
        if "Show" in request.args.get("show"):
            content = text_printer.print_race_info(request.args.get("race"))
    except TypeError:
        pass
    return render_template('race.html',
                           subtitle="Race List",
                           content=content,
                           race_list=race_list)


@app.route('/classes')
def classes() -> str:
    """ List Classes """
    text_printer = TextPrinter()
    class_list = CharacterClass.get_all_classes()
    content = ""
    try:
        if "Show" in request.args.get("show"):
            content = text_printer.print_class_info(request.args.get("character_class"))
    except TypeError:
        pass
    return render_template('class.html',
                           subtitle="Class List",
                           content=content,
                           class_list=class_list)


@app.route('/sheet')
def sheet() -> str:
    """ Character Sheet """
    text_printer = TextPrinter()
    frank = Character("Frank", "Human", "Fighter")
    key_pairs = SheetGenerator(frank).generate_key_pairs()
    details = text_printer.print_character(frank)
    basic_info = text_printer.print_basic_stats(frank)

    return render_template('character_sheet.html',
                           subtitle="Character Sheet",
                           key_pairs=key_pairs,
                           details=details,
                           basic_info=basic_info)


if __name__ == '__main__':
    app.run(debug=True)
