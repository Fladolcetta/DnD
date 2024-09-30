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
    print("Stats:")
    for stat in stats:
        print(f" - {stat}: {stats[stat]}")

def print_all_skills(character):
    """ Print all the skills of the character. """
    print("Skills:")
    for skill in character.all_skills:
        print(f" - {skill}: {character.all_skills[skill]}")

def print_proficiencies(character):
    """ Print the proficiencies of the character. """
    if character.proficiencies:
        print(f"Proficiencies:(+{character.proficiency_bonus})")
        for proficiency in character.proficiencies:
            print(f" - {proficiency}")

def print_saving_throws(character):
    """ Print the saving throws of the character. """
    if character.saving_throws:
        print("Saving Throws:")
        for saving_throw in character.saving_throws:
            print(f" - {saving_throw}")

def print_languages(character):
    """ Print the languages of the character. """
    print("Languages:")
    for language in character.languages:
        print(f" - {language}")

def print_traits(character):
    """ Print the traits of the character. """
    print("Traits:")
    for trait in character.traits:
        print(f" - {trait}")

def print_character(character):
    """ Print the character. """
    print(f"Name: {character.name}")
    print(f"Race: {character.race}")
    print(f"Class: {character.dnd_class}")
    print(f"Hit Die: {character.hit_die}")
    print(f"Speed: {character.speed}")
    print_languages(character)
    print_traits(character)
    print_stats(character.stats)
    print_all_skills(character)
    print_saving_throws(character)
    print_proficiencies(character)

def main():
    """ Main function. """
    frank = Character("Frank", "Elves")
    print_character(frank)

if __name__ == '__main__':
    main()
