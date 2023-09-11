import board # the pin definitions
import time
import digitalio # get access to digital pins

# make pin GP14 a digital output
greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

# build a LED circuit form GP14 to GND
while 1:
    greenled.value = 1 # turn on the LED
    time.sleep(.1) # wait
    greenled.value = 0 # turn off the LED
    time.sleep(.1) # wait