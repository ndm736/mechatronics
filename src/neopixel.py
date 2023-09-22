import time
import board
import neopixel # copy neopixel.mpy from library bundle into CIRCUITPY/lib

din_pin = board.GP17 # the pin connected to the neopixel DIN
num_pixels = 8 # how many neopixels in the strip

ORDER = neopixel.GRB # sometimes a strip is RGB, depends on the manufacturer

# make a variable to represent all the pixel LEDs
# neopixels are painfully bright, the brightness setting scales them to not be too powerful
pixels = neopixel.NeoPixel(din_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

pixels.fill((0, 0, 0)) # set the value of every pixel to off
pixels.show() # send the values to the strip, this function must be called to make the colors appear

while True:
    pixels.fill((0, 255, 0)) # set every pixel to green
    pixels.show()
    time.sleep(1)
    
    pixels.fill((0, 0, 0)) # set every pixel to off
    pixels[0] = (255,0,0) # first pixel to red
    pixels[1] = (0,255,0) # second pixel to green
    pixels[2] = (0,0,255) # third pixel to blue
    pixels.show()
    time.sleep(1)
