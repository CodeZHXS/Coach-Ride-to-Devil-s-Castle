import socket
from player import Player

class Server(socket.socket):
    def __init__(self, addr:str, port:int) -> None:
        super.__init__(socket.AF_INET)
        self.addr = addr
        self.port = port
        self.players = {}
        self.socket = socket.socket(socket.AF_INET)
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
            try:
                msg = b.decode('utf-8')
            except UnicodeDecodeError:
                conn.close()
            if not msg.startswith('REGISTER'):
                conn.close()
                continue
            nickname = msg.split()[1]
            player = Player(nickname)
            player.socket = conn
            self.players[nickname] = player

