from threading import Thread
import datetime
import constants

# klasse die overerft van Thread zodat deze op zijn eigen thread geinstantieerd wordt, zodat iedere inkomende verbinding op een eigen thread afgehandeld wordt
class IncomingConnection(Thread):

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

                #TODO verwerk data

                # stuur reply, en sluit de vebinding
                self.connection.sendall(constants.KB_SUCCES.encode())
                self.connection.close()