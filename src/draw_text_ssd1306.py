# draw text on the I2C OLED SSD1306 display

import time
import board
import busio
import adafruit_ssd1306
# also requires adafruit_framebuf
# requires a font file in .bin format to be in CIRCUITYPY/ from:
#   https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/main/examples/font5x8.bin

i2c = busio.I2C(board.GP11, board.GP10) # the I2C pins used, (SCL, SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)

display.fill(0) # turn off every pixel in memory
display.show() # update the display

# use the following try..except block to make sure you have the font file
# once you know this works you can remove this section
try:
    display.fill(0)
    char_width = 6
    char_height = 8
    chars_per_line = display.width // 6
    for i in range(255):
        x = char_width * (i % chars_per_line)
        y = char_height * (i // chars_per_line)
        display.text(chr(i), x, y, 1)
    display.show()
    time.sleep(4)
    display.fill(0)
    display.show()
except FileNotFoundError:
    print(
        "Missing font file!"
    )
    while True:
        # no font file, get stuck here forever
        time.sleep() 

i = 0
while True:
    display.fill(0) # turn off all pixels (fill(1) to turn on all pixels)
    display.text("i = "+str(i), 0, 10, 1) # write text to left corner at x,y,pixel on
    display.show()
    time.sleep(0.01)
    i=i+1
    
