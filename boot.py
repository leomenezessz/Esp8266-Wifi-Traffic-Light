from lib.logging import Logger
from lib.wifi import WifiManager

logger = Logger(__name__)


def main():
    wifi = WifiManager('your-ssid', 'your-network-password')

    if wifi.is_connected():
        logger.info("Connected to the network : " + wifi.show_networks())


if __name__ == '__main__':
    main()
