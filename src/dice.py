""" A module to represent a dice roll. """
import random


class Dice:
    """ A class to represent a dice roll. """
    def __init__(self, num_dice: int, num_sides: int, modifier: int) -> None:
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.modifier = modifier
        self.rolls = []
        self.total = 0
        self.rolls = []
        self.critical_success = False
        self.critical_fail = False
        self.roll()

    def roll(self) -> None:
        """ Roll the dice and return the total. """
        for i in range(self.num_dice):
            self.rolls.append(random.randint(1, self.num_sides))
            if self.rolls[i] == self.num_sides:
                self.critical_success = True
            if self.rolls[i] == 1:
                self.critical_fail = True
        total = sum(self.rolls) + self.modifier
        self.total = total
        self.rolls = self.rolls
