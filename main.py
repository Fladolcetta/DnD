""" Main file for the Dungeons and Dragons character generator. """
from src.character import Character
from src.text_printer import TextPrinter

#Code TODOs
#TODO: List Classes
#TODO: List Races
#TODO: Make APIs
#TODO: Add Web UI

#Repo TODOS
#TODO: Add Unit Tests
#TODO: Add Linting
#TODO: Generate Documentation
#TODO: Update README with generated documentation
#TODO: Add Code Coverage
#TODO: Add Containerization
#TODO: Add Kubernetes


def main():
    """ Main function. """
    frank = Character("Frank", "Elves")
    text_printer = TextPrinter()
    text_printer.print_character(frank)
    text_printer.print_roll(1,20,2)

if __name__ == '__main__':
    main()
