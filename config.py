
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

SQL_CREATE_CARDS_TABLE = """ CREATE TABLE IF NOT EXISTS Cards (
                                        id integer PRIMARY KEY,
                                        data text NOT NULL
                                    ); """