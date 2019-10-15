
""" client_constants.py: Constanten voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 15 okt 2019
"""

APP_NAME = "kanbanpy"
APP_VERSION = "v0.1"

MSG_UNKNOWN_COMMAND = "Unknown command, type help for available options"
MSG_NOT_IMPLEMENTED = "Method not yet implementend!"
MSG_HELP_MSG = """
=============================================================================================
The following options are available on the commandline:

  create card:  Adds a new card to the repository, pinned to either a project, a team or both
  read card:    Reads a single card from the repository
  update card:  To edit an existing card in the repository
  delete card:  To permanently delete a card from the repository

  list board:   To list all cards filterd by team, project or both
  pretty board: Shows all cards for a team, project or team + project in a browser

  help:         Displays this manual
  exit:         To exit from the kanbanpy program

=============================================================================================
"""