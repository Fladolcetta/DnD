""" Main file for the Dungeons and Dragons character generator. """
from src.dice import Dice
from src.character import Character

def print_roll(total, rolls):
    """ Prompt the user for the number of dice, the number of sides, and the modifier. """

    num_dice = int(input("Enter the number of dice to roll: "))
    num_sides = int(input("Enter the number of sides on the dice: "))
    modifier = int(input("Enter the modifier: "))
    die = Dice(num_dice, num_sides, modifier)
    total, rolls = die.roll()
    print(f"Total: {total}")
    print(f"Rolls: {rolls}")
    if die.critical_success:
        print("Critical Success!")
    if die.critical_fail:
        print("Critical Fail!")

def print_stats(stats):
    """ Print the stats of the character. """
    for stat in stats:
        print(f"{stat}: {stats[stat]}")

def print_skills(skills):
    """ Print the skills of the character. """
    for skill in skills:
        print(f"- {skill}: {skills[skill]}")

def print_all_skills(character):
    """ Print all the skills of the character. """
    print_skills(character.all_skills)

def print_character(character):
    """ Print the character. """
    print(f"Name: {character.name}")
    print_stats(character.stats)
    print_all_skills(character)
    print(f"Speed: {character.speed}")
    print(f"Languages: {character.languages}")
    print(f"Traits: {character.traits}")

def main():
    """ Main function. """
    frank = Character("Frank", "Elves")
    print_character(frank)

if __name__ == '__main__':
    main()
