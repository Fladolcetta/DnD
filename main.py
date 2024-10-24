""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, request, redirect
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
    return page_loader.load_character(request.args.to_dict())


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
