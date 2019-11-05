""" server_database.py: Klasse voor het schrijven naar en lezen uit een sqlite database
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
"""

import datetime
import sqlite3
from pathlib import Path

import constants
import kb_sql
from kbcard import KBCard, Stage


# klasse voor communicatie met de applicatie database (sqlite3)
class ServerDatabase():

    # bepaal het pad van de databasefile (als class-variable, want gedeeld door alle instances van de klasse)
    _dbfile = Path(Path.home(), constants.DB_FILE)

    # constructor
    def __init__(self):

        # probeer een connectie naar de db te maken, als deze nog niet bestaat wordt een nieuwe db-file aangemaakt
        try:
            # verbind naar database
            self._connection = sqlite3.connect(ServerDatabase._dbfile)
            self._connection.row_factory = sqlite3.Row # maakt het mogelijk velden uit db regels op naam te benaderen
            self._cursor = self._connection.cursor()

            # maak tabel als deze nog niet bestaat
            self._cursor.execute(kb_sql.CREATE_CARDS_TABLE)

        # exceptie afhandeling
        except sqlite3.Error as e:
            print("\n" + constants.ERR_DB_CREATION)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')


    # maakt het mogelijk te instantieren met 'with ServerDB'
    def __enter__(self):
        return self


    # sluit de verbinding automatisch wanneer database geinstantieerd was met 'with ServerDB'
    def __exit__(self, ext_type, exc_value, traceback):
        self._cursor.close()
        self._connection.close()

    def _execute(self, sql: str, data: tuple):

        # probeer sql statement uit te voeren
        try:
            if data is None:
                self._cursor.execute(sql)
            else:    
                self._cursor.execute(sql, data)
            
        # exceptie afhandeling
        except sqlite3.Error as e: 
            print("\n" + constants.ERR_DB_INSERTION)    # TODO insertion?
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')


    # voeg nieuw card toe aan de database
    def insertCard(self, card):
        
        self._execute(kb_sql.INSERT_CARD, (card.team, card.project, card.title, card.description, card.stage.value))
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBCREATE, self._cursor.lastrowid, constants.KB_PROMPT), end='')

    # lees card uit de database, returntype: KBCard
    def readCard(self, idnr: int) -> KBCard:
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBREAD, idnr, constants.KB_PROMPT), end='')
        
        # voer sql SELECT uit en lees de eerste regel uit de response
        self._execute(kb_sql.READ_CARD, (idnr, ))
        result = self._cursor.fetchone()
        
        if result is not None:
            # construeer card uit database regel
            card = KBCard()
            card.id = result["id"]
            card.team = result["team"]
            card.project = result["project"]
            card.title = result["title"]
            card.description = result["description"]
            card.stage = Stage(result["stage"])

            return card

        else:
            print("{0}\n{1}".format(constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

    def updateCard(self, new_card: KBCard):
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBUPDATE, new_card.id, constants.KB_PROMPT), end='')

        # lees item uit de db, zodat we altijd hetzelfe update statement kunnen gebruiken dat alle velden overschrijft
        self._execute(kb_sql.READ_CARD, (new_card.id, ))
        original = self._cursor.fetchone()

        # alleen bestaande items updaten
        if original is not None:

            # voer update statement uit, probeer waarde uit inkomende new_card te halen, of als de waarde daar None is gebruik de originele waarde
            self._execute(kb_sql.UPDATE_CARD, (new_card.team or original["team"], new_card.project or original["project"], new_card.title or original["title"], new_card.description or original["description"], new_card.stage.value or Stage(original["stage"]), new_card.id))
        
        else:
            print("{0}\n{1}".format( constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

    def deleteCard(self, idnr: int):

        # voer sql DELETE statement uit
        self._execute(kb_sql.DELETE_CARD, (idnr, ))
        print("{0} :: {1} {2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBDELETE, idnr, constants.KB_PROMPT), end='')

    def selectCards(self, query: tuple) -> list:

        # controleer query
        if len(query) != 2 or type(query[0]) != str or type(query[1]) != str:
            return None

        # voer sql SELECT statement uit
        if query[0] == "" and query[1] == "":
            self._execute(kb_sql.SELECT_ALL, None)
        else:
            self._execute(kb_sql.SELECT_CARDS.format(query[0], query[1]), None)

        # haal db regels op
        rows = self._cursor.fetchall()

        # check óf er resultaten zijn
        if not rows:
            print("{0}\n{1}".format( constants.MSG_SERVER_NORESULT, constants.KB_PROMPT), end='')
            return None

        # gebruikers output
        print("{0} :: {1}{2}\n{3}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_DBSELECT, len(rows), constants.KB_PROMPT), end='')

        # lege lijst voor het eindresultaat
        result = list()

        # maak card objecten van de db regels
        for row in rows:
            # construeer card uit database regel
            card = KBCard()
            card.id = row["id"]
            card.team = row["team"]
            card.project = row["project"]
            card.title = row["title"]
            card.description = row["description"]
            card.stage = Stage(row["stage"])
            # voeg toe aan eindresultaat
            result.append(card)

        return result


    # maakt wijzigingen definitief
    def commit(self):
        self._connection.commit()
