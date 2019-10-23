""" kbcard.py: card klasse, representeert één card op het kanban board
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 16 okt 2019
"""

from enum import Enum

import config
import constants

# enum voor de verschillende statussen die card kunnen hebben
class Stage(Enum):
    HOLD = 1
    BACKLOG = 2
    DOING = 3
    TESTING = 4
    DOCUMENTING = 5
    DELIVERING = 6
    DONE = 7

# klasse voor het object Card, de kaartjes op het kanbanbord
class KBCard():

    # constructor
    def __init__(self):
        self.id = None
        self.team = ""
        self.project = ""
        self.title = ""
        self.description = ""
        self.stage = Stage.BACKLOG

    # card weergave in terminal
    def print(self) -> str:
        return '\n'.join([
            "\n+-------------->\n"
            "| Cardnumber: {}".format(self.id),
            "| Title: {}".format(self.title),
            "| Team: {}".format(self.team),
            "| Project: {}".format(self.project),
            "| Stage: {}".format(self.stage.name),
            "| Description: {}".format(self.description),
            "+-------------->\n"
            ])

    # functie voor het ophalen van gebruikers input voor de card
    def fillCard(self):

        # vraag gebruiker om team en/of project
        user_team = input(constants.INP_TEAM)
        user_project = input(constants.INP_PROJECT)
        while user_team == "" and user_project == "":
            print(constants.MSG_CLIENT_NO_TEAMORPROJECT)
            user_team = input(constants.INP_TEAM)
            user_project = input(constants.INP_PROJECT)
            
        # vraag gebruiker om titel
        user_title = input(constants.INP_TITLE)
        while user_title == "" or len(user_title) > config.MAX_TITLE_LENGTH:
            print(constants.MSG_CLIENT_TITLE_BLANK)
            user_title = input(constants.INP_TITLE)
            
        # vraag gebruiker om omschrijving
        user_description = input(constants.INP_DESCRIPTION)
        while len(user_description) > config.MAX_DESCRIPTION_LENGTH:
            print(constants.MSG_CLIENT_TITLE_BLANK)
            user_title = input(constants.INP_DESCRIPTION)
        
        # verwerk input in kbcard object
        self.team = user_team
        self.project = user_project
        self.title = user_title
        self.description = user_description