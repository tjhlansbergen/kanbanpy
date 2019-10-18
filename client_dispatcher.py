
""" client_dispatcher.py: asynchrone klasse voor versturen voor card objecten naar de server
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

from threading import Thread 
from kbcard import KBCard
import constants
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
        self.sendData(dump)

    def sendData(self, data: str):

        # creeer een socket object, verbind naar server en stuur de card als string
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((socket.gethostname(), config.SERVER_PORT))
                s.sendall(data)
                reply = s.recv(1024)

                # controleer de reactie van de server
                if reply.decode() != constants.KB_SUCCES:
                    print("\n{0}\n{1}".format(constants.ERR_RECIEVING_CARD, constants.KB_PROMPT), end='')

        # exceptie verwerking
        except Exception as e:
            print("\n" + constants.ERR_SENDING_CARD)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')



