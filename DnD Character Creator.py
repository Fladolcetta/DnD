'''
This tool is a simple dice roller for Dungeons and Dragons.
It will roll a specified number of dice with a specified number of sides.
It will also add a specified modifier to the roll.
The tool will then display the total of the roll and the individual rolls.
'''

#TODO: Update character based on class details
#TODO: Make skills an array
#TODO: Make primary stats an array
#TODO: Find opposite of primary stats and make lowest
#TODO: Add proficiency bonus

import random

class Race:
	def __init__(self, name):
		self.name = name
		self.stats = self.get_race_bonus_stat()
		self.speed = self.get_race_speed()
		self.languages = self.get_race_languages()
		self.traits = self.get_race_traits()

	def get_race_bonus_stat(self):
		race_bonus_stat = {
			"Humans": {
				"Strength": 1,
				"Dexterity": 1,
				"Constitution": 1,
				"Intelligence": 1,
				"Wisdom": 1,
				"Charisma": 1
			},
			"Elves": {
				"Dexterity": 2,
				"Intelligence": 1
			},
			"Dwarves": {
				"Constitution": 2,
				"Wisdom": 1
			},
			"Halflings": {
				"Dexterity": 2,
				"Charisma": 1
			},
			"Half-Orcs": {
				"Strength": 2,
				"Constitution": 1
			},
			"Gnomes": {
				"Intelligence": 2,
				"Constitution": 1
			},
			"Half-Elves": {
				"Charisma": 2,
				"Two Other Stats": 1
			},
			"Dragonborn": {
				"Strength": 2,
				"Charisma": 1
			},
			"Tieflings": {
				"Intelligence": 1,
				"Charisma": 2
			}
		}
		return race_bonus_stat[self.name]

	def get_race_speed(self):
		race_speed = {
			"Humans": 30,
			"Elves": 30,
			"Dwarves": 25,
			"Halflings": 25,
			"Half-Orcs": 30,
			"Gnomes": 25,
			"Half-Elves": 30,
			"Dragonborn": 30,
			"Tieflings": 30
		}
		return race_speed[self.name]

	def get_race_languages(self):
		race_languages = {
			"Humans": ["Common"],
			"Elves": ["Common", "Elvish"],
			"Dwarves": ["Common", "Dwarvish"],
			"Halflings": ["Common", "Halfling"],
			"Half-Orcs": ["Common", "Orc"],
			"Gnomes": ["Common", "Gnomish"],
			"Half-Elves": ["Common", "Elvish"],
			"Dragonborn": ["Common", "Draconic"],
			"Tieflings": ["Common", "Infernal"]
		}

		return race_languages[self.name]

	def get_race_traits(self):
		race_traits = {
			"Humans": ["None"],
			"Elves": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"],
			"Dwarves": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning"],
			"Halflings": ["Lucky", "Brave", "Halfling Nimbleness"],
			"Half-Orcs": ["Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"],
			"Gnomes": ["Darkvision", "Gnome Cunning"],
			"Half-Elves": ["Darkvision", "Fey Ancestry", "Skill Versatility"],
			"Dragonborn": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
			"Tieflings": ["Darkvision", "Hellish Resistance", "Infernal Legacy"]
		}

		return race_traits[self.name]

class DnDClass:
	def __init__(self, name):
		self.name = name
		self.hit_die = self.get_hit_die()
		self.primary_stat = self.get_primary_stat()
		self.saving_throws = self.get_saving_throws()
		self.skills = self.get_skills()

	def get_hit_die(self):
		hit_die = {
			"Barbarian": 12,
			"Bard": 8,
			"Cleric": 8,
			"Druid": 8,
			"Fighter": 10,
			"Monk": 8,
			"Paladin": 10,
			"Ranger": 10,
			"Rogue": 8,
			"Sorcerer": 6,
			"Warlock": 8,
			"Wizard": 6
		}
		return hit_die[self.name]

	def get_primary_stat(self):
		primary_stat = {
			"Barbarian": "Strength",
			"Bard": "Charisma",
			"Cleric": "Wisdom",
			"Druid": "Wisdom",
			"Fighter": "Strength or Dexterity",
			"Monk": "Dexterity and Wisdom",
			"Paladin": "Strength and Charisma",
			"Ranger": "Dexterity and Wisdom",
			"Rogue": "Dexterity",
			"Sorcerer": "Charisma",
			"Warlock": "Charisma",
			"Wizard": "Intelligence"
		}
		return primary_stat[self.name]

	def get_saving_throws(self):
		saving_throws = {
			"Barbarian": ["Strength", "Constitution"],
			"Bard": ["Dexterity", "Charisma"],
			"Cleric": ["Wisdom", "Charisma"],
			"Druid": ["Intelligence", "Wisdom"],
			"Fighter": ["Strength", "Constitution"],
			"Monk": ["Strength", "Dexterity"],
			"Paladin": ["Wisdom", "Charisma"],
			"Ranger": ["Strength", "Dexterity"],
			"Rogue": ["Dexterity", "Intelligence"],
			"Sorcerer": ["Constitution", "Charisma"],
			"Warlock": ["Wisdom", "Charisma"],
			"Wizard": ["Intelligence", "Wisdom"]
		}
		return saving_throws[self.name]

	def get_skills(self):
		skills = {
			"Barbarian": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
			"Bard": ["Any Three"],
			"Cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
			"Druid": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
			"Fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
			"Monk": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
			"Paladin": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
			"Ranger": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
			"Rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
			"Sorcerer": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
			"Warlock": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
			"Wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
		}
		return skills[self.name]




class Dice:
	def __init__(self, num_dice, num_sides, modifier):
		self.num_dice = num_dice
		self.num_sides = num_sides
		self.modifier = modifier
		self.rolls = []
		self.criticalSuccess = False
		self.criticalFail = False

	def roll(self):
		for i in range(self.num_dice):
			self.rolls.append(random.randint(1, self.num_sides))
			if self.rolls[i] == self.num_sides:
				self.criticalSuccess = True
			if self.rolls[i] == 1:
				self.criticalFail = True
		total = sum(self.rolls) + self.modifier
		return total, self.rolls

class character:
	def __init__(self, name, desired_race=None, desired_class=None):
		self.name = name
		self.race = desired_race
		self.dnd_class = desired_class
		self.speed = 0
		self.traits = []
		self.languages = []
		self.stats = {
			"Strength": 0,
			"Dexterity": 0,
			"Constitution": 0,
			"Intelligence": 0,
			"Wisdom": 0,
			"Charisma": 0
		}
		self.strengthSkills = {
			"Athletics": 0
		}
		self.dexteritySkills = {
			"Acrobatics": 0,
			"Sleight of Hand": 0,
			"Stealth": 0
		}
		self.constitutionSkills = {}
		self.intelligenceSkills = {
			"Arcana": 0,
			"History": 0,
			"Investigation": 0,
			"Nature": 0,
			"Religion": 0
		}
		self.wisdomSkills = {
			"Animal Handling": 0,
			"Insight": 0,
			"Medicine": 0,
			"Perception": 0,
			"Survival": 0
		}
		self.charismaSkills = {
			"Deception": 0,
			"Intimidation": 0,
			"Performance": 0,
			"Persuasion": 0
		}

		# Roll stats and update values
		self.roll_stats()
		self.update_race_details()
		self.update_skills()

	def find_modifier(self, stat):
		return (self.stats[stat] - 10) // 2

	def update_race_details(self):
		race_object = Race(self.race)
		self.speed = race_object.speed
		self.languages = race_object.languages
		self.traits = race_object.traits
		for stat in self.stats:
			try:
				self.stats[stat] = self.stats[stat] + race_object.stats[stat]
			except KeyError:
				pass

	def update_skills(self):
		for stat in self.stats:
			if stat == "Strength":
				for skill in self.strengthSkills:
					self.strengthSkills[skill] = self.find_modifier(stat)
			if stat == "Dexterity":
				for skill in self.dexteritySkills:
					self.dexteritySkills[skill] = self.find_modifier(stat)
			if stat == "Constitution":
				for skill in self.constitutionSkills:
					self.constitutionSkills[skill] = self.find_modifier(stat)
			if stat == "Intelligence":
				for skill in self.intelligenceSkills:
					self.intelligenceSkills[skill] = self.find_modifier(stat)
			if stat == "Wisdom":
				for skill in self.wisdomSkills:
					self.wisdomSkills[skill] = self.find_modifier(stat)
			if stat == "Charisma":
				for skill in self.charismaSkills:
					self.charismaSkills[skill] = self.find_modifier(stat)


	def roll_stats(self, primary_stat=None, secondary_stat=None):
		for stat in self.stats:
			die = Dice(4, 6, 0)
			total, rolls = die.roll()
			self.stats[stat] = total - min(rolls)



def print_roll(total, rolls):
	# Prompt the user for the number of dice, the number of sides, and the modifier
	num_dice = int(input("Enter the number of dice to roll: "))
	num_sides = int(input("Enter the number of sides on the dice: "))
	modifier = int(input("Enter the modifier: "))
	die = Dice(num_dice, num_sides, modifier)
	total, rolls = die.roll()
	print("Total: {}".format(total))
	print("Rolls: {}".format(rolls))
	if die.criticalSuccess:
		print("Critical Success!")
	if die.criticalFail:
		print("Critical Fail!")

def print_stats(stats):
	for stat in stats:
		print("{}: {}".format(stat, stats[stat]))

def print_skills(skills):
	for skill in skills:
		print("- {}: {}".format(skill, skills[skill]))

def print_all_skills(character):
	print("Strength Skills:")

	print_skills(character.strengthSkills)
	print("Dexterity Skills:")
	print_skills(character.dexteritySkills)
	print("Constitution Skills:")
	print_skills(character.constitutionSkills)
	print("Intelligence Skills:")
	print_skills(character.intelligenceSkills)
	print("Wisdom Skills:")
	print_skills(character.wisdomSkills)
	print("Charisma Skills:")
	print_skills(character.charismaSkills)

def print_character(character):
	print("Name: {}".format(character.name))
	print_stats(character.stats)
	print_all_skills(character)
	print("Speed: {}".format(character.speed))
	print("Languages: {}".format(character.languages))
	print("Traits: {}".format(character.traits))

def main():
	frank = character("Frank", "Elves")
	print_character(frank)

if __name__ == '__main__':
	main()