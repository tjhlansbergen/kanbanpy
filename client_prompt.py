
""" client_prompt.py: commandline interface voor de kanbanpy applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 15 okt 2019
"""

import client_constants

# klasse voor verwerken van gebruikers commando's
class KanbanpyPrompt:
    def __init__(self):
        self.user_exit = False
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
    
    # hoofd method voor het verwerken van commando's
    def show(self):

        # menu loop
        while self.user_exit == False:

            # toon prompt
            user_in = input(">> ")
            
            # verifier de input, en voer uit         
            method = getattr(self, self.commands.get(user_in, "invalid"), "not_implemented") 
            if(method == "not_implemented"):
                print(client_constants.MSG_NOT_IMPLEMENTED)
            else:
                method()


    # methodes voor menu-opties
    def invalid(self):
        print(client_constants.MSG_UNKNOWN_COMMAND)

    def help(self):
        print(client_constants.MSG_HELP_MSG)

    def exit(self):
        self.user_exit = True

