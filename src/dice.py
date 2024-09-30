""" A module to represent a dice roll. """
import random


class Dice:
    """ A class to represent a dice roll. """
    def __init__(self, num_dice, num_sides, modifier):
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.modifier = modifier
        self.rolls = []
        self.critical_success = False
        self.critical_fail = False

    def roll(self):
        """ Roll the dice and return the total. """
        for i in range(self.num_dice):
            self.rolls.append(random.randint(1, self.num_sides))
            if self.rolls[i] == self.num_sides:
                self.critical_success = True
            if self.rolls[i] == 1:
                self.critical_fail = True
        total = sum(self.rolls) + self.modifier
        return total, self.rolls
