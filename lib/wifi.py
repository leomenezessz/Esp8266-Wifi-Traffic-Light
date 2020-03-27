from time import sleep

import network


class WifiManager:

    def __init__(self, ssid, password):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        self._waiting_connection()

    def _waiting_connection(self):
        conn = "."

        while not self.wlan.isconnected():
            sleep(1)
            conn = conn + conn
            print(conn)

    def is_connected(self):
        return self.wlan.isconnected()

    def show_networks(self):
        return self.wlan.ifconfig()
