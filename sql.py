
""" sql.py: SQL statements voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
"""

CREATE_CARDS_TABLE = """ CREATE TABLE IF NOT EXISTS Cards (
                                id INTEGER PRIMARY KEY, 
                                team TEXT,
                                project TEXT,
                                title TEXT NOT NULL,
                                description TEXT,
                                stage INTEGER NOT NULL
                                ); """

INSERT_CARD = """ INSERT INTO Cards (
                                team,
                                project,
                                title,
                                description,
                                stage)
                                VALUES (?,?,?,?,?); """

UPDATE_CARD = """ UPDATE Cards SET
                                team = ?,
                                project = ?,
                                title = ?,
                                description = ?,
                                stage = ?
                                WHERE id = ?; """
                                
READ_CARD = """ SELECT * FROM Cards WHERE id = ?; """

DELETE_CARD = """ DELETE FROM Cards WHERE id = ?; """

SELECT_CARDS = """ SELECT * FROM Cards WHERE {0} = {1}; """

SELECT_ALL = """ SELECT * FROM Cards; """