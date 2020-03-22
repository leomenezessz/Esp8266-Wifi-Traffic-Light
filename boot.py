from lib.wifi import connect_to_wifi, is_connected, show_network


def main():
    connect_to_wifi('***********', '***********')

    if is_connected():
        print("Connected to the network : ", show_network())


if __name__ == '__main__':
    main()
