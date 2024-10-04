""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask
from src.character import Character
from src.text_printer import TextPrinter

app = Flask(__name__)

#Character TODOs
#TODO: List Classes
#TODO: List Races
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
    return "Welcome to the Dungeons and Dragons character generator!"

@app.route('/roll')
def roll():
    """ Roll function. """
    text_printer = TextPrinter()
    return text_printer.print_roll(1,20,2)

@app.route('/character')
def character():
    """ Character function. """
    frank = Character("Frank", "Elves")
    text_printer = TextPrinter()
    return text_printer.print_character(frank)

if __name__ == '__main__':
    app.run(debug=True)
