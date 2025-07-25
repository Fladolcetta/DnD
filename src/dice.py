"""A module to represent a dice roll."""

import secrets


class Dice:
    """A class to represent a dice roll."""

    def __init__(self, num_dice: int, num_sides: int, modifier: int) -> None:
        """Initialize the dice roll."""
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.modifier = modifier
        self.rolls = []
        self.total = 0
        self.critical_success = False
        self.critical_fail = False

    def roll(self) -> None:
        """Roll the dice and return the total."""
        for i in range(self.num_dice):
            self.rolls.append(secrets.choice(range(1, self.num_sides + 1)))
            if self.rolls[i] == self.num_sides:
                self.critical_success = True
            if self.rolls[i] == 1:
                self.critical_fail = True
        total = sum(self.rolls) + self.modifier
        self.total = total
        self.rolls = self.rolls

    def roll_stat(self) -> int:
        """Roll a single stat."""
        rolls = [secrets.choice(range(1, 7)) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)

    def roll_stats(self) -> list:
        """Roll the stats for the character."""
        return [self.roll_stat() for _ in range(6)]
