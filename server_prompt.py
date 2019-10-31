
""" server_prompt.py: commandline interface voor de kanbanpy server applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 22 okt 2019
"""

import config
import constants
from kbcard import KBCard
from kbprompt import KBPrompt
from server_listener import ServerListener
from server_database import ServerDatabase


# implementie van abstracte klasse KBPrompt 
class ServerPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # start de listener
        listener = ServerListener() # maak een deamon thread van listener zodat deze actief blijf maar stopt als de applicatie stopt
        listener.daemon = True  
        listener.start()
        print(constants.MSG_SERVER_LISTENING, config.SERVER_PORT)

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self.commands = {
            "help": "help",
            "exit": "exit"
        }

    # methodes voor menu-opties
    def help(self):
        print(constants.MSG_SERVER_HELP)


