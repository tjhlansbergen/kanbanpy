
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


# implementie van abstracte klasse KBPrompt 
class ServerPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self.commands = {
            "test insert": "testi",
            "listen": "listen",
            "exit": "exit"
        }

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

    def listen(self):
        listener = ServerListener()
        # maak een deamon thread van listener zodat deze actief blijf maar stopt als de applicatie stopt
        listener.daemon = True  
        listener.start()
        
