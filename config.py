
""" config.py: Configuratie voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

MAX_TITLE_LENGTH = 20
MAX_DESCRIPTION_LENGTH = 250

SERVER_HOSTNAME = ""
SERVER_PORT = 65432

# SQL
SQL_CREATE_CARDS_TABLE = """ CREATE TABLE IF NOT EXISTS Cards (
                                id INTEGER PRIMARY KEY, 
                                team TEXT,
                                project TEXT,
                                title TEXT NOT NULL,
                                description TEXT,
                                stage INTEGER NOT NULL
                                ); """

SQL_INSERT_CARD = """ INSERT INTO Cards (
                                team,
                                project,
                                title,
                                description,
                                stage)
                                VALUES (?,?,?,?,?); """