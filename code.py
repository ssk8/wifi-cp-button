import os
import time
import ssl
import wifi
import socketpool
import microcontroller
import adafruit_requests
import board
import digitalio

button = digitalio.DigitalInOut(board.GP19)
button.switch_to_input(pull=digitalio.Pull.UP)


wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


while True:
    time.sleep(0.5)
    if not button.value:
        print("attemp post")
        response = requests.post(os.getenv('NTFY_ADDRESS'), data="button pressed")
        print(response.text)
