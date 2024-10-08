""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, render_template, request
from src.character import Character
from src.text_printer import TextPrinter

app = Flask(__name__)

#Character TODOs
#TODO: Make selectable classes and races

#Repo TODOS
#TODO: Add Unit Tests
#TODO: Add Linting
#TODO: Generate Documentation
#TODO: Update README with generated documentation
#TODO: Add Code Coverage
#TODO: Add Kubernetes
#TODO: Update branch rules to require PRs

@app.route('/')
def main():
    """ Main function. """
    text_printer = TextPrinter()
    links = {
        "Roll": "/roll",
        "Character": "/character",
        "Race List": "/races",
        "Class List": "/classes"
    }

    content = text_printer.print_home(links)
    return render_template('blank.html', subtitle="Home", content=content)

@app.route('/roll')
def roll():
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
def character():
    """ Character function. """
    text_printer = TextPrinter()

    content = ""
    name = ""
    race = ""
    character_class = ""


    try:
        if "Create" in request.args.get("create"):
            name = str(request.args.get("name"))
            race = str(request.args.get("race"))
            character_class = str(request.args.get("character_class"))
            new_char = Character(name, race, character_class)

            content = text_printer.print_character(new_char)
    except TypeError:
        pass
    return render_template('character.html',
                            subtitle="Character Generator",
                            name=name,
                            race=race,
                            character_class=character_class,
                            content=content)

@app.route('/races')
def races():
    """ List Races """
    text_printer = TextPrinter()

    content = text_printer.print_races()
    return render_template('blank.html', subtitle="Race List", content=content)

@app.route('/classes')
def classes():
    """ List Classes """
    text_printer = TextPrinter()

    content = text_printer.print_classes()
    return render_template('blank.html', subtitle="Class List", content=content)

if __name__ == '__main__':
    app.run(debug=True)
