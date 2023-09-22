import time
import board
import busio

import adafruit_mpr121 # library for the MPR121 cap touch board

i2c = busio.I2C(board.GP11, board.GP10) # the I2C pins used, (SCL, SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    # get the raw data from the pins
    pin0 = mpr121.filtered_data(0)
    pin6 = mpr121.filtered_data(6)
    pin11 = mpr121.filtered_data(11)
    # print in the format that the Plotter uses
    print("("+str(pin0)+","+str(pin6)+","+str(pin11)+",)")
    time.sleep(0.1)
