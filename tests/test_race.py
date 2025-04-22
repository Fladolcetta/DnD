"""Tests for the race class."""

from src.race import Race


def test_race_initialization() -> None:
    """Test that you can initialize a race."""
    elf = Race("Elf")
    assert elf.name == "Elf"
    assert elf.stats == {"Dexterity": 2, "Intelligence": 1}
    assert elf.speed == 30
    assert elf.languages == ["Common", "Elvish"]
    assert elf.traits == ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"]


def test_get_race_bonus_stat() -> None:
    """Test that you can get the bonus stats."""
    dwarf = Race("Dwarf")
    assert dwarf.get_race_bonus_stat() == {"Constitution": 2, "Wisdom": 1}


def test_get_race_speed() -> None:
    """Test that you can get the speed of the race."""
    halfling = Race("Halfling")
    assert halfling.get_race_speed() == 25


def test_get_race_languages() -> None:
    """Test that you can get the languages of the race."""
    half_orc = Race("Half-Orc")
    assert half_orc.get_race_languages() == ["Common", "Orc"]


def test_get_race_traits() -> None:
    """Test that you can get the traits of the race."""
    gnome = Race("Gnome")
    assert gnome.get_race_traits() == ["Darkvision", "Gnome Cunning"]


def test_get_all_races() -> None:
    """Test that you can get all the races."""
    expected_races = [
        "Human",
        "Elf",
        "Dwarf",
        "Halfling",
        "Half-Orc",
        "Gnome",
        "Half-Elf",
        "Dragonborn",
        "Tiefling",
    ]
    assert Race.get_all_races() == expected_races
