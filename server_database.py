""" server_database.py: Klasse voor het schrijven naar en lezen uit een sqlite database
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 19 okt 2019
"""

from pathlib import Path
import sqlite3
import constants
import config

class ServerDB():

    # bepaal het pad van de databasefile (als class-variable, want gedeeld door alle instances van de klasse)
    dbfile = Path(Path.home(), constants.DB_FILE)

    def __init__(self):

        # probeer een connectie naar de db te maken, als deze nog niet bestaat wordt een nieuwe db-file aangemaakt
        try:
            # verbind naar database
            self.connection = sqlite3.connect(ServerDB.dbfile)
            self.cursor = self.connection.cursor()

            # maak tabel als deze nog niet bestaat
            self.cursor.execute(config.SQL_CREATE_CARDS_TABLE)

        # exceptie afhandeling
        except sqlite3.Error as e:
            print("\n" + constants.ERR_DB_CREATION)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')


    # maakt het mogelijk te instantieren met 'with ServerDB'
    def __enter__(self):
        return self


    # sluit de verbinding automatisch wanneer database geinstantieerd was met 'with ServerDB'
    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        self.connection.close()


    # voeg nieuw card toe aan de database
    # return type: int, retourneert de automatisch opgehoogde id van de database regel
    def insertCard(self, card) -> int:

        # probeer sql INSERT INTO commando uit te voeren
        try:
            self.cursor.execute(config.SQL_INSERT_CARD, card.team, card.project, card.title, card.description, card.stage)
            return self.cursor.lastrowid
        
        # exceptie afhandeling
        except Exception as e: #sqlite3.Error
            print("\n" + constants.ERR_DB_INSERTION)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')
            return None


    # maakt wijzigingen definitief
    def commit(self):
        self.connection.commit()
