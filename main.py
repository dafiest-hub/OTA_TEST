from machine import Pin
from time import sleep
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/kevinmcaleer/ota_test/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test_ota.py")

ota_updater.download_and_install_update_if_available()

led = Pin(2, Pin.OUT) 

def main():
    while True:
        led.value(not led.value())  # Cambia el estado del LED
        sleep(0.3)  # Espera 1 segundo


if __name__ == "__main__":
    main()