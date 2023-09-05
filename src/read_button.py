import board
import time
import digitalio

greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

buttonpin = digitalio.DigitalInOut(board.GP15)
buttonpin.direction = digitalio.Direction.INPUT

while 1:
    if buttonpin.value == 0:
        greenled.value = 1
        print(“On!”)
    else:
        greenled.value = 0
        print(“off”)
    time.sleep(0.05) # 20 times per second
