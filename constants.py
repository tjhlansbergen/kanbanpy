
""" constants.py: Constanten voor de kanbanpy client applicatie
    Auteur: Tako Lansbergen, Novi Hogeschool
    Studentnr.: 800009968
    Leerlijn: Python
    Datum: 18 nov 2019
"""

APP_NAME = "kanbanpy"
APP_VERSION = "v1.0"

KB_OK = "succes"
KB_NOT_OK = "error"
KB_PROMPT = ">> "

DB_FILE = ".kanbanpy.db"
INTERFACE_COMMANDS = ('create','read','update','delete','select')

INP_SERVER_CLIENT = "Run as server or client (s/c)? "
INP_TEAM = "Specify a team name, or leave blank: "
INP_PROJECT = "Specify a project name, or leave blank: "
INP_TITLE = "Specify a title for your card (max 20 characters): "
INP_DESCRIPTION = "Specify a description (max 250 characters): "
INP_CARDNUMBER = "Specify Card number: "
INP_STAGE = "Specify stage (Backlog, ToDo, Doing, Done): "

ERR_SENDING_REQUEST = "Error sending request to server: "
ERR_RECEIVING_REQUEST = "Error, a request was send but not succesfully received "
ERR_DB_CREATION = "Error bij het aanmaken van een nieuwe database: "
ERR_DB_INSERTION = "Error bij het invoegen van nieuwe data in de database: "
ERR_IO_ERROR = "Error bij het schrijven naar bestand: "
ERR_SERVER_RUNNING = "Kanbanpy SERVER is already running, please type exit to exit!"

MSG_UNKNOWN_COMMAND = "Unknown command, type help for available options"
MSG_NOT_IMPLEMENTED = "Not yet implemented!"

MSG_SERVER_LISTENING = "Server is listening on port:"
MSG_SERVER_INCOMING = "Connection coming from:"
MSG_SERVER_DATARECEIVED = "bytes of incoming data"
MSG_SERVER_DBCREATE = "CREATE: Adding item to database with ID ="
MSG_SERVER_DBREAD = "READ: Returning item with ID ="
MSG_SERVER_DBUPDATE = "UPDATE: Editing item with ID ="
MSG_SERVER_DBDELETE = "DELETE: Removing card from database with ID ="
MSG_SERVER_DBSELECT = "SELECT: Returning selection of cards in database, count ="
MSG_SERVER_INCORRECTTYPE = "Incoming data not accepted, payload is of incorrect type"
MSG_SERVER_RESULT = "Requested item returned"
MSG_SERVER_NORESULT = "Requested item not found"

MSG_CLIENT_TITLE_BLANK = "Card title should not be blank or too long"
MSG_CLIENT_DESCRIPTION_TOLONG = "Card description is too long"
MSG_CLIENT_NO_TEAMORPROJECT = "Team and project cannot both be blank, please specify either a team name, a project name or both"
MSG_CLIENT_INVALID_CARDNUMBER = "Sorry, that's not a valid card number"
MSG_CLIENT_INVALID_STAGE = "Sorry, that's not a valid stage name"
MSG_CLIENT_NOCARD = "No card(s) found"
MSG_CLIENT_HELP = """
=============================================================================================
The following options are available on the commandline:

  create card:    Adds a new card to the repository, pinned to either a project, a team or both
  read card:      Reads a single card from the repository
  move card:      Edits the stage of an existing card in the repository
  delete card:    To permanently delete a card from the repository
  list cards:     Lists all cards

  show board:     Generates HTML view for your tasks based on project, team or both
  refresh board:  Generates HTML like above, but without opening a browser window

  help:           Displays this manual
  exit:           To exit the kanbanpy CLIENT program

=============================================================================================
"""
MSG_SERVER_HELP = """
=============================================================================================
The following options are available on the commandline:

  help:         Displays this manual
  exit:         To exit the kanbanpy SERVER program

=============================================================================================
"""