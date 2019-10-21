
""" constants.py: Constanten voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 15 okt 2019
"""

APP_NAME = "kanbanpy"
APP_VERSION = "v0.5"

KB_SUCCES = "succes"
KB_PROMPT = ">> "

DB_FILE = ".kanbanpy.db"

INP_SERVER_CLIENT = "Run as server or client (s/c)? "
INP_TEAM = "Specify a team name, or leave blank: "
INP_PROJECT = "Specify a project name, or leave blank: "
INP_TITLE = "Specify a title for your card: "
INP_DESCRIPTION = "Specify a description (max 120 characters): "

ERR_SENDING_CARD = "Error sending card to server: "
ERR_RECIEVING_CARD = "Error, a card was send but not succesfully received "
ERR_DB_CREATION = "Error bij het aanmaken van een nieuwe database: "
ERR_DB_INSERTION = "Error bij het invoegen van nieuwe data in de database: "

MSG_TITLE_BLANK = "Card title should not be blank or too long"
MSG_DESCRIPTION_TOLONG = "Card description is too long"
MSG_NO_TEAMORPROJECT = "Team and project cannot both be blank, please specify either a team name, a project name or both"
MSG_UNKNOWN_COMMAND = "Unknown command, type help for available options"
MSG_NOT_IMPLEMENTED = "Not yet implemented!"
MSG_SERVER_LISTENING = "Server is listening on port:"
MSG_SERVER_INCOMING = "Connection coming from:"
MSG_SERVER_DATARECEIVED = "bytes of incoming data"
MSG_CLIENT_HELP = """
=============================================================================================
The following options are available on the commandline:

  create card:  Adds a new card to the repository, pinned to either a project, a team or both
  read card:    Reads a single card from the repository
  update card:  To edit an existing card in the repository
  delete card:  To permanently delete a card from the repository

  list board:   To list all cards filterd by team, project or both
  pretty board: Shows all cards for a team, project or team + project in a browser

  help:         Displays this manual
  exit:         To exit the kanbanpy program

=============================================================================================
"""
MSG_SERVER_HELP = """
=============================================================================================
The following options are available on the commandline:

  help:         Displays this manual
  exit:         To exit the kanbanpy program

=============================================================================================
"""