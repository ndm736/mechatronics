# play a tone 

import time
import array
import math
import audiocore # library to play a sound
import board
import audiobusio # library to use I2S to communicate with MAX98357 amplifier

# for the MAX98357 amplifier
# Vin can be 3.3V or 5V, 5V is louder
# SD is shutdown if put to GND
# Gain: loudest with 100k to GND, loud straight to GND, regular no connection, 
#       quieter straight to VIN, quietest 100k to VIN
audio = audiobusio.I2SOut(board.GP0, board.GP1, board.GP2) # I2S pins BCLK, LRC, DIN

tone_volume = 0.5  # digital volume, 0.0 to 1.0
frequency = 440  # tone frequency
samplerate = 8000
length = samplerate // frequency # // takes the floor() after doing the division
# make an array of signed 16bit values, which is what the MAX98357 takes
sine_wave = array.array("h", [0] * length) # the values are all initially 0

# make a single cycle of a sine wave to be played at 8kHz
for i in range(length):
    sine_wave[i] = int((math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))
sine_wave_sample = audiocore.RawSample(sine_wave)

while True:
    audio.play(sine_wave_sample, loop=True)
    time.sleep(1)
    audio.stop()
    time.sleep(1)
