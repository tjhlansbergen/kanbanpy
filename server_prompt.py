
""" server_prompt.py: commandline interface voor de kanbanpy server applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 17 okt 2019
"""

from kbprompt import KBPrompt
import constants


# implementie van abstracte klasse KBPrompt 
class ServerPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self.commands = {
            "test": "test",
            "exit": "exit"
        }

    def test(self):
        print('server says hi')
        
