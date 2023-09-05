import board
import time
import digitalio

greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

buttonpin = digitalio.DigitalInOut(board.GP15)
buttonpin.direction = digitalio.Direction.INPUT

buttonprevious = 1
greenledstate = 0
buttonpressedcount = 0

while 1:
    if buttonpin.value == 0 and buttonprevious == 1:
        if greenledstate == 0:
            greenledstate = 1
        else:
            greenledstate = 0
        buttonpressedcount = buttonpressedcount + 1
        print(str(buttonpressedcount))
    
    buttonprevious = buttonpin.value
    greenled.value = greenledstate