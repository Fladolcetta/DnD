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
    character_id = db.insert_character(mock_character.name, mock_character.race, mock_character.dnd_class, mock_character.stats)
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


@patch.dict(os.environ, {"MYSQL_USER": "user", "MYSQL_PASSWORD": "password"}, clear=True)
@patch('src.db.DB.load_character_list')
@patch('mysql.connector')
def test_load_character(mock_connect, mock_load_character_list):
    """Test the load_character method."""
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_connect.connect.return_value = mock_db
    test_id = 42
    fake_id = 1
    test_char_list = [test_id, "Test Character", "Warrior", "Human", 10, 15, 14, 12, 13, 8]
    mock_load_character_list.return_value = [test_char_list]
    test_char_dict = {"id": test_char_list[0],
                      "name": test_char_list[1],
                      "dnd_class": test_char_list[2],
                      "race": test_char_list[3],
                      "stats": {"Dexterity": test_char_list[4],
                                "Strength": test_char_list[5],
                                "Constitution": test_char_list[6],
                                "Intelligence": test_char_list[7],
                                "Wisdom": test_char_list[8],
                                "Charisma": test_char_list[9]}}
    # Create a DB instance
    db = DB()
    # Call the method to test
    nothing = db.load_character(fake_id)
    assert nothing is None
    character = db.load_character(test_id)
    assert character == test_char_dict


@patch.dict(os.environ, {"MYSQL_USER": "user", "MYSQL_PASSWORD": "password"}, clear=True)
@patch('src.db.DB.read_from_table')
@patch('mysql.connector')
def test_load_character_list(mock_connect, mock_read_from_table):
    """Test the load_character_list method."""
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_connect.connect.return_value = mock_db
    test_result = [(1, "Test Character", "Warrior", "Human", 10, 15, 14, 12, 13, 8)]
    mock_read_from_table.return_value = test_result
    # Create a DB instance
    db = DB()
    # Call the method to test
    char_list = db.load_character_list()
    assert char_list is test_result


@patch.dict(os.environ, {"MYSQL_USER": "user", "MYSQL_PASSWORD": "password"}, clear=True)
@patch('mysql.connector')
def test_read_from_table(mock_connect):
    """Test the load_character_list method."""
    # Mock the database connection and cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_connect.connect.return_value = mock_db
    mock_cursor.fetchall.return_value = [[1]]
    # Create a DB instance
    db = DB()
    # Call the method to test
    sql = "TEST;"
    data = db.read_from_table(sql)
    # Assertions
    assert data == [[1]]
    mock_cursor.execute.assert_any_call("USE dnd;")
    mock_cursor.execute.assert_any_call(sql)
    mock_db.commit.assert_called_once()
