"""Test the Character class"""
from unittest.mock import patch, MagicMock
import pytest
from src.character import Character


@pytest.fixture(name="_mock_dice")
def fixture_mock_dice():
    """ Mock the Dice class """
    with patch('src.character.Dice') as mock_dice_object:
        instance = mock_dice_object.return_value
        instance.total = 14
        instance.rolls = [3, 3, 4, 4]
        yield mock_dice_object


@pytest.fixture(name="_mock_race")
def fixture_mock_race():
    """ Mock the race class """
    with patch('src.character.Race') as mock_race_object:
        instance = mock_race_object.return_value
        instance.speed = 30
        instance.languages = ["Common", "Elvish"]
        instance.traits = ["Darkvision", "Keen Senses"]
        instance.stats = {"Dexterity": 2, "Intelligence": 1}
        yield mock_race_object


@pytest.fixture(name="_mock_character_class")
def fixture_mock_character_class():
    """Mock the CharacterClass class"""
    with patch('src.character.CharacterClass') as mock_character_class_object:
        instance = mock_character_class_object.return_value
        instance.get_primary_stat.return_value = ["Dexterity"]
        instance.get_worst_stat.return_value = ["Strength"]
        instance.hit_die = 10
        instance.get_skill_proficiencies.return_value = ["Acrobatics", "Perception"]
        instance.get_saving_throw_proficiencies.return_value = ["Dexterity"]
        yield mock_character_class_object


def test_character_initialization(_mock_dice, _mock_race, _mock_character_class):
    """Test the initialization of the Character class"""
    # _mock_dice, _mock_race, and _mock_character_class are fixtures
    character = Character()
    character.new_character("Aragorn", "Elf", "Ranger")
    assert character.name == "Aragorn"
    assert character.race == "Elf"
    assert character.dnd_class == "Ranger"
    assert character.level == 1
    assert character.ac == 11  # 10 + Dexterity modifier (1)
    assert character.initiative == 1  # Dexterity modifier
    assert character.hp == 14  # Mocked Dice total
    assert character.passive_perception == 12  # 10 + Wisdom modifier (0) + proficiency bonus (2)
    assert character.speed == 30
    assert character.languages == ["Common", "Elvish"]
    assert character.traits == ["Darkvision", "Keen Senses"]
    assert character.stats["Dexterity"] == 13  # Base 11 + Race bonus 2
    assert character.stats["Strength"] == 11  # Base 11
    assert character.all_skills["Acrobatics"] == 3  # Dexterity modifier (1) + proficiency bonus (2)


def test_find_modifier_value():
    """Test the find_modifier_value method"""
    assert Character.find_modifier_value(10) == 0
    assert Character.find_modifier_value(12) == 1
    assert Character.find_modifier_value(8) == -1


@patch('src.character.DB')
def test_store_character_in_db(mock_db):
    """Test the store_character_in_db method"""
    mock_db.return_value = MagicMock()
    mock_db.return_value.insert_character.return_value = 42
    character = Character()
    character.new_character("Aragorn", "Elf", "Ranger")
    character.store_character_in_db()
    assert character.char_id == 42


@patch('src.character.DB')
def test_load_character_from_db(mock_db):
    """Test the load_character_from_db method"""
    test_name = "Test Character"
    test_id = 1
    mock_db.return_value = MagicMock()
    mock_db.return_value.load_character.return_value = {"id": test_id,
                                                        "name": test_name,
                                                        "dnd_class": "Wizard",
                                                        "race": "Human",
                                                        "stats": {
                                                            "Dexterity": 11,
                                                            "Strength": 12,
                                                            "Constitution": 13,
                                                            "Intelligence": 14,
                                                            "Wisdom": 15,
                                                            "Charisma": 16}}
    character = Character()
    character.load_character_from_db(1)
    assert character.name == test_name
