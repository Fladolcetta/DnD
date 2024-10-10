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
    * [print\_links](#text_printer.TextPrinter.print_links)
    * [print\_single\_value](#text_printer.TextPrinter.print_single_value)
    * [print\_dict\_with\_modifiers](#text_printer.TextPrinter.print_dict_with_modifiers)
    * [print\_dict\_with\_data\_and\_modifiers](#text_printer.TextPrinter.print_dict_with_data_and_modifiers)
    * [print\_modifiers](#text_printer.TextPrinter.print_modifiers)
    * [print\_character](#text_printer.TextPrinter.print_character)
    * [print\_basic\_stats](#text_printer.TextPrinter.print_basic_stats)
    * [print\_race\_info](#text_printer.TextPrinter.print_race_info)
    * [print\_class\_info](#text_printer.TextPrinter.print_class_info)
    * [print\_roll](#text_printer.TextPrinter.print_roll)
    * [print\_home](#text_printer.TextPrinter.print_home)
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
* [character](#character)
  * [Character](#character.Character)
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

<a id="text_printer.TextPrinter.print_links"></a>

#### print\_links

```python
def print_links(links: dict) -> None
```

Print the links.

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

<a id="text_printer.TextPrinter.print_home"></a>

#### print\_home

```python
def print_home(links: dict) -> str
```

Print the home page.

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
def get_primary_stat() -> dict
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

Generate key pairs for the character sheet.

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

<a id="character"></a>

# character

A module to represent a character in Dungeons and Dragons.

<a id="character.Character"></a>

## Character Objects

```python
class Character()
```

A class to represent a character in Dungeons and Dragons.

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
def roll_stats() -> None
```

Roll the stats for the character.

