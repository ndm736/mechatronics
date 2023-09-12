import board
import time
from analogio import AnalogIn # get access to analog pins

potentiometerpin = AnalogIn(board.A0) # on the Pico there are only 3 pins!

while 1:
    # the analog converter returns 0 for 0V, 65535 for 3.3V
    print(potentiometerpin.value)
    time.sleep(.1) # 10 times per second

    # or try these lines to format for the Plotter tool in Mu
    #volt = 3.3 * potentiometerpin.value / 65535
    #print("(" + str(volt) + ",)")
    #time.sleep(.1) # 10 times per second