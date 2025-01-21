from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT) 

def main():
    while True:
        led.value(not led.value())  # Cambia el estado del LED
        sleep(0.1)  # Espera 1 segundo
        print("Actualizando...")


if __name__ == "__main__":
    main()
