
""" server_listener.py: Asynchrone klasse voor het ontvangen van data via netwerksocket
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 21 okt 2019
"""

from threading import Thread 
from server_incoming import IncomingConnection
import datetime
import constants
import config
import socket

# klasse die overerft van Thread zodat deze op zijn eigen thread geinstantieerd wordt
class ServerListener(Thread):

    # override de run methode die aangeroepen wordt wanneer de thread gestart wordt
    def run(self):

        # with zorgt voor het sluiten van de socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((socket.gethostname(), config.SERVER_PORT))
            s.listen()

            # wacht op inkomende verbindingen
            while True: 
                # inkomende verbinding
                connection, address = s.accept()

                # nieuwe thread starten (aparte thread voor iedere verbinding)
                incoming = IncomingConnection(connection, address)
                incoming.start()
               


       
