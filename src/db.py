""" A module for the database connection. """
import os
import mysql.connector
from src.character import Character


class DB:
    """ A class to represent a database connection. """
    def __init__(self):
        self.host = "dnd-db"
        self.user = os.environ["MYSQL_USER"]
        self.password = os.environ["MYSQL_PASSWORD"]
        self.db = mysql.connector.connect(host=self.host,
                                          port=3306,
                                          user=self.user,
                                          password=self.password)

    def insert_character(self, character: Character) -> int:
        """ Insert a character into the database. """
        stats_sql = "INSERT INTO character_stats (dexterity, strength, constitution, intelligence, wisdom, charisma) VALUES ( %s, %s, %s, %s, %s, %s);"
        stats_data = (character.stats["Dexterity"],
                      character.stats["Strength"],
                      character.stats["Constitution"],
                      character.stats["Intelligence"],
                      character.stats["Wisdom"],
                      character.stats["Charisma"])
        stat_id = self.insert_into_table(stats_sql, stats_data)
        stat_id = 1
        character_sql = "INSERT INTO character_data (char_name, dnd_class, dnd_race, stat_id) VALUES (%s, %s, %s, %s);"
        character_data = (character.name, character.dnd_class, character.race, stat_id)
        character_id = self.insert_into_table(character_sql, character_data)
        return character_id

    def insert_into_table(self, sql: str, data: list) -> int:
        """ Insert into a table. """
        cursor = self.db.cursor(buffered=True)
        use_sql = "USE dnd;"
        cursor.execute(use_sql)
        cursor.execute(sql, data)
        last_id = "SELECT LAST_INSERT_ID();"
        cursor.execute(last_id)
        self.db.commit()
        return cursor.fetchone()[0]

    def load_character_list(self) -> list:
        """ Load the character list"""
        fake = [["1", "Frank", "Human", "Barbarian", "1", "2", "3", "4", "5", "6"],
                ["2", "Steve", "Human", "Barbarian", "1", "2", "3", "4", "5", "6"],
                ["3", "Jimmy", "Human", "Barbarian", "1", "2", "3", "4", "5", "6"]]
        return fake
