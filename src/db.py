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

        stats_sql = f"""
                        INSERT INTO stats (
                            dexterity,
                            strength,
                            constitution,
                            intelligence,
                            wisdom,
                            charisma
                            )
                        VALUES (
                            {character.stats["Dexterity"]},
                            {character.stats["Strength"]},
                            {character.stats["Constitution"]},
                            {character.stats["Intelligence"]},
                            {character.stats["Wisdom"]},
                            {character.stats["Charisma"]}
                            );
                    """
        stat_id = self.insert_into_table(stats_sql)
        character_sql = f"""
                            INSERT INTO character_data (
                                char_name,
                                dnd_class,
                                dnd_race,
                                stat_id
                                )
                            VALUES (
                                {character.name},
                                {character.dnd_class},
                                {character.race},
                                {stat_id}
                                );
                        """
        character_id = self.insert_into_table(character_sql)
        return character_id

    def insert_into_table(self, sql: str) -> int:
        """ Insert into a table. """
        cursor = self.db.cursor(buffered=True)
        use_sql = "USE characters;"
        cursor.execute(use_sql)
        cursor.execute(sql)
        last_id = "SELECT LAST_INSERT_ID();"
        cursor.execute(last_id)
        self.db.commit()
        return cursor.fetchone()[0]
