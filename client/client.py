import socket
import random
from typing import Dict
if __name__ == '__main__':
    from player import Player
    from cards import *
    from logger import logger
    from colors import Colors
else:
    from .player import Player
    from .cards import *
    from .logger import logger
    from .colors import Colors

class Client(socket.socket):
    def __init__(self, addr:str, port:int) -> None:
        super().__init__(socket.AF_INET)
        self.addr = addr
        self.port = port
        self.player = None
        self.connect((self.addr, self.port))

    def register(self, nickname:str):
        '''
        [Client]                            [Server]
            |    -- REGISTER <NICKNAME> -->     |
            |                                   |
            |    <----       OK        ----     |
            |                                   |
        '''
        self.player = Player(nickname)
        self.send(f'REGISTER {nickname}'.encode())

        if (msg := self.recv(2).decode()) != 'OK':
            self.close()
            logger.error('注册失败')
            logger.error(msg)
            return
        camp = self.recv(4).decode()

        if camp == 'RED':
            self.player.camp = RedCamp()
            logger.info(f'{Colors.RED}你的身份是: 真实谎言兄弟会成员{Colors.NORMAL}')
        elif camp == 'BLUE':
            self.player.camp = BlueCamp()
            logger.info(f'{Colors.BLUE}你的身份是: 公示机密联盟成员{Colors.NORMAL}')

