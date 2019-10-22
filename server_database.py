""" server_database.py: Klasse voor het schrijven naar en lezen uit een sqlite database
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 19 okt 2019
"""

import datetime
import sqlite3
from pathlib import Path

import constants
import sql
from kbcard import KBCard

class ServerDatabase():

    # bepaal het pad van de databasefile (als class-variable, want gedeeld door alle instances van de klasse)
    dbfile = Path(Path.home(), constants.DB_FILE)

    def __init__(self):

        # probeer een connectie naar de db te maken, als deze nog niet bestaat wordt een nieuwe db-file aangemaakt
        try:
            # verbind naar database
            self.connection = sqlite3.connect(ServerDatabase.dbfile)
            self.connection.row_factory = sqlite3.Row # maakt het mogelijk velden uit db regels op naam te benaderen
            self.cursor = self.connection.cursor()

            # maak tabel als deze nog niet bestaat
            self.cursor.execute(sql.SQL_CREATE_CARDS_TABLE)

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

    def _execute(self, sql: str, data: tuple):

        # probeer sql statement uit te voeren
        try:
            self.cursor.execute(sql, data)
            
        # exceptie afhandeling
        except sqlite3.Error as e: 
            print("\n" + constants.ERR_DB_INSERTION)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')


    # voeg nieuw card toe aan de database
    def insertCard(self, card):
        
        self._execute(sql.SQL_INSERT_CARD, (card.team, card.project, card.title, card.description, card.stage))
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBCREATE, self.cursor.lastrowid, constants.KB_PROMPT), end='')

    # lees card uit de database, returntype: KBCard
    def readCard(self, idnr: int) -> KBCard:
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBREAD, idnr, constants.KB_PROMPT), end='')
        
        # voer sql SELECT uit en lees de eerste regel uit de response
        self._execute(sql.SQL_READ_CARD, (idnr, ))
        result = self.cursor.fetchone()
        
        if result is not None:
            # construeer card uit database regel
            card = KBCard()
            card.id = result["id"]
            card.team = result["team"]
            card.project = result["project"]
            card.title = result["title"]
            card.description = result["description"]
            card.stage = result["stage"]

            return card

        else:
            print("{0} :: {1}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

    #TODO update en delete
    

    # maakt wijzigingen definitief
    def commit(self):
        self.connection.commit()
