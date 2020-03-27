import machine

from lib.logging import Logger

RED = "/red"
YELLOW = "/yellow"
GREEN = "/green"

logger = Logger(__name__)


class Bridge:

    def __init__(self, identification, baud):

        """
        Start serial port with a id and a specific baud rate.


        :param identification: Its id for UART can be 0 or 1.
        :param baud: The baud rate of data transfer.
        """

        self.bridge = machine.UART(identification, baud)

        logger.info("Serial port is enabled with id : " + str(identification) + " and baud : " + str(baud))

    def send_data(self, data):
        """

        This function receive request and send the color to arduíno
        serial port.


        :param data: Request bytes with all data of request.
        :return: True if request contain a valid data and False to a invalid request.
        """

        if GREEN in data:
            logger.info("Received a request to the path :" + GREEN)
            self.bridge.write("green")
        elif YELLOW in data:
            logger.info("Received a request to the path: " + YELLOW)
            self.bridge.write("yellow")
        elif RED in data:
            logger.info("Received a request to the path" + RED)
            self.bridge.write("red")
        else:
            logger.warning("Invalid request : " + str(data))
            return False

        logger.info("Data has been sent to arduíno")

        return True
