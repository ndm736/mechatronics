import board
import time
import digitalio

greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

buttonpin = digitalio.DigitalInOut(board.GP15)
buttonpin.direction = digitalio.Direction.INPUT

# global variables
buttonprevious = 1 # the default state of the button is 1
greenledstate = 0 # the initial state of the LED
buttonpressedcount = 0 # how many times the button has been pressed

while 1:
    # if the button vlaue changed from hight to low
    # this is the moment the button is pressed
    if buttonpin.value == 0 and buttonprevious == 1:
        # IMPLEMENT
        # wait a small amount of time and see if the button is still pressed
        # then:
        
        # change the state of the LED
        if greenledstate == 0:
            greenledstate = 1
        else:
            greenledstate = 0
        # add one to the number of times the button was pressed
        buttonpressedcount = buttonpressedcount + 1
        print(str(buttonpressedcount))
    
    # remember the button state for next time and set the LED
    buttonprevious = buttonpin.value
    greenled.value = greenledstate