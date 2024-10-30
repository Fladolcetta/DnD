""" Tests for the PageLoader class. """
from unittest.mock import patch, call, Mock
from src.page_loader import PageLoader
from src.character import Character


@patch('src.page_loader.render_template')
def test_load_left_right_page(mock_render_template):
    """ Test the load_left_right_page method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    page_loader = PageLoader()

    result = page_loader.load_left_right_page("left", "right", "Subtitle")

    calls = [call('left_right_split_body.html', left_content="left", right_content="right"),
             call('base.html', subtitle="Subtitle", content="<html>Mocked HTML</html>", other_styles="    <link rel='stylesheet' type='text/css' href='/static/left_and_container.css'>\n    <link rel='stylesheet' type='text/css' href='/static/right_only.css'>\n    <link rel='stylesheet' type='text/css' href='/static/inputs.css'>\n")]
    mock_render_template.assert_has_calls(calls)
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
def test_load_left_only_page(mock_render_template):
    """ Test the load_left_only_page method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    page_loader = PageLoader()

    result = page_loader.load_left_only_page("left", "Subtitle")

    calls = [call('left_only_body.html', left_content="left"),
             call('base.html', subtitle="Subtitle", content="<html>Mocked HTML</html>", other_styles="    <link rel='stylesheet' type='text/css' href='/static/left_and_container.css'>\n    <link rel='stylesheet' type='text/css' href='/static/inputs.css'>\n")]
    mock_render_template.assert_has_calls(calls)
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
@patch('src.page_loader.TextPrinter')
@patch('src.page_loader.SheetGenerator')
def test_display_char(mock_sheet_generator, mock_text_printer, mock_render_template):
    """ Test the display_char method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    mock_sheet_generator.return_value.generate_key_pairs.return_value = {}
    mock_text_printer.return_value.print_character.return_value = "Character Details"
    mock_text_printer.return_value.print_basic_stats.return_value = "Basic Stats"

    page_loader = PageLoader()
    test_char = Character()
    test_char.new_character("Name", "Human", "Bard")
    result = page_loader.display_char(test_char)

    calls = [call('character_sheet.html', subtitle="Character Sheet", char_id=None, key_pairs={}, details="Character Details", basic_info="Basic Stats"),
             call('base.html', subtitle="Character Sheet", content="<html>Mocked HTML</html>", other_styles="    <link rel='stylesheet' type='text/css' href='/static/sheet.css'>\n", other_scripts="        <script type='text/javascript' src='/static/sheet.js'></script>\n")]
    mock_render_template.assert_has_calls(calls)

    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
@patch('src.page_loader.TextPrinter')
def test_load_roll(mock_text_printer, mock_render_template):
    """ Test the load_roll method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    mock_text_printer.return_value.print_roll.return_value = "Roll Result"

    page_loader = PageLoader()
    args = {"num_sides": "6", "num_dice": "2", "modifier": "1", "submit": "submit"}

    result = page_loader.load_roll(args)

    mock_render_template.assert_any_call('roll.html', num_sides=6, num_dice=2, modifier=1)
    mock_text_printer.return_value.print_roll.assert_called_once_with(2, 6, 1)
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
@patch('src.page_loader.TextPrinter')
@patch('src.page_loader.Race')
def test_load_races(mock_race, mock_text_printer, mock_render_template):
    """ Test the load_races method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    mock_race.get_all_races.return_value = ["Human", "Elf"]
    mock_text_printer.return_value.print_race_info.return_value = "Race Info"

    page_loader = PageLoader()
    args = {"race": "Elf", "submit": "submit"}

    result = page_loader.load_races(args)

    mock_render_template.assert_any_call('race.html', race_list=["Human", "Elf"])
    mock_text_printer.return_value.print_race_info.assert_called_once_with("Elf")
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
@patch('src.page_loader.TextPrinter')
@patch('src.page_loader.CharacterClass')
def test_load_classes(mock_character_class, mock_text_printer, mock_render_template):
    """ Test the load_classes method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    mock_character_class.get_all_classes.return_value = ["Barbarian", "Wizard"]
    mock_text_printer.return_value.print_class_info.return_value = "Class Info"

    page_loader = PageLoader()
    args = {"character_class": "Wizard", "submit": "submit"}

    result = page_loader.load_classes(args)

    mock_render_template.assert_any_call('class.html', class_list=["Barbarian", "Wizard"])
    mock_text_printer.return_value.print_class_info.assert_called_once_with("Wizard")
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.render_template')
def test_left_right_dance(mock_render_template):
    """ Test the left_right_dance method. """
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    page_loader = PageLoader()

    # Test with submit
    result = page_loader.left_right_dance("submit", "left", "right", "Subtitle")
    mock_render_template.assert_any_call('left_right_split_body.html', left_content="left", right_content="right")
    assert result == "<html>Mocked HTML</html>"

    # Test without submit
    result = page_loader.left_right_dance(None, "left", "right", "Subtitle")
    mock_render_template.assert_any_call('left_only_body.html', left_content="left")
    assert result == "<html>Mocked HTML</html>"


@patch('src.page_loader.PageLoader.display_char')
@patch('src.page_loader.render_template')
@patch('src.page_loader.Race')
@patch('src.page_loader.CharacterClass')
@patch('src.page_loader.Character')
def test_load_character(mock_character, mock_character_class, mock_race, mock_render_template, mock_display_char):
    """ Test the load_character method. """
    mock_character.return_value = Mock()
    mock_character.new_character.return_value = None
    mock_character.store_character_in_db.return_value = None
    mock_display_char.return_value = "<html>Mocked HTML</html>"
    mock_render_template.return_value = "<html>Mocked HTML</html>"
    mock_race.get_all_races.return_value = ["Human", "Elf"]
    mock_character_class.get_all_classes.return_value = ["Barbarian", "Wizard"]

    page_loader = PageLoader()
    args = {"name": "Hero", "race": "Elf", "character_class": "Wizard", "submit": "submit"}

    result = page_loader.load_character(args)

    mock_render_template.assert_any_call('character.html', subtitle="Character Generator", race_list=["Human", "Elf"], class_list=["Barbarian", "Wizard"])
    assert result == "<html>Mocked HTML</html>"

    # Test without submit
    args = {"name": "Hero", "race": "Elf", "character_class": "Wizard"}
    result = page_loader.load_character(args)
    mock_render_template.assert_any_call('left_only_body.html', left_content="<html>Mocked HTML</html>")
    assert result == "<html>Mocked HTML</html>"
