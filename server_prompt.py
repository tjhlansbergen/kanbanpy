
""" server_prompt.py: commandline interface voor de kanbanpy server applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 17 okt 2019
"""

from server_listener import ServerListener
from server_database import ServerDB
from kbprompt import KBPrompt
from kbcard import KBCard
import constants
import config


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
            "test insert": "testi",
            "help": "help",
            "exit": "exit"
        }

    # methodes voor menu-opties
    def help(self):
        print(constants.MSG_SERVER_HELP)

    def testi(self):
        card = KBCard()
        card.title = "test_title"
        card.team = "test team"
        card.project = "test project"
        card.description = "some descriptive text"

        with ServerDB() as db:
            id = db.insertCard(card)
            db.commit()

        if id is not None:
            print('card inserted with ID: ', id)

        
