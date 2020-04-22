from lib.bridge import Bridge
from lib.server import SocketManager


def main():
    SocketManager(url="", port=3333, listen=10, bridge=Bridge(0, 9600)).start()


if __name__ == '__main__':
    main()
