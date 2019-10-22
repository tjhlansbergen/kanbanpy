
""" client_dispatcher.py: asynchrone klasse voor versturen voor card objecten naar de server
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

import pickle
import socket
from threading import Thread 

import config
import constants
from kbcard import KBCard


# klasse die overerft van Thread zodat deze op zijn eigen thread geinstantieerd wordt
class ClientDispatcher(Thread):

    # override de constructor om parameter aan de klasse mee te kunnen geven
    def __init__(self, request: tuple):
        Thread.__init__(self)
        self.request = request

    # override de run methode die aangeroepen wordt wanneer de thread gestart wordt
    def run(self):

        # creeer pickle als string
        dump = pickle.dumps(self.request)

        # verstuur naar server
        self.sendData(dump)

    def sendData(self, data: str):

        # creeer een socket object, verbind naar server en stuur de request als string
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((socket.gethostname(), config.SERVER_PORT))
                s.sendall(data)
                reply = s.recv(1024)

                # controleer de reactie van de server # TODO voor de verschillende requests (wellicht beter returnen?)
                if reply.decode() != constants.KB_OK:
                    print("\n{0}\n{1}".format(constants.ERR_RECEIVING_REQUEST, constants.KB_PROMPT), end='')

        # exceptie verwerking
        except Exception as e:
            print("\n" + constants.ERR_SENDING_REQUEST)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')



