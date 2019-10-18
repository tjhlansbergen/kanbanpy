
""" server_listener.py: Asynchrone klasse voor het ontvangen van data via netwerksocket
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 18 okt 2019
"""

from threading import Thread 
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
                print("listening")
                connection, address = s.accept()
                print("Connection coming from: ", address)
                data = connection.recv(1024)
                print("Data:\n", data)  # TODO kan weg

                # stuur reply, en sluit de vebinding
                connection.sendall(constants.KB_SUCCES.encode())
                connection.close()
