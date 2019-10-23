
""" sql.py: SQL statements voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 21 okt 2019
"""

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

SQL_READ_CARD = """ SELECT * from Cards WHERE id = ?; """

SQL_DELETE_CARD = """ DELETE FROM Cards WHERE id = ?; """