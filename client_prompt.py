
""" client_prompt.py: commandline interface voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

import pickle

import constants
from client_dispatcher import ClientDispatcher
from kbcard import KBCard
from kbprompt import KBPrompt




# implementie van abstracte klasse KBPrompt
class ClientPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self.commands = {
            "test": "test",
            "create card": "ccard",
            "move card": "mcard",
            "list board": "lboard",
            "pretty board": "pboard",
            "help": "help",
            "exit": "exit"
        }

    # methodes voor menu-opties
    def help(self):
        print(constants.MSG_CLIENT_HELP)

    def ccard(self):
        # maak en vul een card object
        card = KBCard()
        card.fillCard()

        # start de dispatcher (op zijn eigen thread), en verzend de card naar de server
        dispatcher = ClientDispatcher(card)
        dispatcher.start()

    # test methode voor het aanmaken en versturen van een card
    def test(self):
        card = KBCard()
        card.title = "test_title"
        card.team = "test team"
        card.project = "test project"
        card.description = "some descriptive text"
        dispatcher = ClientDispatcher(card)
        dispatcher.start()
        
