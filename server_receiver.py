
""" server_receiver.py: Asynchrone klasse voor verwerking van inkomende data
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
"""

import datetime
import pickle
from threading import Thread

import config
import constants
from kbcard import KBCard
from server_database import ServerDatabase

# klasse die overerft van Thread waardoor deze op zijn eigen thread geinstantieerd wordt, zodat iedere inkomende verbinding op een eigen thread afgehandeld wordt
# Interface: de ServerReceiver kan de volgende data verwerken:
#
# ("create", <Card>)    - voegt een Card object toe aan de database
# ("read", <Int>)       - retourneert het card object met de corresponderende ID indien aanwezig, anders -1
# ("update", <Card>)    - Indien Card object met corresponderend ID bestaat wordt deze bijgewerkt.
# ("delete", <Int>)     - Verwijder Card object uit de database met corresponderend ID indien aanwezig.
# ("select", <Tuple>)   - retourneert het resultaat van de query in de tupel of None bij geen resultaat
#
class ServerReceiver(Thread):

    def __init__(self, connection, address):
        Thread.__init__(self)
        self.address = address
        self.connection = connection
    
    # override de run methode die aangeroepen wordt wanneer de thread gestart wordt
    def run(self):

                print("\n{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_INCOMING, self.address))

                # ontvang de data
                data = self.connection.recv(1024)
                print("{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), len(data), constants.MSG_SERVER_DATARECEIVED))

                # data deserializeren
                request = pickle.loads(data)

                # controleer inkomende data
                if type(request) != tuple or request[0] not in config.INTERFACE_COMMANDS:

                    # stuur géén reply, sluit de vebinding en stop uitvoering
                    self.connection.close()
                    return
    
                # selecteer juiste methode voor verdere verwerking
                method = getattr(self, request[0], "not_implemented") 
                if(method == "not_implemented"):
                    print(constants.MSG_NOT_IMPLEMENTED)
                else:
                    # roep de gekozen methode aan
                    type_ok = method(request[1])

                    if type_ok == False:
                        print("{0}\n{1}".format(constants.MSG_SERVER_INCORRECTTYPE, constants.KB_PROMPT), end='')     

                    # en sluit de vebinding
                    self.connection.close()

    # mapping van interface methode naar database methode
    def create(self, payload) -> bool:
        
        # controleer inkomende data
        if type(payload) != KBCard:
            return False

        # voeg toe aan database
        with ServerDatabase() as db:
            db.insertCard(payload)
            db.commit()

        # stuur reply
        self.connection.sendall(constants.KB_OK.encode())
        return True

            


    def read(self, payload) -> bool:
        
        # controleer inkomende data
        if type(payload) != int:
            return False

        # lees uit database
        with ServerDatabase() as db:
            card = db.readCard(payload)
            
        # stuur card als reply
        self.connection.sendall(pickle.dumps(card))
        return True


    def update(self, payload) -> bool:
        
        # controleer inkomende data
        if type(payload) != KBCard:
            return False

        # update in database
        with ServerDatabase() as db:
            db.updateCard(payload)
            db.commit()

        # stuur reply
        self.connection.sendall(constants.KB_OK.encode())
        return True


    def delete(self, payload):

        # controleer inkomende data
        if type(payload) != int:
            return False

        # verwijder uit database
        with ServerDatabase() as db:
            db.deleteCard(payload)
            db.commit()
        
        # stuur reply
        self.connection.sendall(constants.KB_OK.encode())
        return True

    def select(self, payload) -> bool:

        # controleer inkomende data
        if type(payload) != tuple:
            return False
        if len(payload) != 2:
            return False
        if type(payload[0]) != str or type(payload[1]) != str:
            return False

        # lees uit database
        with ServerDatabase() as db:
            cards = db.selectCards(payload)
            
        # stuur card als reply
        self.connection.sendall(pickle.dumps(cards))
        return True
