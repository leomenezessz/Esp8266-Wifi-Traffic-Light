import machine


class PinsOutputManager:

    def __init__(self, green: int, yellow: int, red: int):
        self.green = machine.Pin(green, machine.Pin.OUT)
        self.yellow = machine.Pin(yellow, machine.Pin.OUT)
        self.red = machine.Pin(red, machine.Pin.OUT)

    def all_pins_values(self):
        return [
            {"green": self.green.value()},
            {"yellow": self.yellow.value()},
            {"red": self.red.value()}
        ]

    def change_light_status(self, data):

        param = str(data).split()[1]

        try:
            value = int(param[-1::])
        except Exception as e:
            print(e)
            return False

        if param == "/?green=0" or param == "/?green=1":
            self.green.value(value)
        elif param == "/?yellow=0" or param == "/?yellow=1":
            self.yellow.value(value)
        elif param == "/?red=0" or param == "/?red=1":
            self.red.value(value)
        elif param == "/?lights=0":
            self.all_pins_values()
        else:
            return False

        return True


