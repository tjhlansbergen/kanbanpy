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
from kbcard import KBCard, Stage

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
            self.cursor.execute(sql.CREATE_CARDS_TABLE)

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
        
        self._execute(sql.INSERT_CARD, (card.team, card.project, card.title, card.description, card.stage.value))
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBCREATE, self.cursor.lastrowid, constants.KB_PROMPT), end='')

    # lees card uit de database, returntype: KBCard
    def readCard(self, idnr: int) -> KBCard:
        print("{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBREAD, idnr))
        
        # voer sql SELECT uit en lees de eerste regel uit de response
        self._execute(sql.READ_CARD, (idnr, ))
        result = self.cursor.fetchone()
        
        if result is not None:
            # construeer card uit database regel
            card = KBCard()
            card.id = result["id"]
            card.team = result["team"]
            card.project = result["project"]
            card.title = result["title"]
            card.description = result["description"]
            card.stage = Stage(result["stage"])

            print("{0} :: {1}\n{2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_RESULT, constants.KB_PROMPT), end='')
            return card

        else:
            print("{0} :: {1}\n{2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

    def updateCard(self, new_card: KBCard):
        print("{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBUPDATE, new_card.id))

        # lees item uit de db, zodat we altijd hetzelfe update statement kunnen gebruiken dat alle velden overschrijft
        self._execute(sql.READ_CARD, (new_card.id, ))
        original = self.cursor.fetchone()

        # alleen bestaande items updaten
        if original is not None:

            # voer update statement uit, probeer waarde uit inkomende new_card te halen, of als de waarde daar None is gebruik de originele waarde
            self._execute(sql.UPDATE_CARD, (new_card.team or original["team"], new_card.project or original["project"], new_card.title or original["title"], new_card.description or original["description"], new_card.stage.value or Stage(original["stage"]), new_card.id))
        
        else:
            print("{0} :: {1}\n{2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

    def deleteCard(self, idnr: int):

        # voer sql DELETE statement uit
        self._execute(sql.DELETE_CARD, (idnr, ))
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBDELETE, idnr, constants.KB_PROMPT), end='')


    # maakt wijzigingen definitief
    def commit(self):
        self.connection.commit()
