from time import sleep
import network
from lib.logging import Logger

logger = Logger(__name__)


class WifiManager:

    def __init__(self, ssid, password):
        """
        This class have the responsibility to manage the connection of ESP8266 to the local wlan.

        :param ssid: Your network name.
        :param password: Your network password.
        """

        logger.info("Starting wifi connection...")

        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        self._waiting_connection()

    def _waiting_connection(self):
        conn = "."

        while not self.wlan.isconnected():
            sleep(1)
            conn = conn + conn
            logger.info(conn)

    def is_connected(self):
        """
        Check if you have been connected.

        :return: True to connected and False to not connected.
        """

        return self.wlan.isconnected()

    def network_config(self):
        """
        Get connection configuration data and convert this tuple to str.

        :return: Return a str representing :IP address, subnet mask, gateway and DNS server.
        """

        return " , ".join(self.wlan.ifconfig())
