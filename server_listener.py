
""" server_listener.py: Asynchrone klasse voor het ontvangen van data via netwerksocket
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 21 okt 2019
"""

from threading import Thread 
import datetime
import constants
import config
import socket

# klasse die overerft van Thread zodat deze op zijn eigen thread geinstantieerd wordt
class ServerListener(Thread):

    # override de run methode die aangeroepen wordt wanneer de thread gestart wordt
    def run(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((socket.gethostname(), config.SERVER_PORT))
            s.listen()

            while True: # TODO constant strings
                # inkomende verbinding
                connection, address = s.accept()

                # TODO nieuwe thread vanaf hier starten voor iedere verbinding?

                print("\n{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), constants.MSG_SERVER_INCOMING, address))

                # ontvang de data
                data = connection.recv(1024)
                print("{0} :: {1} {2}".format(datetime.datetime.now().strftime("%d %b %H:%M:%S"), len(data), constants.MSG_SERVER_DATARECEIVED))

                #TODO verwerk data

                # stuur reply, en sluit de vebinding
                connection.sendall(constants.KB_SUCCES.encode())
                connection.close()

       
