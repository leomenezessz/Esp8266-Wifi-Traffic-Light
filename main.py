from lib.board import PinsOutputManager
from lib.socket_manager import SocketManager


def main():
    SocketManager(url="", port=80, listen=10, pins=PinsOutputManager(green=12, yellow=13, red=2)).start()


if __name__ == '__main__':
    main()
