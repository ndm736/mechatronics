import board
import neopixel_write
import digitalio

pin = digitalio.DigitalInOut(board.GP13)
pin.direction = digitalio.Direction.OUTPUT
pixel_off = bytearray([0, 0, 0])
neopixel_write.neopixel_write(pin, pixel_off)