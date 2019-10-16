
""" client_dispatcher.py: asynchrone klasse voor versturen voor card objecten naar de server
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

from threading import Thread 
from kbcard import KBCard
import config
import pickle
import socket


# klasse die overerft van Thread zodat deze op zijn eigen thread geinstantieerd wordt
class ClientDispatcher(Thread):

    # override de constructor om parameter (het card object) aan de klasse mee te kunnen geven
    def __init__(self, card: KBCard):
        Thread.__init__(self)
        self.card = card

    # override de run methode die aangeroepen wordt wanneer de thread gestart wordt
    def run(self):

        # creeer pickle als string
        dump = pickle.dumps(self.card)

        # verstuur naar server
        result = self.sendData(dump)

    def sendData(self, data: str) -> bool:
        
        # creeer een socket object, verbind naar server en stuur de card als string
        # TODO exception handling!!
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((socket.gethostname(), config.SERVER_PORT))
            s.sendall(data)
            reply = s.recv(1024)

        print('Received', repr(reply))

        #TODO return afhankelijk van reply
        return True