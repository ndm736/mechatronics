import board
import time
import digitalio

greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

while 1:
    greenled.value = 1
    time.sleep(.1)
    greenled.value = 0
    time.sleep(.1)