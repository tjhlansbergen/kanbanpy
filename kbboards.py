from abc import ABC, abstractmethod # ten behoeve van abstracte klasse (Abstract Base Class)
import pickle

import constants
from kbcard import KBCard, Stage

class Board(ABC):

    # constructor
    def __init__(self):
        self._cards = []    

    def set_cards(self, data):
        
        # controleer data
        cards = pickle.loads(data)

        # data niet in orde, doe niets
        if type(cards) != list:
            return

        # data niet in orde, doe niets
        if type(cards[0]) != KBCard:
            return

        # data in orde, voeg toe
        if not self._cards:
            # er zijn nog geen cards toegevoegd, voeg alles toe wat binnen komt
            self._cards = cards
        else:
            # board heeft al card, pas totaal cards aan naar de intersectie van de reeds aanwezige en nieuw toe te voegen met list-comprehension
            self._cards = [card for card in cards if card in self._cards]



    def create(self):
        print("Cards: ", len(self._cards)) 
        for card in self._cards:
            print(card.listprint())


class TeamBoard(Board):
     
    # constructor
    def __init__(self, teamname: str):
         super().__init__()
         self._teamname = teamname
         
    # functie voor het ophalen van de cards met de gevraagde teamname
    def getRequests(self) -> list:
        try:
            return [pickle.dumps(("select", ("team", '"{0}"'.format(self._teamname))))]   # omvat teamname in quotes
        except pickle.PickleError:
            return []


class ProjectBoard(Board):
    
    # constructor
    def __init__(self, projectname: str):
        super().__init__()
        self._projectname = projectname
         

    # functie voor het ophalen van de cards met de gevraagde teamname
    def getRequests(self) -> list:
        try:
            return [pickle.dumps(("select", ("project", '"{0}"'.format(self._projectname))))] # omvat projectname in quotes
        except pickle.PickleError:
            return []


class TeamProjectBoard(TeamBoard, ProjectBoard):

    # constructor
    def __init__(self, teamname: str, projectname: str):
        # roep contructor van superklasse aan op naam zodat de juiste gebruikt wordt
        Board.__init__(self)

        self._teamname = teamname
        self._projectname = projectname

    # override getRequest om een resultaat van beide parents samen te voegen
    def getRequests(self) -> list:
        tr = TeamBoard.getRequests(self)
        pr = ProjectBoard.getRequests(self)

        # merge en retourneer resultaat
        return tr + pr
