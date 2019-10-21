
""" kbprompt.py: abstracte klasse voor commandline prompt voor de kanbanpy applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

from abc import ABC, abstractmethod # ten behoeve van abstracte klasse (Abstract Base Class)
import constants

# abstracte klasse voor verwerken van gebruikers commando's
class KBPrompt(ABC):

    # constructor
    def __init__(self):
        self.user_exit = False
        self.commands = {}
    
    # hoofd methode voor het verwerken van commando's
    def show(self):

        # menu loop
        while self.user_exit == False:

            # toon prompt
            user_in = input(constants.KB_PROMPT)
            
            # verifier de input, en voer uit         
            method = getattr(self, self.commands.get(user_in, "invalid"), "not_implemented") 
            if(method == "not_implemented"):
                print(constants.MSG_NOT_IMPLEMENTED)
            else:
                # roep de gekozen methode aan
                method()

    # globale methodes voor menu-opties
    def invalid(self):
        print(constants.MSG_UNKNOWN_COMMAND)

    def exit(self):
        self.user_exit = True

