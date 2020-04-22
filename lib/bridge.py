import machine

RED = "/red"
YELLOW = "/yellow"
GREEN = "/green"


class Bridge:

    def __init__(self, identification, baud):

        """
        Start serial port with a id and a specific baud rate.


        :param identification: Its id for UART can be 0 or 1.
        :param baud: The baud rate of data transfer.
        """

        self.bridge = machine.UART(identification, baud)

    def send_data(self, data):
        """

        This function receive request and send the color to arduíno
        serial port.


        :param data: Request bytes with all data of request.
        :return: True if request contain a valid data and False to a invalid request.
        """

        if GREEN in data:
            self.bridge.write("green")
        elif YELLOW in data:
            self.bridge.write("yellow")
        elif RED in data:
            self.bridge.write("red")
        else:
            return False
        return True
