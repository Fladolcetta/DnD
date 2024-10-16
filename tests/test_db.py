"""Tests for the DB class."""
import os
from unittest.mock import patch, MagicMock
from src.db import DB


@patch.dict(os.environ, {"MYSQL_USER": "user", "MYSQL_PASSWORD": "password"}, clear=True)
@patch('mysql.connector')
def test_insert_into_table(mock_connect):
    """Test the insert_into_table method."""
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.connect.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = [1]  # Mock the last insert ID

    # Create a DB instance
    db = DB()

    # Call the method to test
    sql = "INSERT INTO some_table (column1, column2) VALUES (%s, %s);"
    data = ("value1", "value2")
    last_id = db.insert_into_table(sql, data)

    # Assertions
    assert last_id == 1
    mock_cursor.execute.assert_any_call("USE dnd;")
    mock_cursor.execute.assert_any_call(sql, data)
    mock_db.commit.assert_called_once()


@patch.dict(os.environ, {"MYSQL_USER": "user", "MYSQL_PASSWORD": "password"}, clear=True)
@patch('mysql.connector.connect')
@patch('src.character.Character')
@patch('src.db.DB.insert_into_table')
def test_insert_character(mock_insert, mock_character, mock_connect):
    """Test the insert_character method."""
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = [1]  # Mock the last insert ID

    # Mock the character
    mock_character.name = "Test Character"
    mock_character.dnd_class = "Warrior"
    mock_character.race = "Human"
    mock_character.stats = {
        "Dexterity": 10,
        "Strength": 15,
        "Constitution": 14,
        "Intelligence": 12,
        "Wisdom": 13,
        "Charisma": 8
    }

    # Mock the insert_into_table method
    mock_insert.side_effect = [1, 1]

    # Create a DB instance
    db = DB()

    # Call the method to test
    character_id = db.insert_character(mock_character)

    # Assertions
    assert character_id == 1
    assert mock_insert.call_count == 2
    assert mock_insert.call_args_list[0][0] == (
        "INSERT INTO character_stats (dexterity, strength, constitution, intelligence, wisdom, charisma) VALUES ( %s, %s, %s, %s, %s, %s);",
        (10, 15, 14, 12, 13, 8)
    )
    assert mock_insert.call_args_list[1][0] == (
        "INSERT INTO character_data (char_name, dnd_class, dnd_race, stat_id) VALUES (%s, %s, %s, %s);",
        ("Test Character", "Warrior", "Human", 1)
    )
