
""" config.py: Default configuratie voor de kanbanpy applicatie en methode voor het aanpassen van de config
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 31 okt 2019
"""

import configparser

MAX_TITLE_LENGTH = 20
MAX_DESCRIPTION_LENGTH = 250

CONFIG_FILE = "kanbanpy.config"
# onderstaande instellingen kunnen overschreven worden in een config bestand met naam zoals hierboven geconfigureerd
SERVER_HOSTNAME = ""
SERVER_PORT = 65432

# functie voor het inladen van configuratie uit een .config bestand
def loadConfig(path: str):

    # try voor exceptie afhandeling
    try:    

        # gebruikers feedback
        print("Looking for configuration in:", path)

        # open bestand en sluit automatisch na lezen
        with open(path, 'r') as cfgfile:

            # lees bestand                
            cfgcontent = cfgfile.read()
            if len(cfgcontent) == 0:
                print("Config file found, but it is empty")
                return

            # gebruikers feedback
            print("Config file found, will try to read from it")

            # initialiseer parser en lees key/values pairs uit 
            cfgparser = configparser.ConfigParser()     
            cfgparser.read_string(cfgcontent)           

            # maak de global variablen aanpasbaar met het global keyword, en ken de juiste waarde toe uit de config
            global SERVER_HOSTNAME, SERVER_PORT
            SERVER_HOSTNAME = cfgparser['connectivity'].get('SERVER_HOSTNAME', fallback=SERVER_HOSTNAME)
            SERVER_PORT = cfgparser['connectivity'].getint('SERVER_PORT', fallback=SERVER_PORT)
 
    except Exception:
        print("Config file not found or unfit for reading, will continue with default configuration.")


