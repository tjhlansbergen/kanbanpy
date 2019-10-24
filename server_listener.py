
""" server_listener.py: Asynchrone klasse voor het ontvangen van data via netwerksocket
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 22 okt 2019
"""

import datetime
import socket
from threading import Thread 
from server_receiver import ServerReceiver

import constants
import config


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
                incoming = ServerReceiver(connection, address)
                incoming.start()
               


       
