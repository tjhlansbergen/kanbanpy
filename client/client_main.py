
""" client_main.py: Entrypoint van de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 15 okt 2019
"""

import os
import client_constants

# hoofdfunctie, entrypoint van de client applicatie
def main():
    
    os.system('cls||clear')
    print(client_constants.APP_NAME, client_constants.APP_VERSION)

if __name__ == "__main__":
    main()