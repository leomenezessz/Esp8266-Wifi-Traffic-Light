from socket import socket, AF_INET, SOCK_STREAM
from lib.bridge import Bridge
from lib.logging import Logger

logger = Logger(__name__)


class SocketManager:
    _SUCCESS = "HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n"
    _FAIL = "HTTP/1.0 404 OK\r\nContent-type: application/json\r\n\r\n"

    def __init__(self, url, port, listen, bridge: Bridge):
        """
        Initialize socket server to allow client connections.

        :param url: Server url.
        :param port: Server port.
        :param listen: Simultaneous users.
        :param bridge: A bridge to serial communication and the paths requests pattern.

        """

        logger.info("Starting socket server...")

        self.soc = socket(AF_INET, SOCK_STREAM)
        self.soc.bind((url, port))
        self.soc.listen(listen)
        self.client = None
        self.pins = bridge

        logger.info("Server has been started.")

    def start(self):
        while True:

            self.client, addr = self.soc.accept()

            data = self.client.recv(1024)

            if self.pins.send_data(data):
                self.client.send(self._SUCCESS)
            else:
                self.client.send(self._FAIL)

            self.client.close()
