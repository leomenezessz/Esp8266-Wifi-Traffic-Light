from lib.logging import Logger
from lib.wifi import WifiManager

logger = Logger(__name__)


def main():
    wifi = WifiManager('Americana 2.4G', 'lully360')

    if wifi.is_connected():
        logger.info("Connected to the network : " + wifi.network_config())


if __name__ == '__main__':
    main()
