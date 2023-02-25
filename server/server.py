import socket

import random
from typing import Dict
if __name__ == '__main__':
    from player import Player
    from logger import dbg_logger
else:
    from .player import Player
    from .logger import dbg_logger

class Server(socket.socket):
    def __init__(self, addr:str, port:int) -> None:
        super().__init__(socket.AF_INET)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.addr = addr
        self.port = port
        self.players:Dict[str, Player] = {}
        self.bind((addr, port))
        self.listen(6)

    def register(self):
        '''
        [Client]                            [Server]
            |    -- REGISTER <NICKNAME> -->     |
            |                                   |
            |    <----       OK        ----     |
            |                                   |
        '''
        while len(self.players) < 6:
            conn, addr = self.accept()
            b = conn.recv(1024)
            dbg_logger.debug(f"收到来自 {addr[0]}:{addr[1]} 的连接")
            try:
                msg = b.decode('utf-8')
            except UnicodeDecodeError:
                conn.close()
                dbg_logger.debug(f"{addr[0]}:{addr[1]} 消息解码错误")
            if not msg.startswith('REGISTER'):
                conn.close()
                dbg_logger.debug(f"{addr[0]}:{addr[1]} 注册格式错误")
                continue
            nickname = msg.split()[1]
            player = Player(nickname)
            player.socket = conn
            self.players[nickname] = player
            player.socket.send(b'OK')
            dbg_logger.debug(f"{addr[0]}:{addr[1]} 注册了ID \"{nickname}\"")

    def determine_camp(self):
        """向玩家分发阵营牌
        """
        camps = ['BLUE', 'BLUE', 'BLUE', 'RED', 'RED', 'RED']
        random.shuffle(camps)
        for num, nickname in enumerate(self.players):
            self.players[nickname].socket.send(camps[num].encode())
            dbg_logger.debug(f'向玩家 {nickname} 发放了 {camps[num]} 身份')
