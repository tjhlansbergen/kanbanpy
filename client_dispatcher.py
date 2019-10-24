
""" client_dispatcher.py: asynchrone klasse voor versturen voor card objecten naar de server
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
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

        # voorkom het versturen van bad request vanaf client-zijde
        if type(self.request) != tuple or self.request[0] not in config.INTERFACE_COMMANDS:
            print("{0}\n{1}".format(constants.ERR_SENDING_REQUEST, constants.KB_PROMPT), end='')
            return

        # creeer pickle als string
        dump = pickle.dumps(self.request)

        # verstuur naar server
        reply = self.sendData(dump)

        # verwerk antwoord
        self.receiveData(reply)

    def sendData(self, data: str):

        # return variabele
        reply = None

        # creeer een socket object, verbind naar server en stuur de request als string
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((socket.gethostname(), config.SERVER_PORT))
                s.sendall(data)
                reply = s.recv(1024)

        # exceptie verwerking
        except Exception as e:
            print("\n" + constants.ERR_SENDING_REQUEST)
            print("{0}\n{1}".format(e, constants.KB_PROMPT), end='')

        return reply

    def receiveData(self, data):

        # controleer input
        if data is None:
            return

        # check soort request
        if self.request[0] == "read":

            # controleer de reactie van de server
            card = pickle.loads(data)
            if type(card) != KBCard:
                print("\n{0}\n{1}".format(constants.MSG_CLIENT_NOCARD, constants.KB_PROMPT), end='')
                return

            # toon resultaat aan gebruiker
            print("{0}\n{1}".format(card.print(), constants.KB_PROMPT), end='')

        elif self.request[0] == "listall":

            # controleer de reactie van de server
            cards = pickle.loads(data)
            if type(cards) != list:
                print("\n{0}\n{1}".format(constants.MSG_CLIENT_NOCARD, constants.KB_PROMPT), end='')
                return

            if type(cards[0]) != KBCard:
                print("\n{0}\n{1}".format(constants.MSG_CLIENT_NOCARD, constants.KB_PROMPT), end='')
                return

            # toon resultaat aan gebruiker
            print("\n")
            for card in cards:
                print(card.listprint())

            print("\n{}".format(constants.KB_PROMPT), end='')

        else:   # create, update, delete
            # controleer de reactie van de server
            if data.decode() != constants.KB_OK:
                print("\n{0}\n{1}".format(constants.ERR_RECEIVING_REQUEST, constants.KB_PROMPT), end='')



