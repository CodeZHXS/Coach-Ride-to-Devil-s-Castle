from server.server import Server
from server.logger import dbg_logger

server = Server('0.0.0.0', 17623)
try:
    server.register()
    dbg_logger.debug(server.players)
    server.determine_camp()
except KeyboardInterrupt:
    server.close()
