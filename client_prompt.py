
""" client_prompt.py: commandline interface voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
"""

import pickle

import constants
from client_dispatcher import ConsoleDispatcher, BoardDispatcher
from kbboards import ProjectBoard, TeamBoard, TeamProjectBoard
from kbcard import KBCard, Stage
from kbprompt import KBPrompt


# implementie van abstracte klasse KBPrompt
class ClientPrompt(KBPrompt):
    
    # constructor
    def __init__(self):

        # initieer de super klasse
        super().__init__()

        # en de commando's specifiek voor deze implementatie
        self._commands = {
            "test": "test",
            "create card": "ccard",
            "read card": "rcard",
            "move card": "mcard",
            "delete card": "dcard",
            "list cards": "lcards",
            "show board": "sboard",
            "refresh board": "rboard",
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
        dispatcher = ConsoleDispatcher(("create", card))
        dispatcher.start()

    def rcard(self):

        # vraag de user om het card nummer
        user_in = input(constants.INP_CARDNUMBER)
        if user_in.isdigit():
            idnr = int(user_in)
        else:
            print(constants.MSG_CLIENT_INVALID_CARDNUMBER)
            return
            
        # start de dispatcher (op zijn eigen thread), en verzend het verzoek naar de server
        dispatcher = ConsoleDispatcher(("read", idnr))
        dispatcher.start()

    def mcard(self):

        # vraag de user om het card nummer en stage
        id_in = input(constants.INP_CARDNUMBER)
        stage_in = input(constants.INP_STAGE).upper()
        
        if id_in.isdigit():
            idnr = int(id_in)          
        else:
            print(constants.MSG_CLIENT_INVALID_CARDNUMBER)
            return  

        if stage_in in Stage.__members__:
            stage = Stage[stage_in]
        else:
            print(constants.MSG_CLIENT_INVALID_STAGE)
            return

        # construeer card met gewijzigde waarde voor stage, maak andere velden None om de originele waarde te behouden
        card = KBCard()
        card.id = idnr
        card.stage = stage
        card.title = None
        card.team = None
        card.project = None
        card.description = None

        # start de dispatcher (op zijn eigen thread), en verzend het verzoek naar de server
        dispatcher = ConsoleDispatcher(("update", card))
        dispatcher.start()

    def dcard(self):

        # vraag de user om het card nummer
        user_in = input(constants.INP_CARDNUMBER)
        if user_in.isdigit():
            idnr = int(user_in)
        else:
            return  # faal zonder feedback, de gebruiker kan zelf ook wel bedenken dat hij hier een getal in moet vullen

        # start de dispatcher (op zijn eigen thread), en verzend het verzoek naar de server
        dispatcher = ConsoleDispatcher(("delete", idnr))
        dispatcher.start()

    def lcards(self):

        dispatcher = ConsoleDispatcher(("select", ("","")))
        dispatcher.start()


    def sboard(self):

        # vraag gebruiker om team en/of project
        user_team = input(constants.INP_TEAM).lower()
        user_project = input(constants.INP_PROJECT).lower()
        if user_team == "" and user_project == "":
            print(constants.MSG_CLIENT_NO_TEAMORPROJECT)
            return

        board = None

        # check type board
        if user_team == "":

            # project board
            board = ProjectBoard(user_project)

        elif user_project == "":

            # team board
            board = TeamBoard(user_team)

        else:

            # TeamProjectBoard
            board = TeamProjectBoard(user_team, user_project)

        if board is not None:
            dispatcher = BoardDispatcher(board, True)
            dispatcher.start()

    def rboard(self):

        # vraag gebruiker om team en/of project
        user_team = input(constants.INP_TEAM).lower()
        user_project = input(constants.INP_PROJECT).lower()
        if user_team == "" and user_project == "":
            print(constants.MSG_CLIENT_NO_TEAMORPROJECT)
            return

        board = None

        # check type board
        if user_team == "":

            # project board
            board = ProjectBoard(user_project)

        elif user_project == "":

            # team board
            board = TeamBoard(user_team)

        else:

            # TeamProjectBoard
            board = TeamProjectBoard(user_team, user_project)

        if board is not None:
            dispatcher = BoardDispatcher(board, False)
            dispatcher.start()



