
""" main.py: Entrypoint van de kanbanpy applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 15 okt 2019
"""

import os
import constants
from client_prompt import ClientPrompt
from server_prompt import ServerPrompt

# klasse voor kanbanpy applicatie
class kanbanpy:

    # hoofdfunctie, entrypoint van de applicatie
    def main(self):

        # keuze client/server
        context = ''
        while (context == ''):
            user_in = input(constants.INP_SERVER_CLIENT).lower()
            if user_in.startswith('s'):
                context = "SERVER" 
            elif user_in.startswith('c'):
                context = "CLIENT"
            
        # scherm vrijnmaken en applicatienaam + versie + context weergeven 
        os.system('cls||clear')
        print(constants.APP_NAME, constants.APP_VERSION, context)

        # server of client starten
        if context == "SERVER":
            # server, toon events
            server = ServerPrompt()
            server.show()

        elif context == "CLIENT":
            # client, toon de applicatie input-prompt
            client = ClientPrompt()
            client.show()


if __name__ == "__main__":
    app = kanbanpy()
    app.main()