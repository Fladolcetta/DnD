""" This module tests the SheetGenerator class """
import pytest
from src.sheet_generator import SheetGenerator


class MockCharacter:
    """ A mock class to represent a character in Dungeons and Dragons. """
    def __init__(self):
        self.name = "Test Character"
        self.race = "Human"
        self.dnd_class = "Warrior"
        self.level = 5
        self.proficiency_bonus = 2
        self.passive_perception = 10
        self.ac = 15
        self.initiative = 1
        self.speed = 30
        self.hp = 40
        self.hit_die = "5d10"
        self.languages = ["Common", "Elvish"]
        self.traits = ["Brave", "Strong"]
        self.stats = {
            "Strength": 16,
            "Dexterity": 14,
            "Constitution": 15,
            "Wisdom": 12,
            "Intelligence": 10,
            "Charisma": 8
        }
        self.all_skills = {
            "Acrobatics": 2,
            "Animal Handling": 1,
            "Arcana": 0,
            "Athletics": 3,
            "Deception": -1,
            "History": 0,
            "Insight": 1,
            "Intimidation": -1,
            "Investigation": 0,
            "Medicine": 1,
            "Nature": 0,
            "Perception": 1,
            "Performance": -1,
            "Persuasion": -1,
            "Religion": 0,
            "Sleight of Hand": 2,
            "Stealth": 2,
            "Survival": 1
        }
        self.saving_throws = {
            "Strength": 3,
            "Dexterity": 2,
            "Constitution": 2,
            "Wisdom": 1,
            "Intelligence": 0,
            "Charisma": -1
        }
        self.skill_proficiencies = ["Athletics", "Perception"]
        self.save_proficiencies = ["Strength", "Constitution"]

    def find_modifier_stat(self, stat: str) -> int:
        """ Find the modifier for a given stat. """
        stat_value = self.stats[stat]
        return (stat_value - 10) // 2


@pytest.fixture(name="_mock_character")
def fixture_mock_character():
    """ A fixture to return a mock character. """
    return MockCharacter()


@pytest.fixture(name="_sheet_generator")
def fixture_sheet_generator(_mock_character):
    """ A fixture to return a SheetGenerator object. """
    return SheetGenerator(_mock_character)


def test_init():
    """ Test the __init__ method """
    sheet_generator = SheetGenerator(MockCharacter())
    assert sheet_generator.character.name == "Test Character"
    assert sheet_generator.character


def test_generate_key_pairs(_sheet_generator):
    """ Test the generate_key_pairs method """
    # This test will check if the generate_key_pairs method correctly combines all key pairs
    key_pairs = _sheet_generator.generate_key_pairs()
    assert "charname" in key_pairs
    assert "Strengthscore" in key_pairs
    assert "Strengthsave" in key_pairs
    assert "Acrobatics" in key_pairs
    assert "Acrobaticsprof" in key_pairs
    assert "Strengthsaveprof" in key_pairs


def test_generate_basic_key_pairs(_sheet_generator):
    """ Test the generate_basic_key_pairs method """
    expected_keys = {
        "charname": "Test Character",
        "race": "Human",
        "classlevel": "Warrior 5",
        "proficiencybonus": 2,
        "passiveperception": 10,
        "ac": 15,
        "initiative": 1,
        "speed": 30,
        "maxhp": 40,
        "currenthp": 40,
        "temphp": 0,
        "totalhd": "5d10",
        "remaininghd": "5",
        "otherprofs": "- Common\n- Elvish",
        "features": "- Brave\n- Strong"
    }
    assert _sheet_generator.generate_basic_key_pairs() == expected_keys


def test_generate_stat_key_pairs(_sheet_generator):
    """ Test the generate_stat_key_pairs method """
    expected_keys = {
        "Strengthscore": 16,
        "Dexterityscore": 14,
        "Constitutionscore": 15,
        "Wisdomscore": 12,
        "Intelligencescore": 10,
        "Charismascore": 8,
        "Strengthmod": "+3",
        "Dexteritymod": "+2",
        "Constitutionmod": "+2",
        "Wisdommod": "+1",
        "Intelligencemod": "+0",
        "Charismamod": "-1"
    }
    assert _sheet_generator.generate_stat_key_pairs() == expected_keys


def test_generate_saving_throw_key_pairs(_sheet_generator):
    """ Test the generate_saving_throw_key_pairs method """
    expected_keys = {
        "Strengthsave": "+3",
        "Dexteritysave": "+2",
        "Constitutionsave": "+2",
        "Wisdomsave": "+1",
        "Intelligencesave": "+0",
        "Charismasave": "-1"
    }
    assert _sheet_generator.generate_saving_throw_key_pairs() == expected_keys


def test_generate_skill_key_pairs(_sheet_generator):
    """ Test the generate_skill_key_pairs method """
    expected_keys = {
        "Acrobatics": "+2",
        "AnimalHandling": "+1",
        "Arcana": "+0",
        "Athletics": "+3",
        "Deception": "-1",
        "History": "+0",
        "Insight": "+1",
        "Intimidation": "-1",
        "Investigation": "+0",
        "Medicine": "+1",
        "Nature": "+0",
        "Perception": "+1",
        "Performance": "-1",
        "Persuasion": "-1",
        "Religion": "+0",
        "SleightofHand": "+2",
        "Stealth": "+2",
        "Survival": "+1"
    }
    assert _sheet_generator.generate_skill_key_pairs() == expected_keys


def test_generate_skill_prof_key_pairs(_sheet_generator):
    """ Test the generate_skill_prof_key_pairs method """
    expected_keys = {
        "Acrobaticsprof": "",
        "AnimalHandlingprof": "",
        "Arcanaprof": "",
        "Athleticsprof": "checked",
        "Deceptionprof": "",
        "Historyprof": "",
        "Insightprof": "",
        "Intimidationprof": "",
        "Investigationprof": "",
        "Medicineprof": "",
        "Natureprof": "",
        "Perceptionprof": "checked",
        "Performanceprof": "",
        "Persuasionprof": "",
        "Religionprof": "",
        "SleightofHandprof": "",
        "Stealthprof": "",
        "Survivalprof": ""
    }
    assert _sheet_generator.generate_skill_prof_key_pairs() == expected_keys


def test_generate_saving_throw_prof_key_pairs(_sheet_generator):
    """ Test the generate_saving_throw_prof_key_pairs method """
    expected_keys = {
        "Strengthsaveprof": "checked",
        "Dexteritysaveprof": "",
        "Constitutionsaveprof": "checked",
        "Wisdomsaveprof": "",
        "Intelligencesaveprof": "",
        "Charismasaveprof": ""
    }
    assert _sheet_generator.generate_saving_throw_prof_key_pairs() == expected_keys


def get_stat_modifier(_sheet_generator):
    """ Test the get_stat_modifier method """
    assert _sheet_generator.get_stat_modifier(16) == "+3"
    assert _sheet_generator.get_stat_modifier(14) == "+2"
    assert _sheet_generator.get_stat_modifier(10) == "+0"
    assert _sheet_generator.get_stat_modifier(8) == "-1"


def get_skill_modifier(_sheet_generator):
    """ Test the get_skill_modifier method """
    assert _sheet_generator.get_skill_modifier(3) == "+3"
    assert _sheet_generator.get_skill_modifier(2) == "+2"
    assert _sheet_generator.get_skill_modifier(0) == "+0"
    assert _sheet_generator.get_skill_modifier(-1) == "-1"


def get_saving_throw_modifier(_sheet_generator):
    """ Test the get_saving_throw_modifier method """
    assert _sheet_generator.get_saving_throw_modifier(3) == "+3"
    assert _sheet_generator.get_saving_throw_modifier(2) == "+2"
    assert _sheet_generator.get_saving_throw_modifier(0) == "+0"
    assert _sheet_generator.get_saving_throw_modifier(-1) == "-1"


def check_skill_proficiency(_sheet_generator):
    """ Test the check_skill_proficiency method """
    assert _sheet_generator.check_skill_proficiency("Athletics") == "checked"
    assert _sheet_generator.check_skill_proficiency("Perception") == "checked"
    assert _sheet_generator.check_skill_proficiency("Acrobatics") == ""
    assert _sheet_generator.check_skill_proficiency("Deception") == ""


def check_saving_throw_proficiency(_sheet_generator):
    """ Test the check_saving_throw_proficiency method """
    assert _sheet_generator.check_saving_throw_proficiency("Strength") == "checked"
    assert _sheet_generator.check_saving_throw_proficiency("Constitution") == "checked"
    assert _sheet_generator.check_saving_throw_proficiency("Dexterity") == ""
    assert _sheet_generator.check_saving_throw_proficiency("Charisma") == ""


def test_list_to_textarea_string(_sheet_generator):
    """ Test the list_to_textarea_string method """
    test_list = ["Item 1", "Item 2"]
    expected_output = "- Item 1\n- Item 2"
    assert _sheet_generator.list_to_textarea_string(test_list) == expected_output

    test_empty_list = []
    expected_output = ""
    assert _sheet_generator.list_to_textarea_string(test_empty_list) == expected_output

    test_single_item_list = ["Item 1"]
    expected_output = "- Item 1"
    assert _sheet_generator.list_to_textarea_string(test_single_item_list) == expected_output
