# read from the hc-sr04 ultrasonic rangefinder
# works best with 5V from VBUS for VCC

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)

while True:
    try:
        print((sonar.distance,)) # in cm
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)
