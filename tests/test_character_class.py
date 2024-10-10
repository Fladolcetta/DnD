"""Tests for the CharacterClass class."""
import pytest
from src.character_class import CharacterClass


def test_character_class_initialization():
    """Test that you can initialize a character class."""
    barbarian = CharacterClass("Barbarian")
    assert barbarian.name == "Barbarian"
    assert barbarian.hit_die == 12
    assert barbarian.primary_stat == ["Strength"]
    assert barbarian.saving_throws_proficiencies == ["Strength", "Constitution"]
    assert barbarian.skill_proficiencies == ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]


@pytest.mark.parametrize("class_name, expected_hit_die", [
    ("Barbarian", 12),
    ("Wizard", 6),
    ("Fighter", 10),
    ("Rogue", 8),
])
def test_get_hit_die(class_name, expected_hit_die):
    """Test that you can get the hit die of a class."""
    char_class = CharacterClass(class_name)
    assert char_class.hit_die == expected_hit_die


@pytest.mark.parametrize("class_name, expected_primary_stat", [
    ("Barbarian", ["Strength"]),
    ("Bard", ["Charisma"]),
    ("Monk", ["Dexterity", "Wisdom"]),
])
def test_get_primary_stat(class_name, expected_primary_stat):
    """Test that you can get the primary stat of a class."""
    char_class = CharacterClass(class_name)
    assert char_class.primary_stat == expected_primary_stat


@pytest.mark.parametrize("class_name, expected_worst_stat", [
    ("Barbarian", ["Intelligence"]),
    ("Bard", ["Strength"]),
    ("Wizard", ["Strength"]),
])
def test_get_worst_stat(class_name, expected_worst_stat):
    """Test that you can get the worst stat of a class."""
    char_class = CharacterClass(class_name)
    assert char_class.get_worst_stat() == expected_worst_stat


@pytest.mark.parametrize("class_name, expected_saving_throws", [
    ("Rogue", ["Dexterity", "Intelligence"]),
    ("Sorcerer", ["Constitution", "Charisma"]),
    ("Paladin", ["Wisdom", "Charisma"]),
])
def test_get_saving_throw_proficiencies(class_name, expected_saving_throws):
    """Test that you can get the saving throws of a class."""
    char_class = CharacterClass(class_name)
    assert char_class.saving_throws_proficiencies == expected_saving_throws


@pytest.mark.parametrize("class_name, expected_skills", [
    ("Bard", ["Acrobatics", "Performance", "Persuasion"]),
    ("Wizard", ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]),
    ("Fighter", ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]),
])
def test_get_skill_proficiencies(class_name, expected_skills):
    """Test that you can get the skill proficiencies of a class."""
    char_class = CharacterClass(class_name)
    assert char_class.skill_proficiencies == expected_skills


def test_get_all_classes():
    """Test that you can get all the classes."""
    all_classes = CharacterClass.get_all_classes()
    assert all_classes == [
        "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
        "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
    ]
