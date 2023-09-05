import board
import time
from analogio import AnalogIn

potentiometerpin = AnalogIn(board.A0)

while 1:
    print(potentiometerpin.value)
    time.sleep(.1) # 10 times per second

    # or try these lines to format for the Plotter tool
    #volt = 3.3 * potentiometerpin.value / 65535
    #print("(" + str(volt) + ",)")
    #time.sleep(.1) # 10 times per second