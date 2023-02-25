from .cards import Card
from socket import socket

class Player(object):
    def __init__(
        self,
        nickname:str
    ) -> None:
        self.nickname:str = nickname
        self.camp:Card = None
        self.profession:Card = None
        self.cards_holding = []
        self.socket:socket = None

    