""" Main file for the Dungeons and Dragons character generator. """
from flask import Flask, request, redirect, jsonify
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


@app.route('/character_sheet')
def rolled_character() -> str:
    """ Character function. """
    page_loader = PageLoader()
    return page_loader.load_create_character(request.args.to_dict())


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


@app.route('/table')
def table() -> str:
    """ Display characters function. """
    page_loader = PageLoader()
    return page_loader.load_table()


@app.route('/load_character')
def character() -> str:
    """ Character function. """
    page_loader = PageLoader()
    return page_loader.load_old_character_sheet(request.args.to_dict())


@app.route('/roll_check', methods=['POST'])
def roll_check() -> str:
    """ Roll Check function. """
    data = request.get_json()
    char_id = int(data["char_id"])
    page_loader = PageLoader()
    char = page_loader.load_old_character(char_id)
    check_type = data["check_type"]
    check = data["check"]
    result = char.roll_check(check_type, check)
    return jsonify(result=str(result))


if __name__ == '__main__':
    app.run(debug=True)
