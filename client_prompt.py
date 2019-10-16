
""" client_prompt.py: commandline interface voor de kanbanpy applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

from kbprompt import KBPrompt
from kbcard import KBCard
import constants
import pickle


# implementie van abstracte klasse KBPrompt specifieke 
class ClientPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self.commands = {
            "create card": "ccard",
            "read card": "rcard",
            "update card": "ucard",
            "delete card": "dcard",
            "list board": "lboard",
            "pretty board": "pboard",
            "help": "help",
            "exit": "exit"
        }

    # methodes voor menu-opties
    def help(self):
        print(constants.MSG_HELP_MSG)

    def ccard(self):
        card = KBCard()
        card.fillCard()
        print(pickle.dumps(card))
