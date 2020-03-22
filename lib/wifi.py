from time import sleep

import network

WLAN = network.WLAN(network.STA_IF)


def connect_to_wifi(ssid, password):
    WLAN.connect(ssid, password)
    _waiting_connection()


def _waiting_connection():
    conn = "."

    while not WLAN.isconnected():
        sleep(1)
        conn = conn + conn
        print(conn)


def is_connected():
    return WLAN.isconnected()


def show_network():
    return WLAN.ifconfig()