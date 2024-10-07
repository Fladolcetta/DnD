""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, render_template
from src.character import Character
from src.text_printer import TextPrinter

app = Flask(__name__)

#Character TODOs
#TODO: Make selectable classes and races
#TODO: Add name text box
#TODO: Add submit button

#Dice TODOs
#TODO: Add side selector
#TODO: Add number of dice selector
#TODO: Add modifier text box that accepts ints only
#TODO: Add submit button

#Repo TODOS
#TODO: Add Unit Tests
#TODO: Add Linting
#TODO: Generate Documentation
#TODO: Update README with generated documentation
#TODO: Add Code Coverage
#TODO: Add Containerization
#TODO: Add Kubernetes

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

    content = text_printer.print_roll(1,20,2)
    return render_template('blank.html', subtitle="Dice Roller", content=content)

@app.route('/character')
def character():
    """ Character function. """
    frank = Character("Frank", "Elves")
    text_printer = TextPrinter()

    content = text_printer.print_character(frank)
    return render_template('blank.html', subtitle="Character Generator", content=content)

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
