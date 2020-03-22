import json
from socket import socket, AF_INET, SOCK_STREAM
from lib.board import PinsOutputManager


class SocketManager:

    _SUCCESS = "HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n"
    _FAIL = "HTTP/1.0 404 OK\r\nContent-type: application/json\r\n\r\n"

    def __init__(self, url, port, listen, pins: PinsOutputManager):
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.soc.bind((url, port))
        self.soc.listen(listen)
        self.client = None
        self.pins = pins

    def start(self):
        while True:
            self.client, addr = self.soc.accept()
            data = self.client.recv(1024)

            if self.pins.change_light_status(data):
                self.client.send(self._SUCCESS)
                self.client.send(json.dumps(self.pins.all_pins_values()))
            else:
                self.client.send(self._FAIL)

            self.client.close()





