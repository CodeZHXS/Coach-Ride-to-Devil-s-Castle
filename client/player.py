from cards import Card

class Player(object):
    def __init__(
        self,
        nickname:str
    ) -> None:
        self.nickname:str = nickname
        self.camp:Card = None
        self.profession:Card = None
        self.cards_holding = []
    
