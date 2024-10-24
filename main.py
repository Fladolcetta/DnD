""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, render_template, request, redirect
from src.race import Race
from src.character_class import CharacterClass
from src.page_loader import PageLoader

app = Flask(__name__)


@app.route('/')
def main() -> str:
    """ Main function. """
    return redirect('roll')


@app.route('/roll')
def roll() -> str:
    """ Roll function. """
    page_loader = PageLoader()
    return page_loader.load_roll(request.args.to_dict())


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
    return page_loader.load_races(request.args.to_dict())


@app.route('/classes')
def classes() -> str:
    """ List Classes """
    page_loader = PageLoader()
    return page_loader.load_classes(request.args.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
