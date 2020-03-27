from lib.bridge import Bridge
from lib.logging import Logger
from lib.server import SocketManager

logger = Logger(__name__)


def main():
    logger.info("Main module is starting...")

    SocketManager(url="", port=3333, listen=10, bridge=Bridge(0, 9600)).start()


if __name__ == '__main__':
    main()
