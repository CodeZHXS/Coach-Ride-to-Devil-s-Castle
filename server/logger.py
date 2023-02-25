import logging
if __name__ == '__main__':
    from colors import Colors
else:
    from .colors import Colors

logger = logging.getLogger('client')
handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
fmt = logging.Formatter(f"{Colors.YELLOW}[%(levelname)s]:{Colors.NORMAL} %(message)s")
handler.setFormatter(fmt)
logger.addHandler(handler)

dbg_logger = logging.getLogger('debug')
handler = logging.StreamHandler()
dbg_logger.setLevel(logging.DEBUG)
fmt = logging.Formatter(f"{Colors.YELLOW}[%(levelname)s] %(funcName)s (%(filename)s:%(lineno)s):{Colors.NORMAL}{Colors.GREEN} %(message)s{Colors.NORMAL}")
handler.setFormatter(fmt)
dbg_logger.addHandler(handler)
