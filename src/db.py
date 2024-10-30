""" A module for the database connection. """
import os
import mysql.connector


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

    def insert_character(self, name: str, race: str, dnd_class: str, stats: dict) -> int:
        """ Insert a character into the database. """
        stats_sql = "INSERT INTO character_stats (dexterity, strength, constitution, intelligence, wisdom, charisma) VALUES ( %s, %s, %s, %s, %s, %s);"
        stats_data = (stats["Dexterity"],
                      stats["Strength"],
                      stats["Constitution"],
                      stats["Intelligence"],
                      stats["Wisdom"],
                      stats["Charisma"])
        stat_id = self.insert_into_table(stats_sql, stats_data)
        character_sql = "INSERT INTO character_data (char_name, dnd_class, dnd_race, stat_id) VALUES (%s, %s, %s, %s);"
        character_data = (name, dnd_class, race, stat_id)
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

    def read_from_table(self, sql: str) -> list:
        """ Read data from the db. """
        cursor = self.db.cursor(buffered=True)
        use_sql = "USE dnd;"
        cursor.execute(use_sql)
        cursor.execute(sql)
        self.db.commit()
        return cursor.fetchall()

    def load_character_list(self) -> list:
        """ Load the character list"""
        sql = "SELECT cd.id, cd.char_name, cd.dnd_class, cd.dnd_race, \
                      cs.dexterity, cs.strength, cs.constitution, cs.intelligence, cs.wisdom, cs.charisma \
              FROM character_data AS cd \
              LEFT JOIN character_stats AS cs\
              ON cd.stat_id = cs.id \
              ORDER BY cd.id;"
        test = self.read_from_table(sql)
        return test
