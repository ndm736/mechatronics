import board
import neopixel_write # a simple method for setting a neopixel color
import digitalio
import time

# connect the pin to the neopixel DIN
pin = digitalio.DigitalInOut(board.GP13)
pin.direction = digitalio.Direction.OUTPUT

pixel_off = bytearray([0, 0, 0]) # R,G,B value, 0 for off, 255 for full on
red = bytearray([255,0,0])
green = bytearray([0,255,0])
blue = bytearray([0,0,255])
neopixel_write.neopixel_write(pin, pixel_off)

while True:
    neopixel_write.neopixel_write(pin, red)
    time.sleep(1)
    neopixel_write.neopixel_write(pin, green)
    time.sleep(1)
    neopixel_write.neopixel_write(pin, blue)
    time.sleep(1)
