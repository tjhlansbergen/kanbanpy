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
    def __init__(self):

        # bepaal het pad van de databasefile
        self.dbfile = Path(Path.home(), constants.DB_FILE)

        # check of er al een database bestaat, anders maak deze aan
        if not self.dbfile.is_file():
            self.createDB()

    def createDB(self):

        # probeer een connectie naar de db te maken, als deze nog niet bestaat wordt een nieuwe db-file aangemaakt
        # en creeer de benodigde tabel
        try:
            # verbind naar database
            dbconnection = sqlite3.connect(self.dbfile)
            
            # maak tabel
            cursor = dbconnection.cursor()
            cursor.execute(config.SQL_CREATE_CARDS_TABLE)

        # exceptie afhandeling
        except sqlite3.Error as e:
            print("\n" + constants.ERR_CREATING_DB)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')

        # sluit de connection (ongeacht evt. foutmeldingen)    
        finally:
            if dbconnection:
                dbconnection.close()
