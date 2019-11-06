""" kbcard.py: card klasse, representeert één card op het kanban board
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 24 okt 2019
"""

from enum import Enum
from string import Template

import config
import constants
import kb_html

# enum voor de verschillende statussen die card kunnen hebben
class Stage(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4


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

    # override compare functie, zodat cards vergeleken worden aan de hand van id ipv hash
    def __eq__(self, other): 
        if not isinstance(other, KBCard):
            # alleen tegen hetzelfde type verglijken
            return NotImplemented
        # vergelijk op ID
        return self.id == other.id

    # methode voor het tonen van KBCard objecten op de commandline
    def print(self) -> str:
        return '\n'.join([
            "\n\n+-------------->\n"
            "| Cardnumber: {}".format(self.id),
            "| Title: {}".format(self.title),
            "| Team: {}".format(self.team),
            "| Project: {}".format(self.project),
            "| Stage: {}".format(self.stage.name),
            "| Description: {}".format(self.description),
            "+-------------->\n"
            ])

    # card weergave in lijst op de commandline
    def listprint(self) -> str:
        return ' '.join([str(self.id), self.title, "->", self.stage.name, "(t:", self.team, "p:", self.project, ")"])

    # card weergave als HTML
    def htmlprint(self) -> str:
        html = Template(kb_html.BLOCK)
        return html.safe_substitute(ID=self.id, TITLE=self.title, DESC=self.description, TEAM=self.team, PROJECT=self.project)

    # methode voor het ophalen van gebruikers input voor de card
    def fillCard(self):

        # vraag gebruiker om team en/of project
        user_team = input(constants.INP_TEAM).lower()
        user_project = input(constants.INP_PROJECT).lower()
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