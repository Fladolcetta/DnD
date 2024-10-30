"""Tests for the Dice class."""
from unittest.mock import patch
from src.dice import Dice


def test_dice_initialization():
    """Test that the Dice class initializes"""
    dice = Dice(num_dice=2, num_sides=6, modifier=3)
    assert dice.num_dice == 2
    assert dice.num_sides == 6
    assert dice.modifier == 3
    assert dice.total == 0
    assert dice.rolls == []


@patch('random.randint')
def test_roll_updates_total(mock_randint):
    """Test if the roll function correctly updates the total."""
    mock_randint.side_effect = [4, 5]
    dice = Dice(num_dice=2, num_sides=6, modifier=3)
    dice.roll()
    assert dice.total == 12  # (4 + 5 + 3)


@patch('random.randint')
def test_roll_critical_success(mock_randint):
    """Test that a critical success is detected."""
    mock_randint.side_effect = [6, 3]
    dice = Dice(num_dice=2, num_sides=6, modifier=0)
    dice.roll()
    assert dice.critical_success is True


@patch('random.randint')
def test_roll_critical_fail(mock_randint):
    """Test that a critical fail is detected."""
    mock_randint.side_effect = [1, 5]
    dice = Dice(num_dice=2, num_sides=6, modifier=0)
    dice.roll()
    assert dice.critical_fail is True


@patch('random.randint')
def test_roll_modifier_applied_correctly(mock_randint):
    """Test that the modifier is correctly applied to the total."""
    mock_randint.side_effect = [2, 3]
    dice = Dice(num_dice=2, num_sides=6, modifier=4)
    dice.roll()
    assert dice.total == 9  # (2 + 3 + 4)


@patch('random.randint')
def test_multiple_dice_rolls(mock_randint):
    """Test that multiple dice rolls are stored."""
    mock_randint.side_effect = [1, 6, 3, 4]
    dice = Dice(num_dice=4, num_sides=6, modifier=2)
    dice.roll()
    assert dice.total == 16  # (1 + 6 + 3 + 4 + 2)
    assert len(dice.rolls) == 4  # There should be 4 rolls


@patch('random.randint')
def test_single_sided_die(mock_randint):
    """Test that a single-sided die always rolls 1."""
    mock_randint.return_value = 1
    dice = Dice(num_dice=1, num_sides=1, modifier=0)
    dice.roll()
    assert dice.total == 1
    assert dice.critical_fail is True


def test_roll_stat():
    """Test the roll_stat method"""
    dice = Dice(num_dice=4, num_sides=6, modifier=0)
    stat = dice.roll_stat()
    assert 3 <= stat <= 18


def test_roll_stats():
    """Test the roll_stats method"""
    dice = Dice(num_dice=4, num_sides=6, modifier=0)
    stats = dice.roll_stats()
    assert len(stats) == 6
    for stat in stats:
        assert 3 <= stat <= 18
