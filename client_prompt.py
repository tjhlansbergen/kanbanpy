
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
            "read card": "rcard",
            "move card": "mcard",
            "delete card": "dcard",
            "list cards": "lcards",
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
        dispatcher = ClientDispatcher(("create", card))
        dispatcher.start()

    def rcard(self):

        # vraag de user om het card nummer
        user_in = input(constants.INP_CARDNUMBER)
        if user_in.isdigit():
            idnr = int(user_in)
        else:
            return  # faal zonder feedback, de gebruiker kan zelf ook wel bedenken dat hij hier een getal in moet vullen

        # start de dispatcher (op zijn eigen thread), en verzend het verzoek naar de server
        dispatcher = ClientDispatcher(("read", idnr))  # TODO vraag user input
        dispatcher.start()

    def dcard(self):

        # vraag de user om het card nummer
        user_in = input(constants.INP_CARDNUMBER)
        if user_in.isdigit():
            idnr = int(user_in)
        else:
            return  # faal zonder feedback, de gebruiker kan zelf ook wel bedenken dat hij hier een getal in moet vullen

        # start de dispatcher (op zijn eigen thread), en verzend het verzoek naar de server
        dispatcher = ClientDispatcher(("delete", idnr))  # TODO vraag user input
        dispatcher.start()

    # test methode voor het aanmaken en versturen van een card
    def test(self):
        card = KBCard()
        card.title = "test_title"
        card.team = "test team"
        card.project = "test project"
        card.description = "some descriptive text"
        dispatcher = ClientDispatcher(("create", card))
        dispatcher.start()
        
