# Table of Contents

* [text\_printer](#text_printer)
  * [TextPrinter](#text_printer.TextPrinter)
    * [update\_text\_to\_print](#text_printer.TextPrinter.update_text_to_print)
    * [split\_string](#text_printer.TextPrinter.split_string)
    * [header](#text_printer.TextPrinter.header)
    * [subheader](#text_printer.TextPrinter.subheader)
    * [bolded](#text_printer.TextPrinter.bolded)
    * [list\_to\_dict](#text_printer.TextPrinter.list_to_dict)
    * [sort\_dict](#text_printer.TextPrinter.sort_dict)
    * [print\_data](#text_printer.TextPrinter.print_data)
    * [print\_single\_value](#text_printer.TextPrinter.print_single_value)
    * [print\_dict\_with\_modifiers](#text_printer.TextPrinter.print_dict_with_modifiers)
    * [print\_dict\_with\_data\_and\_modifiers](#text_printer.TextPrinter.print_dict_with_data_and_modifiers)
    * [print\_modifiers](#text_printer.TextPrinter.print_modifiers)
    * [print\_character](#text_printer.TextPrinter.print_character)
    * [print\_basic\_stats](#text_printer.TextPrinter.print_basic_stats)
    * [print\_race\_info](#text_printer.TextPrinter.print_race_info)
    * [print\_class\_info](#text_printer.TextPrinter.print_class_info)
    * [print\_roll](#text_printer.TextPrinter.print_roll)
* [db](#db)
  * [DB](#db.DB)
    * [insert\_character](#db.DB.insert_character)
    * [insert\_into\_table](#db.DB.insert_into_table)
    * [read\_from\_table](#db.DB.read_from_table)
    * [load\_character\_list](#db.DB.load_character_list)
    * [load\_character](#db.DB.load_character)
* [character\_class](#character_class)
  * [CharacterClass](#character_class.CharacterClass)
    * [get\_hit\_die](#character_class.CharacterClass.get_hit_die)
    * [get\_primary\_stat](#character_class.CharacterClass.get_primary_stat)
    * [get\_worst\_stat](#character_class.CharacterClass.get_worst_stat)
    * [get\_saving\_throw\_proficiencies](#character_class.CharacterClass.get_saving_throw_proficiencies)
    * [get\_skill\_proficiencies](#character_class.CharacterClass.get_skill_proficiencies)
    * [get\_all\_classes](#character_class.CharacterClass.get_all_classes)
* [sheet\_generator](#sheet_generator)
  * [SheetGenerator](#sheet_generator.SheetGenerator)
    * [\_\_init\_\_](#sheet_generator.SheetGenerator.__init__)
    * [generate\_key\_pairs](#sheet_generator.SheetGenerator.generate_key_pairs)
    * [generate\_basic\_key\_pairs](#sheet_generator.SheetGenerator.generate_basic_key_pairs)
    * [generate\_stat\_key\_pairs](#sheet_generator.SheetGenerator.generate_stat_key_pairs)
    * [generate\_saving\_throw\_key\_pairs](#sheet_generator.SheetGenerator.generate_saving_throw_key_pairs)
    * [generate\_skill\_key\_pairs](#sheet_generator.SheetGenerator.generate_skill_key_pairs)
    * [generate\_skill\_prof\_key\_pairs](#sheet_generator.SheetGenerator.generate_skill_prof_key_pairs)
    * [generate\_saving\_throw\_prof\_key\_pairs](#sheet_generator.SheetGenerator.generate_saving_throw_prof_key_pairs)
    * [get\_stat\_modifier](#sheet_generator.SheetGenerator.get_stat_modifier)
    * [get\_skill\_modifier](#sheet_generator.SheetGenerator.get_skill_modifier)
    * [get\_saving\_throw\_modifier](#sheet_generator.SheetGenerator.get_saving_throw_modifier)
    * [check\_skill\_proficiency](#sheet_generator.SheetGenerator.check_skill_proficiency)
    * [check\_save\_proficiency](#sheet_generator.SheetGenerator.check_save_proficiency)
    * [list\_to\_textarea\_string](#sheet_generator.SheetGenerator.list_to_textarea_string)
* [race](#race)
  * [Race](#race.Race)
    * [get\_race\_bonus\_stat](#race.Race.get_race_bonus_stat)
    * [get\_race\_speed](#race.Race.get_race_speed)
    * [get\_race\_languages](#race.Race.get_race_languages)
    * [get\_race\_traits](#race.Race.get_race_traits)
    * [get\_all\_races](#race.Race.get_all_races)
* [\_\_init\_\_](#__init__)
* [dice](#dice)
  * [Dice](#dice.Dice)
    * [roll](#dice.Dice.roll)
    * [roll\_stat](#dice.Dice.roll_stat)
    * [roll\_stats](#dice.Dice.roll_stats)
* [page\_loader](#page_loader)
  * [PageLoader](#page_loader.PageLoader)
    * [load\_left\_right\_page](#page_loader.PageLoader.load_left_right_page)
    * [load\_left\_only\_page](#page_loader.PageLoader.load_left_only_page)
    * [display\_char](#page_loader.PageLoader.display_char)
    * [load\_roll](#page_loader.PageLoader.load_roll)
    * [load\_races](#page_loader.PageLoader.load_races)
    * [load\_classes](#page_loader.PageLoader.load_classes)
    * [load\_table](#page_loader.PageLoader.load_table)
    * [left\_right\_dance](#page_loader.PageLoader.left_right_dance)
    * [load\_create\_character](#page_loader.PageLoader.load_create_character)
    * [load\_old\_character](#page_loader.PageLoader.load_old_character)
    * [build\_script\_string](#page_loader.PageLoader.build_script_string)
    * [build\_styles\_string](#page_loader.PageLoader.build_styles_string)
* [character](#character)
  * [Character](#character.Character)
    * [new\_character](#character.Character.new_character)
    * [store\_character\_in\_db](#character.Character.store_character_in_db)
    * [find\_modifier\_stat](#character.Character.find_modifier_stat)
    * [find\_modifier\_value](#character.Character.find_modifier_value)
    * [update\_race\_details](#character.Character.update_race_details)
    * [update\_class\_details](#character.Character.update_class_details)
    * [update\_skills](#character.Character.update_skills)
    * [update\_ac](#character.Character.update_ac)
    * [update\_initiative](#character.Character.update_initiative)
    * [update\_hp](#character.Character.update_hp)
    * [update\_passive\_perception](#character.Character.update_passive_perception)
    * [roll\_stats](#character.Character.roll_stats)
    * [update\_skill\_for\_stat](#character.Character.update_skill_for_stat)
    * [load\_character\_from\_db](#character.Character.load_character_from_db)

<a id="text_printer"></a>

# text\_printer

A module for printing text to the console.

<a id="text_printer.TextPrinter"></a>

## TextPrinter Objects

```python
class TextPrinter()
```

A class to print text to the console.

<a id="text_printer.TextPrinter.update_text_to_print"></a>

#### update\_text\_to\_print

```python
def update_text_to_print(text: str) -> None
```

Print the text.

<a id="text_printer.TextPrinter.split_string"></a>

#### split\_string

```python
def split_string(string: str) -> str
```

Split the string.

<a id="text_printer.TextPrinter.header"></a>

#### header

```python
def header(title: str) -> None
```

Print the header.

<a id="text_printer.TextPrinter.subheader"></a>

#### subheader

```python
def subheader(title: str) -> None
```

Print the subheader.

<a id="text_printer.TextPrinter.bolded"></a>

#### bolded

```python
def bolded(text: str) -> None
```

Print the text in bold.

<a id="text_printer.TextPrinter.list_to_dict"></a>

#### list\_to\_dict

```python
def list_to_dict(list_object: list) -> dict
```

Convert a list to a dictionary.

<a id="text_printer.TextPrinter.sort_dict"></a>

#### sort\_dict

```python
def sort_dict(dict_object: dict) -> dict
```

Sort the dictionary.

<a id="text_printer.TextPrinter.print_data"></a>

#### print\_data

```python
def print_data(data: Union[list, dict], title: str) -> None
```

Print the dictionary.

<a id="text_printer.TextPrinter.print_single_value"></a>

#### print\_single\_value

```python
def print_single_value(value: Union[int, str], title: str) -> None
```

Print a single value.

<a id="text_printer.TextPrinter.print_dict_with_modifiers"></a>

#### print\_dict\_with\_modifiers

```python
def print_dict_with_modifiers(data: dict, title: str) -> None
```

Print the dictionary with modifiers.

<a id="text_printer.TextPrinter.print_dict_with_data_and_modifiers"></a>

#### print\_dict\_with\_data\_and\_modifiers

```python
def print_dict_with_data_and_modifiers(data: dict, title: str) -> None
```

Print the dictionary with data and modifiers.

<a id="text_printer.TextPrinter.print_modifiers"></a>

#### print\_modifiers

```python
def print_modifiers(value: int) -> str
```

Print the modifiers of the value.

<a id="text_printer.TextPrinter.print_character"></a>

#### print\_character

```python
def print_character(character: Character) -> str
```

Print the character.

<a id="text_printer.TextPrinter.print_basic_stats"></a>

#### print\_basic\_stats

```python
def print_basic_stats(character: Character) -> str
```

Print the basic stats.

<a id="text_printer.TextPrinter.print_race_info"></a>

#### print\_race\_info

```python
def print_race_info(race_name: str) -> str
```

Print the list of races.

<a id="text_printer.TextPrinter.print_class_info"></a>

#### print\_class\_info

```python
def print_class_info(class_name: str) -> str
```

Print the list of classes.

<a id="text_printer.TextPrinter.print_roll"></a>

#### print\_roll

```python
def print_roll(num_dice: int, num_sides: int, modifier: int) -> str
```

Print the roll of the dice.

<a id="db"></a>

# db

A module for the database connection.

<a id="db.DB"></a>

## DB Objects

```python
class DB()
```

A class to represent a database connection.

<a id="db.DB.insert_character"></a>

#### insert\_character

```python
def insert_character(name: str, race: str, dnd_class: str, stats: dict) -> int
```

Insert a character into the database.

<a id="db.DB.insert_into_table"></a>

#### insert\_into\_table

```python
def insert_into_table(sql: str, data: list) -> int
```

Insert into a table.

<a id="db.DB.read_from_table"></a>

#### read\_from\_table

```python
def read_from_table(sql: str) -> list[list]
```

Read data from the db.

<a id="db.DB.load_character_list"></a>

#### load\_character\_list

```python
def load_character_list() -> list[list]
```

Load the character list

<a id="db.DB.load_character"></a>

#### load\_character

```python
def load_character(char_id: int) -> dict
```

Load a character from the database.

<a id="character_class"></a>

# character\_class

A module to represent a class in Dungeons and Dragons.

<a id="character_class.CharacterClass"></a>

## CharacterClass Objects

```python
class CharacterClass()
```

A class to represent a class in Dungeons and Dragons.

<a id="character_class.CharacterClass.get_hit_die"></a>

#### get\_hit\_die

```python
def get_hit_die() -> dict
```

Get the hit die of the class.

<a id="character_class.CharacterClass.get_primary_stat"></a>

#### get\_primary\_stat

```python
def get_primary_stat() -> list
```

Get the primary stat of the class.

<a id="character_class.CharacterClass.get_worst_stat"></a>

#### get\_worst\_stat

```python
def get_worst_stat() -> dict
```

Get the worst stat of the class.

<a id="character_class.CharacterClass.get_saving_throw_proficiencies"></a>

#### get\_saving\_throw\_proficiencies

```python
def get_saving_throw_proficiencies() -> dict
```

Get the saving throws of the class.

<a id="character_class.CharacterClass.get_skill_proficiencies"></a>

#### get\_skill\_proficiencies

```python
def get_skill_proficiencies() -> dict
```

Get the skills of the class.

<a id="character_class.CharacterClass.get_all_classes"></a>

#### get\_all\_classes

```python
@staticmethod
def get_all_classes() -> list
```

Get all classes.

<a id="sheet_generator"></a>

# sheet\_generator

A module for generating a character sheet key_pairs.

<a id="sheet_generator.SheetGenerator"></a>

## SheetGenerator Objects

```python
class SheetGenerator()
```

A class to generate a character sheet.

<a id="sheet_generator.SheetGenerator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(character: Character) -> None
```

Initialize the SheetGenerator.

<a id="sheet_generator.SheetGenerator.generate_key_pairs"></a>

#### generate\_key\_pairs

```python
def generate_key_pairs() -> dict
```

Generate all key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_basic_key_pairs"></a>

#### generate\_basic\_key\_pairs

```python
def generate_basic_key_pairs() -> dict
```

Generate basic key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_stat_key_pairs"></a>

#### generate\_stat\_key\_pairs

```python
def generate_stat_key_pairs() -> dict
```

Generate stat key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_saving_throw_key_pairs"></a>

#### generate\_saving\_throw\_key\_pairs

```python
def generate_saving_throw_key_pairs() -> dict
```

Generate saving throw key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_skill_key_pairs"></a>

#### generate\_skill\_key\_pairs

```python
def generate_skill_key_pairs() -> dict
```

Generate skill key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_skill_prof_key_pairs"></a>

#### generate\_skill\_prof\_key\_pairs

```python
def generate_skill_prof_key_pairs() -> dict
```

Generate key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.generate_saving_throw_prof_key_pairs"></a>

#### generate\_saving\_throw\_prof\_key\_pairs

```python
def generate_saving_throw_prof_key_pairs() -> dict
```

Generate key pairs for the character sheet.

<a id="sheet_generator.SheetGenerator.get_stat_modifier"></a>

#### get\_stat\_modifier

```python
def get_stat_modifier(stat: str) -> int
```

Get the modifier of the stat.

<a id="sheet_generator.SheetGenerator.get_skill_modifier"></a>

#### get\_skill\_modifier

```python
def get_skill_modifier(skill: str) -> int
```

Get the modifier of the skill.

<a id="sheet_generator.SheetGenerator.get_saving_throw_modifier"></a>

#### get\_saving\_throw\_modifier

```python
def get_saving_throw_modifier(save: str) -> int
```

Get the modifier of the saving throw.

<a id="sheet_generator.SheetGenerator.check_skill_proficiency"></a>

#### check\_skill\_proficiency

```python
def check_skill_proficiency(skill: str) -> bool
```

Check if the character is proficient in the skill.

<a id="sheet_generator.SheetGenerator.check_save_proficiency"></a>

#### check\_save\_proficiency

```python
def check_save_proficiency(save: str) -> bool
```

Check if the character is proficient in the save.

<a id="sheet_generator.SheetGenerator.list_to_textarea_string"></a>

#### list\_to\_textarea\_string

```python
def list_to_textarea_string(data: list) -> str
```

Convert a list to a string.

<a id="race"></a>

# race

A module for representing a race in Dungeons and Dragons.

<a id="race.Race"></a>

## Race Objects

```python
class Race()
```

A class to represent a race in Dungeons and Dragons.

<a id="race.Race.get_race_bonus_stat"></a>

#### get\_race\_bonus\_stat

```python
def get_race_bonus_stat() -> dict
```

Get the bonus stats of the Race.

<a id="race.Race.get_race_speed"></a>

#### get\_race\_speed

```python
def get_race_speed() -> int
```

Get the speed of the Race.

<a id="race.Race.get_race_languages"></a>

#### get\_race\_languages

```python
def get_race_languages() -> list
```

Get the languages of the Race.

<a id="race.Race.get_race_traits"></a>

#### get\_race\_traits

```python
def get_race_traits() -> list
```

Get the traits of the Race.

<a id="race.Race.get_all_races"></a>

#### get\_all\_races

```python
@staticmethod
def get_all_races() -> list
```

Get a list of all the Dungeons and Dragons races

<a id="__init__"></a>

# \_\_init\_\_

<a id="dice"></a>

# dice

A module to represent a dice roll.

<a id="dice.Dice"></a>

## Dice Objects

```python
class Dice()
```

A class to represent a dice roll.

<a id="dice.Dice.roll"></a>

#### roll

```python
def roll() -> None
```

Roll the dice and return the total.

<a id="dice.Dice.roll_stat"></a>

#### roll\_stat

```python
def roll_stat() -> int
```

Roll a single stat.

<a id="dice.Dice.roll_stats"></a>

#### roll\_stats

```python
def roll_stats() -> list
```

Roll the stats for the character.

<a id="page_loader"></a>

# page\_loader

A module to load html pages.

<a id="page_loader.PageLoader"></a>

## PageLoader Objects

```python
class PageLoader()
```

A class to load html pages.

<a id="page_loader.PageLoader.load_left_right_page"></a>

#### load\_left\_right\_page

```python
def load_left_right_page(left_content: str = "",
                         right_content: str = "",
                         subtitle: str = "") -> str
```

Load the page.

<a id="page_loader.PageLoader.load_left_only_page"></a>

#### load\_left\_only\_page

```python
def load_left_only_page(left_content: str = "", subtitle: str = "") -> str
```

Load the page.

<a id="page_loader.PageLoader.display_char"></a>

#### display\_char

```python
def display_char(char: Character) -> str
```

Display the character sheet.

<a id="page_loader.PageLoader.load_roll"></a>

#### load\_roll

```python
def load_roll(args: dict) -> str
```

Load the roll page.

<a id="page_loader.PageLoader.load_races"></a>

#### load\_races

```python
def load_races(args: dict) -> str
```

Load the races page.

<a id="page_loader.PageLoader.load_classes"></a>

#### load\_classes

```python
def load_classes(args: dict) -> str
```

Load the classes page.

<a id="page_loader.PageLoader.load_table"></a>

#### load\_table

```python
def load_table() -> str
```

Load the table page.

<a id="page_loader.PageLoader.left_right_dance"></a>

#### left\_right\_dance

```python
def left_right_dance(submit: Union[None, str], left_content: str,
                     right_content: str, subtitle: str) -> str
```

Load the left right page.

<a id="page_loader.PageLoader.load_create_character"></a>

#### load\_create\_character

```python
def load_create_character(args: dict) -> str
```

Load the sheet page.

<a id="page_loader.PageLoader.load_old_character"></a>

#### load\_old\_character

```python
def load_old_character(args: dict) -> str
```

Load the sheet page.

<a id="page_loader.PageLoader.build_script_string"></a>

#### build\_script\_string

```python
def build_script_string(script_list: list) -> str
```

Build a string of script tags.

<a id="page_loader.PageLoader.build_styles_string"></a>

#### build\_styles\_string

```python
def build_styles_string(styles_list: list) -> str
```

Build a string of style tags.

<a id="character"></a>

# character

A module to represent a character in Dungeons and Dragons.

<a id="character.Character"></a>

## Character Objects

```python
class Character()
```

A class to represent a character in Dungeons and Dragons.

<a id="character.Character.new_character"></a>

#### new\_character

```python
def new_character(name: str, race: str, dnd_class: str, stats=None) -> None
```

Create a new character.

<a id="character.Character.store_character_in_db"></a>

#### store\_character\_in\_db

```python
def store_character_in_db() -> None
```

Create the character in the database.

<a id="character.Character.find_modifier_stat"></a>

#### find\_modifier\_stat

```python
def find_modifier_stat(stat: str) -> int
```

Find the modifier for a given stat.

<a id="character.Character.find_modifier_value"></a>

#### find\_modifier\_value

```python
@staticmethod
def find_modifier_value(value: int) -> int
```

Find the modifier for a given value.

<a id="character.Character.update_race_details"></a>

#### update\_race\_details

```python
def update_race_details() -> None
```

Update the character based on the race.

<a id="character.Character.update_class_details"></a>

#### update\_class\_details

```python
def update_class_details() -> None
```

Update the character based on the class.

<a id="character.Character.update_skills"></a>

#### update\_skills

```python
def update_skills() -> None
```

Update the skills based on the stats.

<a id="character.Character.update_ac"></a>

#### update\_ac

```python
def update_ac() -> None
```

Update the AC based on the stats.

<a id="character.Character.update_initiative"></a>

#### update\_initiative

```python
def update_initiative() -> None
```

Update the initiative based on the stats.

<a id="character.Character.update_hp"></a>

#### update\_hp

```python
def update_hp() -> None
```

Update the HP based on the stats.

<a id="character.Character.update_passive_perception"></a>

#### update\_passive\_perception

```python
def update_passive_perception() -> None
```

Update the passive perception based on the stats.

<a id="character.Character.roll_stats"></a>

#### roll\_stats

```python
def roll_stats(primary_stat: list, worst_stat: list) -> None
```

Roll the stats for the character.

<a id="character.Character.update_skill_for_stat"></a>

#### update\_skill\_for\_stat

```python
def update_skill_for_stat(stat: str, skill_list: list) -> None
```

Update the skill based on the stat.

<a id="character.Character.load_character_from_db"></a>

#### load\_character\_from\_db

```python
def load_character_from_db(char_id: int) -> None
```

Load the character from the database.

