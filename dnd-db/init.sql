CREATE DATABASE IF NOT EXISTS dnd;
USE dnd;
CREATE TABLE IF NOT EXISTS character_stats (
    id int NOT NULL AUTO_INCREMENT,
    dexterity int DEFAULT NULL,
    strength int DEFAULT NULL,
    constitution int DEFAULT NULL,
    intelligence int DEFAULT NULL,
    wisdom int DEFAULT NULL,
    charisma int DEFAULT NULL,
    PRIMARY KEY (id) );
USE dnd;
CREATE TABLE IF NOT EXISTS character_data (
    id int NOT NULL AUTO_INCREMENT,
    char_name varchar(255),
    dnd_class varchar(255),
    dnd_race varchar(255),
    stat_id int DEFAULT NULL,
    PRIMARY KEY (id));
