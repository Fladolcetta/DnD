""" Tests for the TextPrinter class """
from unittest.mock import Mock, patch
from src.text_printer import TextPrinter
from src.character import Character
from src.race import Race
from src.character_class import CharacterClass


def test_text_printer_initialization():
    """ Test the initialization of the TextPrinter class """
    printer = TextPrinter()
    assert printer.text_to_print == ""


def test_update_text_to_print():
    """ Test the update_text_to_print method """
    printer = TextPrinter()
    printer.update_text_to_print("Hello, World!")
    assert printer.text_to_print == "Hello, World!\n"


def test_split_string():
    """ Test the split_string method """
    printer = TextPrinter()
    test_string = "Line 1\nLine 2"
    expected_output = "<p>Line 1</p><p>Line 2</p>"
    assert printer.split_string(test_string) == expected_output


def test_header():
    """ Test the header method """
    printer = TextPrinter()
    printer.header("My Title")
    assert printer.text_to_print == "<h1>My Title</h1>\n"


def test_subheader():
    """ Test the subheader method """
    printer = TextPrinter()
    printer.subheader("Sub Title")
    assert printer.text_to_print == "<h2>Sub Title</h2>\n"


def test_bolded():
    """ Test the bolded method """
    printer = TextPrinter()
    printer.bolded("Important")
    assert printer.text_to_print == "<b>Important</b>\n"


def test_list_to_dict():
    """ Test the list_to_dict method """
    printer = TextPrinter()
    test_list = ["Item 1", "Item 2"]
    expected_output = {0: "Item 1", 1: "Item 2"}
    assert printer.list_to_dict(test_list) == expected_output


def test_sort_dict():
    """ Test the sort_dict method """
    printer = TextPrinter()
    test_dict = {2: "b", 1: "a"}
    expected_output = {1: "a", 2: "b"}
    assert printer.sort_dict(test_dict) == expected_output


def test_print_data():
    """ Test the print_data method """
    printer = TextPrinter()
    test_list = ["Language 1", "Language 2"]
    printer.print_data(test_list, "Languages")
    assert printer.text_to_print == "<b>Languages:</b>\n - Language 1\n - Language 2\n"


def test_print_single_value():
    """ Test the print_single_value method """
    printer = TextPrinter()
    printer.print_single_value("Common", "Language")
    assert printer.text_to_print == "<b>Language</b>: Common\n"


def test_print_dict_with_modifiers():
    """ Test the print_dict_with_modifiers method """
    printer = TextPrinter()
    test_dict = {"Skill1": -2, "Skill2": 3}
    printer.print_dict_with_modifiers(test_dict, "Skills")
    assert printer.text_to_print == "<b>Skills:</b>\n - Skill1: -2\n - Skill2: +3\n"


def test_print_dict_with_data_and_modifiers():
    """ Test the print_dict_with_data_and_modifiers method """
    printer = TextPrinter()
    test_dict = {"Skill1": 6, "Skill2": 16}
    printer.print_dict_with_data_and_modifiers(test_dict, "Skills")
    assert printer.text_to_print == "<b>Skills:</b>\n - Skill1: 6 (-2)\n - Skill2: 16 (+3)\n"


def test_print_modifiers_positive():
    """ Test the print_modifiers method for a positive modifier """
    printer = TextPrinter()
    assert printer.print_modifiers(3) == "+3"


def test_print_modifiers_negative():
    """ Test the print_modifiers method for a negative modifier """
    printer = TextPrinter()
    assert printer.print_modifiers(-2) == "-2"


def test_print_character():
    """ Test the print_character method """
    mock_character = Mock(spec=Character)
    mock_character.name = "Frodo"
    mock_character.race = "Hobbit"
    mock_character.dnd_class = "Rogue"
    mock_character.level = 4
    mock_character.hp = 25
    mock_character.ac = 14
    mock_character.initiative = 2
    mock_character.proficiency_bonus = 2
    mock_character.passive_perception = 10
    mock_character.hit_die = "1d8"
    mock_character.speed = 25
    mock_character.languages = ["Common", "Elvish"]
    mock_character.traits = ["Bravery", "Lucky"]
    mock_character.skill_proficiencies = ["Stealth", "Perception"]
    mock_character.stats = {"Strength": 8, "Dexterity": 16}
    mock_character.all_skills = {"Stealth": 5, "Perception": 2}
    mock_character.saving_throws = {"Dexterity": 5, "Strength": -1}

    printer = TextPrinter()
    result = printer.print_character(mock_character)
    assert "<p><b>Name</b>: Frodo</p>" in result


def test_print_basic_stats():
    """ Test the print_basic_stats method """
    mock_character = Mock(spec=Character)
    mock_character.race = "Hobbit"
    mock_character.dnd_class = "Rogue"
    mock_character.stats = {"Strength": 8, "Dexterity": 16}

    printer = TextPrinter()
    result = printer.print_basic_stats(mock_character)
    assert "<p><b>Race</b>: Hobbit</p>" in result
    assert "<p><b>Class</b>: Rogue</p>" in result
    assert "<p><b>Stats:</b></p><p> - Dexterity: 16 (+3)</p>" in result


def test_print_race_info():
    """ Test the print_race_info method """
    mock_race = Mock(spec=Race)
    mock_race.name = "Elf"
    mock_race.stats = {"Dexterity": 2}
    mock_race.traits = ["Darkvision"]
    mock_race.languages = ["Common", "Elvish"]
    mock_race.speed = 30

    printer = TextPrinter()
    result = printer.print_race_info("Elf")

    assert "<p><h2>Elf</h2></p>" in result
    assert "<p><b>Stats:</b></p><p> - Dexterity: +2</p>" in result


def test_print_class_info():
    """ Test the print_class_info method """
    mock_class = Mock(spec=CharacterClass)
    mock_class.name = "Wizard"
    mock_class.primary_stat = {"Intelligence": 4}
    mock_class.hit_die = 6
    mock_class.skill_proficiencies = ["Arcana", "History"]
    mock_class.saving_throws_proficiencies = ["Intelligence", "Wisdom"]

    printer = TextPrinter()
    result = printer.print_class_info("Wizard")

    assert "<p><h2>Wizard</h2></p>" in result
    assert "<p><b>Hit Die</b>: 6</p>" in result


@patch('src.text_printer.Dice')
def test_print_roll_success(mock_dice):
    """ Test the print_roll method """
    mock_dice.return_value.total = 18
    mock_dice.return_value.rolls = [6, 6, 6]
    mock_dice.return_value.critical_success = True
    mock_dice.return_value.critical_fail = False
    printer = TextPrinter()
    result = printer.print_roll(3, 6, 0)

    assert "<p><b>Total Roll with Modifier</b>: 18</p>" in result
    assert "Critical Success!" in result


@patch('src.text_printer.Dice')
def test_print_roll_fail(mock_dice):
    """ Test the print_roll method """
    mock_dice.return_value.total = 0
    mock_dice.return_value.rolls = [1]
    mock_dice.return_value.critical_success = False
    mock_dice.return_value.critical_fail = True
    printer = TextPrinter()
    result = printer.print_roll(1, 6, -1)

    assert "<p><b>Total Roll with Modifier</b>: 0</p>" in result
    assert "Critical Fail!" in result
